unit uMain;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdActns, ActnList, ImgList, Menus, ComCtrls, SynEdit, ToolWin;

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
    procedure FormCreate(Sender: TObject);
    procedure SynEdit1GutterPaint(Sender: TObject; aLine, X, Y: Integer);
    procedure SynEdit1MouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
  private
    { Private declarations }
    Margin:integer;
  public
    { Public declarations }
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
    s := Copy(lines[aLine-1],5,10);
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
begin
  with TSynEdit(Sender), Canvas do
  begin
    if x < Gutter.LeftOffset then exit;
    
    lcord := PixelsToRowColumn(x + Gutter.Width + 10, y);
    s := Lines[lcord.Row-1];
    if copy(s, 1, 2) = '0b' then
    begin
      s [7] := '$';
      Lines[lcord.Row-1] := s;
      invalidategutterLine(lcord.Row);
    end;
  end;

end;

end.
