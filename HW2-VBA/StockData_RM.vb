Sub StocksData ():

Dim TickerName As String
Dim Volume As Double
Dim i As Integer
Dim j As Long
Dim k As Long
Dim Change1 As Double
Dim DateMin As Double
Dim Change2 As Double

'Applies to all worksheets and speeds up program by disabling screen update

Application.ScreenUpdating = False
For Each sh In Worksheets
    sh.Activate
Cells(1, 9).Value = "Ticker"
Cells(1, 10).Value = "Yearly Change"
Cells(1, 11).Value = "Percent Change"
Cells(1, 12).Value = "Total Volume"
i = 2
k = 2
j = 2

Do While Cells(j, 1) <> ""
    TickerName = Cells(j, 1).Value
    
'Total Volume
    Volume = 0
        Do While Cells(j, 1).Value = TickerName
            Volume = Volume + Cells(j, 7).Value
            j = j + 1
        Loop
    Cells(i, 9).Value = TickerName
    Cells(i, 12).Value = Volume
    
'Yearly Change and Percent Change
    DateMin = Cells(k, 2)
    Change1 = 0
    Change2 = 0
        Do While Cells(k, 1) = TickerName
            If Cells(k, 2) <= DateMin Then
                Change1 = Cells(k, 3)
            ElseIf Cells(k, 2) > DateMin Then
                Change2 = Cells(k, 6)
            End If
            k = k + 1
        Loop
    Cells(i, 10) = Change2 - Change1
    If Change1 = 0 Then
        Cells(i, 11) = ""
    Else
        Cells(i, 11) = (Change2 / Change1) - 1
    End If
    
'Color
        If Cells(i, 10) <= 0 Then
            Cells(i, 10).Interior.ColorIndex = 3
        Else
            Cells(i, 10).Interior.ColorIndex = 4
        End If
    i = i + 1
Loop

'Max and Min values
Dim m As Integer
Dim Current As Double
Dim Max As Double
Dim Ticker1 As String
Dim Min As Double
Dim Ticker2 As String
Dim MaxVol As Double
Dim Ticker3 As String


m = 2
Max = Cells(m, 11).Value
Min = Cells(m, 11).Value
MaxVol = Cells(m, 11).Value

Do While Cells(m, 11) <> ""
        If Cells(m, 11).Value > Max Then
            Max = Cells(m, 11).Value
            Ticker1 = Cells(m, 9).Value
        ElseIf Cells(m, 11).Value < Min Then
            Min = Cells(m, 11).Value
            Ticker2 = Cells(m, 9)
        End If
        If Cells(m, 12).Value > MaxVol Then
            MaxVol = Cells(m, 12).Value
            Ticker3 = Cells(m, 9).Value
        End If
    m = m + 1
Loop

Cells(2, 14).Value = "Greatest % Increase"
Cells(3, 14).Value = "Greatet % Decrease"
Cells(4, 14).Value = "Greatest Total Volume"
Cells(1, 15).Value = "Ticker"
Cells(1, 16).Value = "Value"

Cells(2, 16).Value = Max
Cells(2, 15).Value = Ticker1
Cells(3, 16).Value = Min
Cells(3, 15).Value = Ticker2
Cells(4, 16).Value = MaxVol
Cells(4, 15).Value = Ticker3

Range("K:K").NumberFormat = "0.00%"
Range("P2:P3").NumberFormat = "0.00%"
Columns("A:P").Select
Selection.EntireColumn.AutoFit
Cells(1, 1).Select

'Move to next sheet and update sheet
Next sh
Application.ScreenUpdating = True

End Sub

        
        





