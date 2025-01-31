import folium
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from folium.plugins import FastMarkerCluster
from folium.plugins import AntPath

from main.forms import ContactFormModelForm, FeaturedFormModelForm
from main.models import BlogPost, Comment, Category, Tag, EVStation


# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def blogs(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # Fetch latest posts
    return render(request, 'blogs.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)  # Fetch post by ID or return 404
    return render(request, 'blog_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactFormModelForm()

    return render(request, 'contact.html', {'form': form})


def featured(request):
    if request.method == 'POST':
        form = FeaturedFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('featured')
    else:
        form = FeaturedFormModelForm()
    return render(request, 'featured.html')


def about(request):
    return render(request, 'about.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def team(request):
    return render(request, 'team.html')


def explore(request):
    stations = EVStation.objects.all()

    # Map centered on Nairobi
    m = folium.Map(location=[-1.286389, 36.817223], zoom_start=10, tiles="CartoDB positron")



    # Add markers for each station
    for station in stations:
        coordinates = (station.latitude, station.longitude)
        popup_html = f"""
                        <div style="width: 200px;">
                            <h4>{station.name}</h4>
                            <h4>{station.charging_types}</h4>
                        </div>
                    """
        folium.Marker(coordinates, popup=folium.Popup(popup_html, max_width=250),icon=folium.Icon(color="green", icon="plug", prefix="fa"),).add_to(m)  # Add station name as popup
    #fastmarker to generate clusters
    # latitudes = {station.latitude for station in stations}
    # longitudes = {station.longitude for station in stations}
    #
    # FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(m)

    # Create context after loop finishes
    context = {'map': m._repr_html_()}

    return render(request, 'explore.html', context)  # Return response after loop


def whyevision(request):
    return render(request, 'whyevision.html')


def routeplanner(request):
    # Default: Nairobi
    user_lat = -1.286389
    user_lon = 36.817223

    # Get user location from URL parameters
    if 'lat' in request.GET and 'lon' in request.GET:
        try:
            user_lat = float(request.GET['lat'])
            user_lon = float(request.GET['lon'])
        except ValueError:
            pass  # Invalid input, fallback to default

    # Create map centered on user's location
    m = folium.Map(location=[user_lat, user_lon], zoom_start=12, tiles="CartoDB positron")

    # Add user marker
    folium.Marker(
        [user_lat, user_lon],
        popup="You are here",
        icon=folium.Icon(color="blue", icon="user")
    ).add_to(m)

    # Find nearest charging station
    stations = EVStation.objects.all()
    if stations.exists():
        nearest_station = min(
            stations, key=lambda station: (station.latitude - user_lat) ** 2 + (station.longitude - user_lon) ** 2
        )
        station_lat, station_lon = nearest_station.latitude, nearest_station.longitude

        # Add station marker
        folium.Marker(
            [station_lat, station_lon],
            popup=f"Nearest Charging Station: {nearest_station.name}",
            icon=folium.Icon(color="green", icon="plug")
        ).add_to(m)

        # Draw route using AntPath
        AntPath([(user_lat, user_lon), (station_lat, station_lon)], color="blue").add_to(m)

    context = {'map': m._repr_html_()}
    return render(request, 'routeplanner.html', context)


def getfeatured(request):
    return render(request, 'getfeatured.html')