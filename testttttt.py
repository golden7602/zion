def a(role_id: int):
        sql = '''
        SELECT CONCAT(fPreFix,
                if(fHasDateTime,
                DATE_FORMAT(CURRENT_DATE(),
                replace(replace(replace(replace(fDateFormat,
                \'yyyy\',\'%Y\'),\'yy\',\'%y\'),\'mm\',\'%m\'),\'dd\',\'%d\')),\'\'),
                LPAD(fCurrentValue+1, fLenght , 0)) into @PK
        FROM systabelautokeyroles
        WHERE fRoleID={r_id};\nUPDATE systabelautokeyroles 
                SET fCurrentValue=fCurrentValue+1, fLastKey=@PK
        WHERE fRoleID={r_id};'''.format(r_id=role_id)
        return sql

print(a(1))