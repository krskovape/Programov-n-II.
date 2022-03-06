import QtQuick 2.14
import QtQuick.Controls 2.14

Rectangle {
	width: 500
	height: 500

	Row {
		anchors.fill: parent
		Component {
			id: rowComponent
			Item {
				height: childrenRect.height
				width: parent.width
				Text {
					text: display
				}
				MouseArea {
					anchors.fill: parent
					onClicked: numberListView.currentIndex = index
				}
			}
		}

		ListView {
			id: numberListView
			width: 200
			height: parent.height

			model:numberListModel
			delegate: rowComponent

			highlight: Rectangle{
				color: "red"
			}

			onCurrentItemChanged: console.log("Item Changed"+numberListView.currentIndex) //vypíše věci do konzole (console.log)
		}

		Column {
			width: 100
			height: parent.height

			Row {
				spacing: 4
				Label {
					text: "Index"
				}
				TextInput {
					id: idxInput
					text: numberListModel.input_idx
					Binding {
						target: numberListModel
						property: "input_idx"
						value: idxInput.text
					}
				}
			}

			Row {
				spacing: 4
				Label {
					text: "Hodnota"
				}
				TextInput {
					id: numInput
					text: numberListModel.input_num
					Binding {
						target: numberListModel
						property: "input_num"
						value: numInput.text
					}
				}
			}
		}

		Column {
			width: 200
			height: parent.height

			Button {
				text: "Přidej prvek"
				onClicked: numberListModel.add_num()
			}
			Button {
				text: "Odeber prvek"
				onClicked: numberListModel.remove_num(numberListView.currentIndex)
			}
			Button {
				text: "Odeber vše"
				onClicked: numberListModel.remove_all()
			}
		}
	}
}