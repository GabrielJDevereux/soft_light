# soft_light
Soft_Light_Calculators
The following is designed to quantify light loss from a diffuser or series of diffusers.

Gabriel Devereux
DIT | Australia/UK
gabjol@me.com
infinityvision.tv

Here’s a breakdown of the variables and the scenario:

You’re using 9x Skypanel S60s, each emitting 2936 LUX (luminous flux) at a distance of 2 meters.
The first diffuser is positioned 50 cm below the lights with 1/4 grid cloth.
The second diffuser is located 1.5 meters below the first diffuser.
Your talent is 5 meters away from the original light source, meaning they are 3 meters away from the second diffuser.


It’s important to note that your grid cloth has little light loss—meaning there’s a very small absorption coefficient, relative permeability, or permittivity—so it does not conduct radiation. Essentially, all light hitting the diffuser is reflected or dispersed in our context. The diffuser itself does not absorb a significant amount of energy as we deal with photographic stops.

When diffusing light, you're essentially re-scattering it from a specific point. You're taking a planar wave (directional light) and scattering it in all directions. In a simplified effect, each diffuser recreates many new light sources across its surface. Much like how light from a bulb propagates in all directions, and its energy falls off based on the expanding sphere’s surface area, this same principle applies when light propagates from a diffuser.

Now, onto how I calculated your setup:

A Skypanel S60 at 2 meters outputs 2936 LUX. Your first diffuser is 0.5 meters away from the light sources. At this distance, the S60s are outputting 45,288 LUX with a beam diameter of 1.3 meters.

If we assume the S60s are arranged in a 3m x 3m array with 1.5 meters of spacing between fixtures, the beams won’t overlap due to the proximity to the first diffuser. Therefore, the energy flux hitting the first diffuser remains at 45,288 LUX.

Input for diffuser 1:

LUX: 45,288 (flux from Skypanels hitting the first diffuser)
Diffuser size: 6m x 6m
Distance to the next diffuser: 1.5 meters
The output from the first diffuser is approximately 8300 LUX (average of 8865 and 7747 LUX).

Input for diffuser 2:

LUX: 8300 (flux density hitting the second diffuser)
Diffuser size: 6m x 6m (this diffuser is fully lit)
Distance to the talent: 2 meters
The output at the second diffuser, and ultimately the light reaching your talent, is approximately 1370 LUX.

I've attached the Python script (softcalc.py) to help automate these calculations. You can save it in your root folder or desktop and run it using the following commands:

In terminal: python [path to file]/softcalc.py
Alternatively, you can open terminal, type nano softcalc.py, paste the code, and run it directly with python softcalc.py. It will prompt you for the necessary inputs.
- Code to download

https://github.com/GabrielJDevereux/soft_light/blob/277450eb2c3ef219c393cd897f7b7a462544ffb2/reflectorcalc.py

 
