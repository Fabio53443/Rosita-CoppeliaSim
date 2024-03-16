# ROSITA in CoppeliaSim

## What is this?
This repo hosts our ([Marte(llo) team](https://rositascuola.altervista.org/team-martello-%f0%9f%94%a8-liceo-scientifico-l-spallanzani-tivoli-rm/)) attempt at making a somewhat working and accurate replica of the 4WD ROSITA rover.

## Installation

1. Install CoppeliaSim from [here](https://www.coppeliarobotics.com/)
2. Clone this repo
3. Install dipendencies (`pip -r requirements.txt`)
# IMPORTANT: Apply patch to Coppelia's remote API
append to `<installFolder>/addOns/ZMQ remote API server.lua` the following **before** opening Coppelia
```
sim.saveImage = wrap(sim.saveImage, function(origFunc)
    return function(img, res, opt, nm, q)
        local ret = origFunc(img, res, opt, nm, q)
        if type(ret) ~= 'string' then
            ret = ''
        end
        return ret
    end
end)
```
## Using it  
1. In Coppelia, run the simulation
2. Write your code in "src/main.py", and run that.

### Available functions: 
1. `getImage()` - Will shoot a picture from the built in virtual camera and save it in a `pictures` folder inside the repo folder. Returns the path to which the picture was saved.
2. `scanTag(path)` - Will check any image for one or more QR Code and return values found. Meant to be used with as `scanTag(getImage())`.
3. `pan(rad)` and `tilt(rad)` - Pans or tilts the camera. Angle in radiants.
4. `setSpeed4W(fl, fr, bl, br, time)` - Sets the wheels' speed, respectively, front left, front right, back left, back right, for a determinted amount of time (provided in seconds as a parameter).
5. `stop()` - Sets the speed of all the wheels to 0.

Thanks to the CoppeliaSim team for providing the patch
(see [CoppeliaSim Forum](https://forum.coppeliarobotics.com/viewtopic.php?p=40407#p40407) for more details. 
## Development
The reccomanded way to develop this project is by using **venv**s. This can be done, in Pycharm, by cloning the repository and by answering "yes" in the venv prompt. 
## Screenshots
![image](https://github.com/Fabio53443/Rosita-CoppeliaSim/assets/64356481/023bf7d7-df3b-4862-91e2-a214a03d1fbf)
![image](https://github.com/Fabio53443/Rosita-CoppeliaSim/assets/64356481/a2311abc-17b4-4b8a-be66-6a3068ff76ca)
