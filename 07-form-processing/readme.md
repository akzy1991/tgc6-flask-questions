# 7. Form Processing

In this execrise, you are going to create a reservation form that has controls such as radio buttons, check boxes and select dropdown.

Create the following route:

## /
Display a link to the route `/book`

## /book
Display the form in the template `book.template.html` The form is only half-completed, add in missing `name` and `value` attributes so that
the form would work. Make sure sure that you can only select one of the radio buttons for seating and one of the radio buttons for the timing.
When the form is submitted, send it to the route `/process_booking`

## /process_booking
Process the form and display the customer's name, selected seating, selected timing, the services requested and how the customer heard about
the resturant, in a table (one row for each entry, use a comma list for the services requested)