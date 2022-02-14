import QtQuick 2.14
import QtQuick.Controls 2.14


Column {
    TextInput {
        id: clickInput
        // Bind the clickModel.count property to the text property of the QML element
        text: clickModel.count
    }
    Binding {
        target: clickModel
        property: "count"
        value: clickInput.text
    }
    Button {
        text: 'Click me!'
        // Connect the clickModel.increase slot to the onClicked signal
        onClicked: clickModel.increase()
    }
    Button {
        text: 'Reset'
        // Connect the clickModel.increase slot to the onClicked signal
        onClicked: clickModel.reset()
    }
    Button {
        text: 'Reset_2'
        // Connect the clickModel.increase slot to the onClicked signal
        onClicked: clickModel.count = 0
    }
}
