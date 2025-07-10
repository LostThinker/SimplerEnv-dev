## 🧩 Using Hunyuan3D to Generate and Import Assets into SimplerEnv

This section provides a step-by-step guide to generating 3D assets with **Hunyuan 3D** and integrating them into the **SimplerEnv** environment.

### 📦 Step 1: Generate 3D Assets with Hunyuan3D

Use Hunyuan3D to create high-quality 3D object assets from text or image prompts.

- Visit: [Hunyuan3D](https://3d.tencent.com/hunyuan)
- Make sure to select **3D Intelligent Topology (3D智能拓扑)** as the output type to ensure better mesh structure and compatibility.
- Choose your generation method (text-to-3D or image-to-3D).
- Export the generated model in `.glb` format.

### 🧰 Step 2: Verify and Re-export the Asset via Blender

#### Import the `.glb` File
1. Open [Blender](https://www.blender.org/).
2. Delete all default objects in the scene
3. Go to `File > Import > glTF 2.0 (.glb/.gltf)` and load the generated file.
4. Verify that:
    - The mesh appears correctly.
    - The object is properly centered and scaled.
    - There are no broken materials or geometry.

#### Export the '.dae' and '.obj' Files
1. Go to `File > Export > Collada (.dae)`, export the file as **`textured.dae`** using the settings shown below:  
   ![Figure 1: Recommended DAE export settings](path/to/figure1.png)
2. Go to `File > Export > Wavefront (.obj)`, export the file as **`collision.obj`** using the settings shown below:  
   ![Figure 2: Recommended OBJ export settings](path/to/figure2.png)
3. You will then get the following three files:
   ![Figure 2: Recommended OBJ export settings](path/to/figure3.png)
4. Put these three files into a single folder and give it a name, for example, **`my_obj`**. 

### 🗂️ Step 3: Import the Exported Files into SimplerEnv
1. Copy the exported folder to `SimplerEnv-dev/ManiSkill2_real2sim/data/custom/models/`

2. Open the file `SimplerEnv-dev/ManiSkill2_real2sim/data/custom/info_bridge_custom_v1.json` and add a configuration entry for your imported object, for example:
```json
"my_obj": {
  "bbox": {
    "min": [],
    "max": []
  },
  "scales": [0.1],
  "density": 200
}
```
3. Go back to Blender, open the Scripting tab, and paste the following code into the console to calculate the bounding box in world coordinates:
```python
import bpy
import mathutils

# Get the currently selected object
obj = bpy.context.active_object

# Get the 8 corners of the bounding box in world coordinates
bbox_corners = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]

# Calculate min and max coordinates along each axis
min_x = min(corner.x for corner in bbox_corners)
max_x = max(corner.x for corner in bbox_corners)

min_y = min(corner.y for corner in bbox_corners)
max_y = max(corner.y for corner in bbox_corners)

min_z = min(corner.z for corner in bbox_corners)
max_z = max(corner.z for corner in bbox_corners)

# Calculate half dimensions (length, width, height)
length = (max_x - min_x) / 2
width = (max_y - min_y) / 2
height = (max_z - min_z) / 2

print("Bounding box dimensions (world coordinates):")
print(f"bbox_min: -{length:.4f}, -{width:.4f}, -{height:.4f}")
print(f"bbox_max: {length:.4f}, {width:.4f}, {height:.4f}")
```
Then fill in the `bbox` fields in the JSON config file using the printed values.

4. Use the script `SimplerEnv-dev/ManiSkill2_real2sim/check_obj.py` to visualize your object and adjust the scales parameter in the config file accordingly:
```python
python check_obj.py --obj_name my_obj
```





