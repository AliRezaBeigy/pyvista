"""
.. _movie_example:

Create a MP4 Movie
~~~~~~~~~~~~~~~~~~

Create an animated MP4 movie of a rendering scene.
This example uses :meth:`~pyvista.Plotter.open_movie` and
:meth:`~pyvista.Plotter.write_frame` to create the movie.

.. Note::
    This movie will appear static since MP4 movies will not be
    rendered on a sphinx gallery example.

"""

from __future__ import annotations

import numpy as np

import pyvista as pv

filename = 'sphere-shrinking.mp4'

# Create a sphere with random data. Seed the rng to make it reproducible.
rng = np.random.default_rng(seed=0)
mesh = pv.Sphere()
mesh.cell_data['data'] = rng.random(mesh.n_cells)

plotter = pv.Plotter()
# Open a movie file
plotter.open_movie(filename)

# Add initial mesh
plotter.add_mesh(mesh, scalars='data', clim=[0, 1])
# Add outline for shrinking reference
plotter.add_mesh(mesh.outline_corners())

plotter.show(auto_close=False)  # only necessary for an off-screen movie

# Run through each frame
plotter.write_frame()  # write initial data

# Update scalars on each frame
for i in range(100):
    random_points = rng.random(mesh.points.shape)
    mesh.points = random_points * 0.01 + mesh.points * 0.99
    mesh.points -= mesh.points.mean(0)
    mesh.cell_data['data'] = rng.random(mesh.n_cells)
    plotter.add_text(f'Iteration: {i}', name='time-label')
    plotter.write_frame()  # Write this frame

# Be sure to close the plotter when finished
plotter.close()
# %%
# .. tags:: plot
