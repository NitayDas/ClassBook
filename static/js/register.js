// JavaScript to toggle the display of Groups and Preferences based on the selected role

document.addEventListener('DOMContentLoaded', function () {
    const roleSelect = document.getElementById('role');
    const groupsContainer = document.getElementById('groups-container');
    const preferencesContainer = document.getElementById('preferences-container');
  
    // Function to update visibility of group and preference fields
    function updateFieldsBasedOnRole() {
      const selectedRole = roleSelect.value;
      
      if (selectedRole === 'student') {
        groupsContainer.style.display = 'block';
        preferencesContainer.style.display = 'block';
      } else {
        groupsContainer.style.display = 'none';
        preferencesContainer.style.display = 'none';
      }
    }
  
    // Initially run the function to set the default state
    updateFieldsBasedOnRole();
  
    // Add event listener to update fields when role is changed
    roleSelect.addEventListener('change', updateFieldsBasedOnRole);
  });
  