from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2200_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
    OP_69(0x101, 0x0)
    SetMapFlags(0x400000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrPos(0x101, 113000, 2000, 22300, 270)
    SetChrPos(0x102, 114500, 2000, 21500, 270)
    SetChrPos(0x105, 115000, 2000, 22600, 270)
    OP_51(0xA, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x0, 30)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    FadeToBright(2000, 0)

    def lambda_12F():
        OP_94(0x1, 0x101, 0x0, 0x15E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12F)
    Sleep(200)

    def lambda_14A():
        OP_94(0x1, 0x102, 0x0, 0x1770, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14A)
    Sleep(200)

    def lambda_165():
        OP_94(0x1, 0x105, 0x0, 0x1900, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_165)

    def lambda_17B():
        OP_69(0xA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_17B)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    def lambda_18F():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18F)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    Sleep(1000)

    ChrTalk(    #0
        0x101,
        (
            "#007F*sigh*\x02\x03",

            "Well, that's taken care of,\x01",
            "but I wouldn't exactly call it\x01",
            "'settled.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x105,
        "#043FSo it would seem, yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#013F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(    #3
        0x101,
        (
            "#002FHey, c'mon, Joshua.\x02\x03",

            "I know you've got something on\x01",
            "your mind.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #4
        0x102,
        (
            "#010FHuh...? Oh. Yeah, a little.\x02\x03",

            "I was just wondering why the thief\x01",
            "would take the candelabrum if he\x01",
            "MEANT for it to be found...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#004FGood question.\x02\x03",

            "But it looks like we may\x01",
            "never know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(    #6
        0x105,
        (
            "#042FThe newest card is what really\x01",
            "gets me...\x02\x03",

            "It's as if this were designed as\x01",
            "a test specifically for you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#003FYeah...that's been bugging me, too.\x02\x03",

            "#002FWe need to keep up our investigation.\x02\x03",

            "For starters, we still don't know\x01",
            "where the crook sneaked in from.\x02\x03",

            "Why don't we do some sneaking\x01",
            "around of our own, and check\x01",
            "out the estate?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #8
        0x102,
        (
            "#018FWon't that make us just as bad\x01",
            "as the crook we're chasing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#009FWell, then what are we supposed\x01",
            "to do?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#017FWhat choice do we have? We're\x01",
            "supposed to abide by the client's\x01",
            "wishes.\x02\x03",

            "#010FFor now, we have to be patient.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #11
        0x101,
        "#505FGrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#010FAll right, let's go.\x02\x03",

            "Like the mayor said, there's a\x01",
            "lot that still has to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#505F...Oh, all right.\x02\x03",

            "#006FGuess it's back to the drawing board.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #14
        0x105,
        (
            "#041FThat seems to be all that we\x01",
            "can do for the moment.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00Quest \x07\x02[Candelabrum Theft] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
