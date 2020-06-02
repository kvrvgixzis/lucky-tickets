```VBA
Sub LuckyTickets()
    Dim i As Long
    Dim j As Integer
    
    Dim tickets_sum As Long
    
    Dim row_index As Long
    Dim column_index As Integer
    
    Dim right_num As Integer
    Dim right_num_str As String
    Dim right_num_sum As Integer
    
    Dim left_num As Integer
    Dim left_num_str As String
    Dim left_num_sum As Integer

    tickets_sum = 1
    row_index = 1
    column_index = 1
    Cells(row_index, column_index).NumberFormat = "@"
    Cells(row_index, column_index).Value = "000000"
    
    For i = 1000 To 999999 Step 1
        left_num_sum = 0: right_num_sum = 0
        
        left_num = i \ 1000
        left_num_str = CStr(left_num)
        For j = 1 To Len(left_num_str)
            left_num_sum = left_num_sum + Int(Mid(left_num_str, j, 1))
        Next
        
        right_num = i Mod 1000
        right_num_str = CStr(right_num)
        For j = 1 To Len(right_num_str)
            right_num_sum = right_num_sum + Int(Mid(right_num_str, j, 1))
        Next
        
        If left_num_sum = right_num_sum Then
            If row_index Mod 1000 = 0 Then
                row_index = 0
                column_index = column_index + 1
            End If
            
            tickets_sum = tickets_sum + 1
            row_index = row_index + 1
            Cells(row_index, column_index).NumberFormat = "@"
            
            Select Case Len(CStr(i))
                Case 4: Cells(row_index, column_index).Value = "00" & CStr(i)
                Case 5: Cells(row_index, column_index).Value = "0" & CStr(i)
                Case 6: Cells(row_index, column_index).Value = CStr(i)
            End Select
        End If
    Next
    
    MsgBox (tickets_sum)
End Sub
```