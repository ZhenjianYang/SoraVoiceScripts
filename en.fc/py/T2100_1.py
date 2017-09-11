from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2100.x',
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

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_51(0x12, 0x1, (scpexpr(EXPR_PUSH_LONG, 0x32C8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_28(0x20, 0x1, 0x4)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8B(0x0, 0x34BC, 0x11EB8, 0x190)
    Fade(1000)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B")
    OP_51(0x1, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x1, 180, 0)
    OP_8C(0x2, 180, 0)
    Jump("loc_2B2")

    label("loc_13B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B9")
    OP_51(0x1, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x1, 180, 0)
    OP_8C(0x2, 180, 0)
    Jump("loc_2B2")

    label("loc_1B9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_237")
    OP_51(0x1, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x1, 0, 0)
    OP_8C(0x2, 0, 0)
    Jump("loc_2B2")

    label("loc_237")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11EB8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B2")
    OP_51(0x1, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x1, 0, 0)
    OP_8C(0x2, 0, 0)

    label("loc_2B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EB")

    def lambda_2CD():
        OP_6D(13500, 1500, 73400, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2CD)
    OP_6C(135000, 3000)
    Jump("loc_3CC")

    label("loc_2EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_324")

    def lambda_306():
        OP_6D(13500, 1500, 73400, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_306)
    OP_6C(45000, 3000)
    Jump("loc_3CC")

    label("loc_324")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35D")

    def lambda_33F():
        OP_6D(13500, 1500, 73400, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_33F)
    OP_6C(45000, 3000)
    Jump("loc_3CC")

    label("loc_35D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_396")

    def lambda_378():
        OP_6D(13500, 1500, 73400, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_378)
    OP_6C(45000, 3000)
    Jump("loc_3CC")

    label("loc_396")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CC")

    def lambda_3B1():
        OP_6D(13500, 1500, 73400, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3B1)
    OP_6C(135000, 3000)

    label("loc_3CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A")

    ChrTalk(    #0
        0x101,
        "#002F...Hmm?\x02",
    )

    CloseMessageWindow()

    def lambda_3F0():
        TurnDirection(0x102, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F0)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #1
        0x102,
        "#014FWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#002FH-Hey...that's a card, isn't it?\x02",
    )

    CloseMessageWindow()

    def lambda_448():
        TurnDirection(0x102, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_448)
    TurnDirection(0x105, 0x12, 400)
    Jump("loc_609")

    label("loc_45A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54B")

    ChrTalk(    #3
        0x102,
        "#014FHmm?\x02",
    )

    CloseMessageWindow()

    def lambda_47B():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47B)
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(    #4
        0x101,
        "#501FWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        "#014F...It's a card.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #6
        0x101,
        (
            "#004F...What?!\x02\x03",

            "Wh-Where?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        "#012FOn top of that plate.\x02",
    )

    CloseMessageWindow()

    def lambda_51D():
        TurnDirection(0x101, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51D)
    TurnDirection(0x105, 0x12, 400)

    ChrTalk(    #8
        0x101,
        "#004FOh, you're right!\x02",
    )

    CloseMessageWindow()
    Jump("loc_609")

    label("loc_54B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_609")

    ChrTalk(    #9
        0x105,
        "#044FOh...\x02",
    )

    CloseMessageWindow()

    def lambda_56D():
        TurnDirection(0x102, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_56D)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #10
        0x101,
        "#501FWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x105,
        "#044FThere's a card there...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_5D3():
        TurnDirection(0x101, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D3)
    TurnDirection(0x102, 0x12, 400)

    ChrTalk(    #12
        0x101,
        (
            "#004FWhat...?!\x02\x03",

            "Oh, you're right!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_609")


    ChrTalk(    #13
        0x102,
        "#012FLet's have a look.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x102, 0x40)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_686")

    def lambda_63D():
        OP_92(0x1, 0x12, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_63D)

    def lambda_652():
        OP_92(0x2, 0x12, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_652)
    OP_8E(0x102, 0x3138, 0x0, 0x11EB8, 0x7D0, 0x0)
    TurnDirection(0x1, 0x12, 0)
    TurnDirection(0x2, 0x12, 0)
    Jump("loc_773")

    label("loc_686")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FB")

    def lambda_698():
        OP_91(0x0, 0xFFFFFCE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_698)
    OP_91(0x102, 0x258, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_6C7():
        OP_92(0x2, 0x12, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_6C7)
    OP_8E(0x102, 0x3138, 0x0, 0x11EB8, 0x7D0, 0x0)
    TurnDirection(0x0, 0x12, 0)
    TurnDirection(0x2, 0x12, 0)
    Jump("loc_773")

    label("loc_6FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_773")

    def lambda_70D():
        OP_91(0x0, 0xFFFFFCE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_70D)

    def lambda_728():
        OP_91(0x1, 0xFFFFFF38, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_728)
    OP_91(0x102, 0x2BC, 0x0, 0x0, 0x7D0, 0x0)
    TurnDirection(0x0, 0x12, 0)
    TurnDirection(0x1, 0x12, 0)
    OP_8E(0x102, 0x3138, 0x0, 0x11EB8, 0x7D0, 0x0)

    label("loc_773")

    ClearChrFlags(0x102, 0x40)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_7BD():
        OP_69(0x12, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7BD)
    OP_8C(0x102, 90, 400)
    Sleep(1000)

    ChrTalk(    #14
        0x102,
        (
            "#012F...This is definitely it.\x02\x03",

            "It's the same card that we saw\x01",
            "in the mayor's estate.\x02\x03",

            "I see... So this is what the card\x01",
            "meant by 'three-eyed.'\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    Fade(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A1")
    OP_67(0, 4875, -10000, 0)
    OP_6D(21130, 1900, 79750, 3000)
    Jump("loc_8C3")

    label("loc_8A1")

    OP_67(0, 4875, -10000, 0)
    OP_6D(21130, 1900, 66830, 3000)

    label("loc_8C3")

    OP_0D()

    ChrTalk(    #15
        0x101,
        (
            "#501FAh, I see. This might be the\x01",
            "'three-eyed' part of the clue.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    Fade(1000)
    OP_69(0x12, 0x0)
    OP_67(0, 9500, -10000, 0)
    OP_0D()
    Sleep(800)

    ChrTalk(    #16
        0x101,
        "#002FSo...is anything written on it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #17
        0x102,
        "#010FLet's see...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #18
        (
            "\x07\x00'Ah, seeker. The eyes of Aidios see only the truth,\x01",
            "and pass it on to you. Look to the endless waltz\x01",
            "which unfolds between the red and black. Do so,\x01",
            "and the blue light will be revealed.\x01\x01",
            "-Phantom Thief B'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrTalk(    #19
        0x101,
        (
            "#006FLooks like the next spot's\x01",
            "been picked.\x02\x03",

            "'Look to the endless waltz which unfolds\x01",
            "between the red and black'...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #20
        0x105,
        (
            "#040FRed and black...\x02\x03",

            "That has to mean something\x01",
            "in Ruan, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B5F():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5F)
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(    #21
        0x102,
        (
            "#010FProbably, yeah.\x02\x03",

            "I guess the criminal sure must\x01",
            "love his puzzles...\x02\x03",

            "He won't break his own rules.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BE1():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BE1)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #22
        0x101,
        (
            "#009FWhat a total jackass.\x02\x03",

            "#006FOh, well. Let's start searching.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x0, 0x1)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
