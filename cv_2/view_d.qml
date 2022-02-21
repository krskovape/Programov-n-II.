import QtQuick 2.14
import QtQuick.Controls 2.14

Column {
    Row {
        spacing: 4
        Row {
            TextInput {
                id: degInput
                text: dmsModel.deg
                Binding {
                    target: dmsModel
                    property: "deg"
                    value: degInput.text
                }
            }
            Label {
                text: "°"
            }
        }

        Row {
            TextInput {
                id: minInput
                text: dmsModel.min
                Binding {
                    target: dmsModel
                    property: "min"
                    value: minInput.text
                }
            }
            Label {
                text: "'"
            }
        }

        Row {
            TextInput {
                id: secInput
                text: dmsModel.sec
                Binding {
                    target: dmsModel
                    property: "sec"
                    value: secInput.text
                }
            }
            Label {
                text: "''"
            }
        }

        Button {
            text: 'To DEG'
            onClicked: dmsModel.to_deg()
        }
    }
    Row {
        spacing: 4
        Row {
            TextInput {
                id: deg_floatInput
                text: dmsModel.deg_float
                Binding {
                    target: dmsModel
                    property: "deg_float"
                    value: deg_floatInput.text
                }
            }
            Label {
                text: "°"
            }
        }
        
        Button {
            text: 'To DMS'
            onClicked: dmsModel.to_dms()
        }
    }
}


