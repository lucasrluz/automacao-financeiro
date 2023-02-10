import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick

ApplicationWindow {
    visible: true
    width: 500
    height: 700
    font.pixelSize: 16
    Material.theme: Material.Dark

    Rectangle {
        color: '#000000ff'
        width: parent.width - 20
        height: parent.height - 20
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter

        Rectangle {
            id: 'ractangle_date_label'
            color: '#000000ff'
            width: parent.width
            height: 50
            anchors.horizontalCenter: parent.horizontalCenter

            Rectangle {
                color: '#000000ff'
                id: 'ractangle_init_date_label'
                width: parent.width * 0.50
                height: 50

                Label {
                    id: 'init_date_label'
                    text: 'Data Inicial'
                    anchors.left: parent.left
                    width: parent.width * 0.80
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.leftMargin: parent.width * 0.10
                }
            }
            
            Rectangle {
                color: '#000000ff'
                width: parent.width * 0.50
                height: 50
                anchors.right: parent.right
                Label {
                    id: 'end_date_label'
                    text: 'Data Final'
                    width: parent.width * 0.80
                    anchors.right: parent.right
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.rightMargin: parent.width * 0.10
                }
            }
        }

        Rectangle {
            id: 'ractangle_date_text_field'
            color: '#000000ff'
            width: parent.width
            height: 50
            anchors.top: ractangle_date_label.bottom
            anchors.horizontalCenter: parent.horizontalCenter

            Rectangle {
                color: '#000000ff'
                width: parent.width * 0.50
                height: 50
                
                TextField {
                    id: 'init_date_text_field'
                    placeholderText: 'dd/mm/yyyy'
                    width: parent.width * 0.80
                    anchors.leftMargin: parent.width * 0.10
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }

            Rectangle {
                color: '#000000ff'
                width: parent.width * 0.50
                height: 50
                anchors.right: parent.right

                TextField {
                    id: 'end_date_text_field'
                    placeholderText: 'dd/mm/yyyy'
                    width: parent.width * 0.80
                    anchors.leftMargin: parent.width * 0.10
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }
        }

        Rectangle {
            id: 'rectangle_start_button'
            color: '#000000ff'
            width: parent.width
            height: 50
            anchors.top: ractangle_date_text_field.bottom
            anchors.horizontalCenter: parent.horizontalCenter

            Rectangle {
                color: '#000000ff'
                width: parent.width
                height: 50
                Button {
                    id: 'submit_button'
                    text: 'Solicitar'
                    width: parent.width
                    height: 50
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }
        }

        Rectangle {
            color: '#000000ff'
            width: parent.width * 0.50
            height: 100
            anchors.top: rectangle_start_button.bottom
            anchors.left: parent.left

            CheckBox {
                checked: true
                id: 'a'
                text: qsTr("Banco A")
            }

            CheckBox {
                checked: true
                id: 'b'
                text: qsTr("Banco B")
                anchors.top: a.bottom
            }

            CheckBox {
                checked: true
                id: 'c'
                text: qsTr("Banco C")
                anchors.top: b.bottom
            }

            CheckBox {
                checked: true
                id: 'd'
                text: qsTr("Banco D")
                anchors.top: c.bottom
            }
        }

        Rectangle {
            color: '#000000ff'
            width: parent.width * 0.50
            height: 100
            anchors.top: rectangle_start_button.bottom
            anchors.right: parent.right

            CheckBox {
                checked: true
                id: 'e'
                text: qsTr("Banco E")
            }

            CheckBox {
                checked: true
                id: 'f'
                text: qsTr("Banco F")
                anchors.top: e.bottom
            }

            CheckBox {
                checked: true
                id: 'g'
                text: qsTr("Banco G")
                anchors.top: f.bottom
            }

            CheckBox {
                checked: true
                id: 'h'
                text: qsTr("Banco H")
                anchors.top: g.bottom
            }
        }
    }
}