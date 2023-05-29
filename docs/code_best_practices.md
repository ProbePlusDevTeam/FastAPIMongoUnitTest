No-SQL DB Code Pattern

### Updating embedded document

While embedding document in other document.
If the main source eg Patient record is updated,
then docs embedding this data needs to be updated.

o patient_record
o prescription ┘ 

For code review, implement this pattern.
update_patient_details() {
  //code to be executed for updating prescription document
  // with correct patient details.
}
