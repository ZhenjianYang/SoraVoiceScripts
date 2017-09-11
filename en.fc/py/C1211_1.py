from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1211_1 ._SN',
        MapName             = 'Bose',
        Location            = 'C1211.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    OP_6D(-10, 0, -7120, 0)
    SetChrPos(0x101, 280, 0, -20580, 0)
    SetChrPos(0x102, 1080, 0, -21780, 0)
    SetChrPos(0x103, -780, 0, -21880, 0)

    def lambda_B7():
        OP_90(0x101, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B7)
    Sleep(100)

    def lambda_D7():
        OP_90(0x102, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D7)
    Sleep(100)

    def lambda_F7():
        OP_90(0x103, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F7)
    FadeToBright(1000, 0)
    OP_6D(480, 0, -17620, 3500)
    OP_0D()
    WaitChrThread(0x103, 0x1)
    Sleep(400)

    ChrTalk(    #0
        0x101,
        (
            "#000FHmm...so what was the name of\x01",
            "this tower, again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#010FThe Amberl Tower.\x02\x03",

            "It's one of the ancient ruins referred\x01",
            "to as a 'Tetracyclic Tower'.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #2
        0x101,
        (
            "#000FOh, I see. That's why it looks exactly\x01",
            "like the Esmelas Tower, huh?\x02\x03",

            "I mean, aside from the color and the\x01",
            "layout, of course. But the atmosphere\x01",
            "is the same...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 0, 400)
    Sleep(400)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #3
        0x102,
        "#014FWhat's wrong...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#505FOh, uh...it's probably nothing...but\x01",
            "I could have sworn I heard somebody\x01",
            "talking...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 19240, 0, 33890, 42)
    SetChrPos(0x9, 10000, 0, 25000, 45)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_8C(0x102, 0, 0)
    OP_6D(170, 0, -8790, 3000)

    ChrTalk(    #5
        0x8,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        "..., ...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #7
        0x9,
        "...?! ...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    Fade(1000)
    OP_6D(480, 0, -17620, 0)
    OP_8C(0x102, 0, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #8
        0x102,
        (
            "#012FYou're right, Estelle. It sounds\x01",
            "like somebody's in here...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #9
        0x101,
        "#002FUmm... Do you think it could be...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #10
        0x103,
        (
            "#027FHmm...\x01",
            "Maybe taking a detour every once\x01",
            "in a while isn't a bad idea.\x02\x03",

            "We may have just netted ourselves\x01",
            "something big.\x02\x03",

            "It looks like we'll need to investigate,\x01",
            "so let's be cautious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#002FRight.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_28(0xF, 0x4, 0x2)
    OP_28(0xF, 0x4, 0x4)
    OP_28(0xF, 0x1, 0x1)
    OP_28(0xF, 0x1, 0x2)
    OP_28(0xF, 0x1, 0x8000)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
