/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    public int getImportance(List<Employee> employees, int id) {
        Stack<Employee> stack = new Stack<>();
        Employee firstEmployee = findEmployee(employees, id);
        int totalTeamImportance = firstEmployee.importance;

        stack.push(firstEmployee);

        while(!stack.isEmpty()){
            Employee subordinate = stack.pop();

            for (int ids: subordinate.subordinates){
                Employee nextEmployee = findEmployee(employees, ids);
                totalTeamImportance += nextEmployee.importance;
                stack.push(nextEmployee);
            }
        }
        return totalTeamImportance;
    }
    public Employee findEmployee(List<Employee>employees, int id){
        for(Employee employee: employees){
            if (employee.id == id) return employee;
        }
        return new Employee();
    }
}
