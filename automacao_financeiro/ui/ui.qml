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
            id: 'rectangle_email_label'
            color: '#000000ff'
            width: parent.width
            height: 50
            anchors.top: ractangle_date_text_field.bottom
            anchors.horizontalCenter: parent.horizontalCenter

            Label {
                id: 'email_label'
                text: 'E-mail para o Novo Saque'
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: parent.width * 0.05
            }
        }

        Rectangle {
            id: 'rectangle_email_text_field'
            color: '#000000ff'
            width: parent.width
            height: 50
            anchors.top: rectangle_email_label.bottom
            anchors.horizontalCenter: parent.horizontalCenter

            TextField {
                id: 'email_text_field'
                placeholderText: 'E-mail'
                width: parent.width * 0.90
                anchors.leftMargin: parent.width * 0.10
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }

        Rectangle {
            id: 'rectangle_start_button'
            color: '#000000ff'
            width: parent.width
            height: 50
            anchors.top: rectangle_email_text_field.bottom
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
                    onClicked: {
                        const initDate = init_date_text_field.text
                        const endDate = end_date_text_field.text

                        const banks = [
                            facta.checkState,
                            novo_saque.checkState,
                            capital_dois.checkState
                        ]

                        bridge.start(initDate, endDate, banks)
                    }
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
                id: 'facta'
                text: qsTr("Facta")
            }

            CheckBox {
                checked: false
                id: 'novo_saque'
                text: qsTr("Novo Saque")
                anchors.top: facta.bottom
            }
            
            CheckBox {
                checked: false
                id: 'capital_dois'
                text: qsTr("Capital2")
                anchors.top: novo_saque.bottom
            }
        }
    }
}