unit uMain;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdActns, ActnList, ImgList, Menus, ComCtrls, SynEdit, ToolWin,
  SynEditHighlighter, SynHighlighterPython;

type
  TForm1 = class(TForm)
    SynEdit1: TSynEdit;
    StatusBar1: TStatusBar;
    MainMenu1: TMainMenu;
    File1: TMenuItem;
    ActionList1: TActionList;
    ImageList1: TImageList;
    FileOpen1: TFileOpen;
    FileSaveAs1: TFileSaveAs;
    FileExit1: TFileExit;
    Open1: TMenuItem;
    SaveAs1: TMenuItem;
    N1: TMenuItem;
    Exit1: TMenuItem;
    CoolBar1: TCoolBar;
    ToolBar1: TToolBar;
    ToolButton1: TToolButton;
    ToolButton2: TToolButton;
    FileSave1: TAction;
    Save1: TMenuItem;
    SynPythonSyn1: TSynPythonSyn;
    procedure FormCreate(Sender: TObject);
    procedure SynEdit1GutterPaint(Sender: TObject; aLine, X, Y: Integer);
    procedure SynEdit1MouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
    procedure SynEdit1MouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure SynEdit1MouseUp(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
    procedure FileOpen1Accept(Sender: TObject);
    procedure FileSave1Execute(Sender: TObject);
    procedure FileSave1Update(Sender: TObject);
  private
    { Private declarations }
    Margin:integer;
    Painting: boolean;
    FPen : integer; // mousedown.left = 1; .right = 0;
    FFileName : string;
    start0b : integer;
  public
    { Public declarations }
    procedure LoadFromFile(AFileName: string);
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
begin
  Margin :=16;
  SynEdit1.Align:=alClient;
//  SynEdit1.Gutter.Width := SynEdit1.LineHeight * (4 + 6);
  SynEdit1.Gutter.Font.Assign(SynEdit1.Font);
  //SynEdit1.ResetModificationIndicator;
  start0b := 7;
  LoadFromFile('..\..\python\arabicArduino\arabic_letters.py');
end;

procedure TForm1.SynEdit1GutterPaint(Sender: TObject; aLine, X,
  Y: Integer);
var s : string;
  LineNumberRect: TRect;
  GutterWidth, Offset: Integer;
  OldFont: TFont;
  i,j:integer;
begin
  with TSynEdit(Sender), Canvas do
  begin
    s := Copy(lines[aLine-1],start0b,10);
    if copy(s, 1, 2) = '0b' then
    begin
      delete(s,1,2);
      i := 1;
      while s[i] in ['1','0'] do
      begin
         if s[i] = '1' then
            Brush.Color := clWindowText
         else
            Brush.Color := clWindow;
         Canvas.Rectangle(Margin + (i-1) * LineHeight, y, Margin + i * LineHeight, y + LineHeight);
         inc(i);
      end;
      {OldFont := TFont.Create;
      try
        OldFont.Assign(Canvas.Font);
        //Canvas.Font := Gutter.Font;
      GutterWidth := Gutter.Width - 5;
      LineNumberRect := Rect(x, y, GutterWidth, y + LineHeight);
      Canvas.TextRect(LineNumberRect, 10,0, s);
      Canvas.TextOut(x,y, s);

      Canvas.Font := OldFont;
      finally
        OldFont.Free;
      end;}
    end;
  end;
end;

procedure TForm1.SynEdit1MouseDown(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
var lcord : TDisplayCoord;
  s : string;
  i : integer;
begin
  with TSynEdit(Sender), Canvas do
  begin
    if (X<Margin) or (X > Gutter.LeftOffset) or (Button = mbMiddle) then
      exit;

    Painting := true;
    if BUtton = mbLeft then
      FPen := 1
    else
      FPen :=0;

    {lcord := PixelsToRowColumn(x + Gutter.Width + 10, y);
    s := Lines[lcord.Row-1];
    if copy(s, 1, 2) = '0b' then
    begin
      s [7] := '$';
      Lines[lcord.Row-1] := s;
      invalidategutterLine(lcord.Row);
    end;}
  end;
  SynEdit1MouseMove(Sender, Shift, X, Y);

end;

procedure TForm1.SynEdit1MouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
var lcord : TDisplayCoord;
  s : string;
  i,n : integer;
  c : char;
begin
  if not Painting then exit;

  if FPen = 0 then
    c := '0'
  else
    c := '1';

  with TSynEdit(Sender), Canvas do
  begin
    n := (x - Margin+1) div (LineHeight);
    lcord := PixelsToRowColumn(x + Gutter.Width + 10, y);
    s := Lines[lcord.Row-1];
    if (length(s) >= start0b+2+n) and (copy(s, start0b, 2) = '0b') and (s[start0b+n+2] in ['0','1'] ) then
    begin
      s [start0b+2+n] := c;
      Lines[lcord.Row-1] := s;
      invalidategutterLine(lcord.Row);
    end;
  end;

end;

procedure TForm1.SynEdit1MouseUp(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
begin
  if Painting then Painting := False;
end;

procedure TForm1.FileOpen1Accept(Sender: TObject);
var i : integer;
begin
 LoadFromFile( TFileOpen(Sender).Dialog.FileName);
end;

procedure TForm1.FileSave1Execute(Sender: TObject);
begin
  if FFileName = EmptyStr then
    FileSaveAs1.Execute
  else
  begin
    SynEdit1.Lines.SaveToFile(FFileName);
    SynEdit1.Modified := false;
  end;
end;

procedure TForm1.LoadFromFile(AFileName: string);
begin
  FFileName := AFileName;
  SynEdit1.Lines.LoadFromFile( FFileName );
  SynEdit1.ResetModificationIndicator;
end;

procedure TForm1.FileSave1Update(Sender: TObject);
begin
  FileSave1.Enabled := SynEdit1.Modified;
end;

end.
