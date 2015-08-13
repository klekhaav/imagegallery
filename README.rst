=====
Image Gallery
=====

Simple image gallery app. Support Author and types of images.

Quick start
-----------

1. Add "image" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'image',
    )

2. Include the image URLconf in your project urls.py like this::

    url(r'^image/', include('image.urls', namespace='image')),

3. Run `python manage.py migrate` to create the image models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to add new image or Author (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/image/ to look at the gallery.
