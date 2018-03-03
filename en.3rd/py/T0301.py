from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0301   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0301.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60084",
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
        'Joshua',                               # 9
        'Cassius',                              # 10
        'Plate',                                # 11
        'Target Camera',                        # 12
        'Elize Highway',                        # 13
    )

    DeclEntryPoint(
        Unknown_00              = 2000,
        Unknown_04              = 0,
        Unknown_08              = -6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02750 ._CH',             # 00
        'ED6_DT06/CH20011 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02750P._CP',             # 00
        'ED6_DT06/CH20011P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262146,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4110,
        Z                   = -1000,
        Y                   = -46140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_22E",          # 00, 0
        "Function_1_26C",          # 01, 1
        "Function_2_270",          # 02, 2
        "Function_3_31E",          # 03, 3
    )


    def Function_0_22E(): pass

    label("Function_0_22E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_259")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)
    Jump("loc_26B")

    label("loc_259")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_26B")

    Return()

    # Function_0_22E end

    def Function_1_26C(): pass

    label("Function_1_26C")

    OP_82(0x80, 0x2)
    Return()

    # Function_1_26C end

    def Function_2_270(): pass

    label("Function_2_270")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -4360, 0, -2200, 0)
    OP_6D(-500, -1000, -18840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3490, 0)
    OP_6C(311000, 0)
    OP_6E(328, 0)

    def lambda_2D0():
        OP_6D(-920, 1000, 740, 10000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2D0)

    def lambda_2E8():
        OP_6C(317000, 10000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2E8)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x13, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_270 end

    def Function_3_31E(): pass

    label("Function_3_31E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -4360, 0, -2200, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2100, 450, -1510, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 9600, 620, -2310, 90)
    SetChrPos(0x12, 10000, 1100, -3300, 0)
    ClearChrFlags(0x12, 0x80)
    OP_6D(2000, 450, -640, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    def lambda_3C5():
        OP_6D(2000, 0, -2280, 6000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_3C5)

    def lambda_3DD():
        OP_67(0, 6500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3DD)

    def lambda_3F5():
        OP_6B(2860, 6000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3F5)
    FadeToBright(4000, 0)
    OP_0D()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1D)
    OP_73(0x0)

    def lambda_42C():
        OP_8F(0xFE, 0x7D0, 0x1C2, 0xFFFFEF02, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_42C)
    WaitChrThread(0x10, 0x1)
    OP_6F(0x0, 29)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #0
        0x11,
        "Man's Voice",
        "...Joshua.\x02",
    )

    CloseMessageWindow()

    def lambda_483():
        OP_6D(4480, 0, -2420, 3500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_483)

    def lambda_49B():
        OP_6C(299000, 3500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_49B)
    WaitChrThread(0x13, 0x0)
    Sleep(500)

    ChrTalk(    #1
        0x11,
        "#085F#5PDetermined to sleep outside again, hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        "#1676F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        (
            "#080F#5PNot a fan of sleeping in the same room as \x01",
            "Estelle, I take it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_545():
        OP_6D(7130, 450, -2330, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_545)

    def lambda_55D():
        OP_6C(298000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_55D)

    def lambda_56D():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_56D)

    def lambda_57D():
        OP_67(0, 5220, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_57D)
    OP_8E(0x10, 0x19C8, 0x1C2, 0xFFFFF1A0, 0x5DC, 0x0)
    WaitChrThread(0x13, 0x0)
    Sleep(500)

    ChrTalk(    #4
        0x10,
        (
            "#1671F#5P...She's way too much of a meddler.\x02\x03",

            "She's also completely clueless.\x02\x03",

            "#1675FShe's got no idea how much danger\x01",
            "she's willingly exposing herself to...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #5
        0x10,
        (
            "#1670F#5PWhy don't you tell her, Cassius Bright?\x01",
            "She has a right to know. \x02\x03",

            "Why do you stand by and say nothing?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #6
        0x11,
        (
            "#085F#6P...The room next to Estelle's has been used\x01",
            "as a storage room for a while now, but it could\x01",
            "still be converted into a bedroom if need be.\x02\x03",

            "#080FIt might actually be perfect for you.\x02\x03",

            "Haven't been in there in a while, but I think\x01",
            "there might even already be a bed in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "#1676F#5PI'm fine as I am.\x02\x03",

            "#1676FI don't need a room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#085F#6PHmm...\x02\x03",

            "I'll give you that Estelle loves to poke\x01",
            "her nose into anything and everything\x01",
            "that catches her interest.\x02\x03",

            "And I can see how from your perspective,\x01",
            "that makes her look like a simpleminded,\x01",
            "clueless child.\x02\x03",

            "But that's where you're mistaken.\x02\x03",

            "#082FIt's not her who's clueless--it's you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        "#1678F#5P...!\x02",
    )

    Sleep(100)
    OP_7C(0x0, 0x64, 0xBB8, 0xC8)
    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        (
            "#080F#6PEstelle knows exactly what she wants out\x01",
            "of life and what she has to do to get it.\x02\x03",

            "Those things are part of what makes her\x01",
            "who she is.\x02\x03",

            "#083FAlthough, I can't deny that I was hoping\x01",
            "to raise her to be a little more of a...well,\x01",
            "ordinary girl than she's grown up to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "#1675F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#085F#6PStill, compare that to you, Joshua.\x02\x03",

            "You don't have a clue what you want anymore.\x01",
            "You don't know what you should be doing.\x02\x03",

            "#082FWhich of you is really in the right here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        "#1675F#5P#40WI...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "#085F#6PJust so we're clear, whatever you decide to do,\x01",
            "I have no intention of indulging you.\x02\x03",

            "I'm not going to tell you to leave...but I'm not\x01",
            "going to tell you to stay, either.\x02\x03",

            "#080FWhat you want to do, where you want to go,\x01",
            "who you want to become...\x02\x03",

            "Those are all things for you to decide, and you\x01",
            "alone.\x02\x03",

            "#085FNo one can make that decision for you, and no \x01",
            "one knows what kind of decision you will make.\x01",
            "Only you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#1675F#5P#40W...\x02\x03",

            "#40WI...\x02\x03",

            "#60W(Just what do I want...?)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D8A():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_D8A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/R0201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_31E end

    SaveToFile()

Try(main)
