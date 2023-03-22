# Datahouse Coding Assignemnt

### Dependency:
pip install Flask

### Input and Output

<ul>
<li>Input: JSON file or raw JSON. (Output has been demostrated below of this file with CURL and POSTMAN)</li>
  <ul>
    <li>
      For CURL: curl -i -H "Content-Type: application/json" charset=utf-8 -X POST -d @applicants.json http://127.0.0.1:5000
    </li>
    </ul>
  <ul>
    <li>
    For POSTMAN: Set method to POST and URL as http://127.0.0.1:5000. Input type: raw and JSON
     </li>
</ul>
  <li>Output: JSON object</li>
</ul>

### Calculating Compatibility Score  
  <ul>
    <li> Assuming Maximum value as 10 and Minimum vaalue as 1 for each of the attributes: intelligence, strength, endurance, spicyFoodTolerance </li>
    <li>Calculating normalized value of the attributes using MIn-Max approach : (value - min_value) / (max_value - min_value))</li>
    <li>Averaging of the normalized value to get the compatibility score</li>
  </ul>


### Demonstration
https://user-images.githubusercontent.com/58367051/226894914-33889f44-c93b-4d2a-ad20-ba794fadfc63.mov



https://user-images.githubusercontent.com/58367051/226895143-a0d67d32-8dc5-431d-b824-4a0f2f83492d.mov

