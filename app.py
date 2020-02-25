from flask import Flask, render_template, request
import folium
import geocoder
import twitter


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    This function generates
    the index default page.
    """
    return render_template("index.html")


@app.route("/map", methods=["POST"])
def map():
    """
    This function creates a html file that contains
    a map.
    """
    def location_finder(locs):
        """
        (list) -> list
        This function gets the coordinates of the locations
        using geocoder and OpenStreetMap.
        """
        locations = []
        for loc in locs:
            g = geocoder.osm(loc[1]).latlng
            if g:
                locations.append((loc[0], g))
        return locations

    if request.method == "POST":
        username = request.form['username']
    if len(username) < 1:
        return render_template("failure.html")
    else:
        locations = location_finder(twitter.get_twitter_info(username))
        if len(locations) == 0:
            return render_template("failure.html")
        m = folium.Map(zoom_start=5, locations=[locations[0][1][0], locations[0][1][1]])

        for i in locations:
            name = i[0]
            loc = [i[1][0], i[1][1]]
            folium.Marker(loc, color='beige', tooltip=name).add_to(m)
        result = m.get_root().render()
        return result



if __name__ == "__main__":
    app.run(debug=True)