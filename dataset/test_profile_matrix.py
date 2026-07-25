from dataset.utils.profile_matrix_generator import ProfileMatrixGenerator

generator = ProfileMatrixGenerator()

count = 0

for profile in generator.generate():

    count += 1

print(f"Generated {count} valid profiles")
