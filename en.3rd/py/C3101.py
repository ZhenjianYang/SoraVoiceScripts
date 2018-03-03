from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Cassius',                              # 9
        'Captain Schwarz',                      # 10
        'Guard',                                # 11
        'Guard',                                # 12
        'Guard',                                # 13
        'Guard',                                # 14
        'Guard',                                # 15
        'Guard',                                # 16
        'Royal Army Officer',                   # 17
        'Guard',                                # 18
        'Guard',                                # 19
        'Guard',                                # 20
        'Guard',                                # 21
        'Guard',                                # 22
        'Richard',                              # 23
        'Target Camera',                        # 24
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT27/CH03580 ._CH',             # 02
        'ED6_DT27/CH04580 ._CH',             # 03
        'ED6_DT27/CH04581 ._CH',             # 04
        'ED6_DT27/CH04584 ._CH',             # 05
        'ED6_DT07/CH00420 ._CH',             # 06
        'ED6_DT07/CH00421 ._CH',             # 07
        'ED6_DT07/CH00424 ._CH',             # 08
        'ED6_DT07/CH01600 ._CH',             # 09
        'ED6_DT07/CH00322 ._CH',             # 0A
        'ED6_DT07/CH00326 ._CH',             # 0B
        'ED6_DT07/CH02030 ._CH',             # 0C
        'ED6_DT07/CH00270 ._CH',             # 0D
        'ED6_DT07/CH00271 ._CH',             # 0E
        'ED6_DT07/CH00274 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT27/CH03580P._CP',             # 02
        'ED6_DT27/CH04580P._CP',             # 03
        'ED6_DT27/CH04581P._CP',             # 04
        'ED6_DT27/CH04584P._CP',             # 05
        'ED6_DT07/CH00420P._CP',             # 06
        'ED6_DT07/CH00421P._CP',             # 07
        'ED6_DT07/CH00424P._CP',             # 08
        'ED6_DT07/CH01600P._CP',             # 09
        'ED6_DT07/CH00322P._CP',             # 0A
        'ED6_DT07/CH00326P._CP',             # 0B
        'ED6_DT07/CH02030P._CP',             # 0C
        'ED6_DT07/CH00270P._CP',             # 0D
        'ED6_DT07/CH00271P._CP',             # 0E
        'ED6_DT07/CH00274P._CP',             # 0F
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 580,
        Z                   = 0,
        Y                   = 35150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2560,
        Z                   = 0,
        Y                   = 35260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16590,
        Z                   = 0,
        Y                   = 29000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14750,
        Z                   = 0,
        Y                   = 29000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 12780,
        Z                   = 0,
        Y                   = 29000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 10840,
        Z                   = 0,
        Y                   = 29000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18730,
        Z                   = 0,
        Y                   = 27570,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16470,
        Z                   = 0,
        Y                   = 29800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13160,
        Z                   = 0,
        Y                   = 29250,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16250,
        Z                   = 0,
        Y                   = 27060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13260,
        Z                   = 0,
        Y                   = 26740,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -15120,
        Z                   = 0,
        Y                   = 31950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C1,
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


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_349",          # 01, 1
        "Function_2_353",          # 02, 2
        "Function_3_3DB",          # 03, 3
        "Function_4_45C",          # 04, 4
        "Function_5_4D8",          # 05, 5
        "Function_6_4ED",          # 06, 6
        "Function_7_1619",         # 07, 7
        "Function_8_301E",         # 08, 8
        "Function_9_3839",         # 09, 9
        "Function_10_3861",        # 0A, 10
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_348")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_348")

    Return()

    # Function_0_32A end

    def Function_1_349(): pass

    label("Function_1_349")

    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_349 end

    def Function_2_353(): pass

    label("Function_2_353")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386")
    Sleep(300)
    Jump("loc_3D7")

    label("loc_386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    Sleep(400)
    Jump("loc_3D7")

    label("loc_39B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B0")
    Sleep(500)
    Jump("loc_3D7")

    label("loc_3B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5")
    Sleep(700)
    Jump("loc_3D7")

    label("loc_3C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D7")
    Sleep(800)

    label("loc_3D7")

    Jump("Function_2_353")

    label("loc_3DA")

    Return()

    # Function_2_353 end

    def Function_3_3DB(): pass

    label("Function_3_3DB")

    LoadEffect(0x0, "battle\\\\btgun00.eff")

    label("loc_3F1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45B")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFE, 600, 900, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0x1F7)
    OP_22(0x1F7, 0x0, 0xA)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(800)
    Jump("loc_3F1")

    label("loc_45B")

    Return()

    # Function_3_3DB end

    def Function_4_45C(): pass

    label("Function_4_45C")

    LoadEffect(0x0, "battle\\\\btgun00.eff")

    label("loc_472")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D7")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFE, 600, 900, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0x1F7)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(800)
    Jump("loc_472")

    label("loc_4D7")

    Return()

    # Function_4_45C end

    def Function_5_4D8(): pass

    label("Function_5_4D8")

    OP_8E(0xFE, 0x4F10, 0x0, 0x7BAC, 0x7D0, 0x0)
    Return()

    # Function_5_4D8 end

    def Function_6_4ED(): pass

    label("Function_6_4ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x10A, -1040, 500, 37340, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrPos(0x10, -1040, 500, 37340, 180)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_6D(15970, 0, 31320, 0)
    OP_67(0, 6330, -10000, 0)
    OP_6B(4400, 0)
    OP_6C(315000, 0)
    OP_6E(300, 0)

    def lambda_59F():
        OP_6D(-3140, 0, 32590, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_59F)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10A, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-2820, 0, 36480, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(315000, 0)
    OP_6E(310, 0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_0D()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x9)
    OP_73(0x1)
    Sleep(300)

    def lambda_675():
        OP_6D(-2820, 0, 31860, 4000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_675)

    def lambda_68D():
        OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0x66BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_68D)
    Sleep(1500)

    def lambda_6AD():
        OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0x8110, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_6AD)
    WaitChrThread(0x10A, 0x0)
    Sleep(300)
    OP_62(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10A)
    Sleep(500)

    ChrTalk(    #0
        0x10A,
        (
            "#813F#11P(What's he planning to do out here?)\x02\x03",

            "(I really want to know who he called, too...)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #1
        0x10,
        (
            "#1120F#12PAh, there you are.\x02\x03",

            "Are you all ready to begin?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_7BA():
        OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0x6F54, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_7BA)
    ClearChrFlags(0x1E, 0x80)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1E, -8820, 0, 24400, 90)

    NpcTalk(    #2
        0x1E,
        "Man's Voice",
        "#2PIndeed, I am.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #3
        0x1E,
        "Man's Voice",
        (
            "#2PI never expected to have to wear this uniform\x01",
            "again, though. Especially not so soon.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x1E,
        "Man's Voice",
        "#2PI'd almost think you enjoyed messing with people.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "#1121F#12PHaha. I'm not doing it to bully you.\x02\x03",

            "#1120FYou know as well as I do your usual work clothes\x01",
            "aren't well suited for this kind of thing.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10A, 0x0)
    SetChrPos(0x1E, -10820, 0, 27400, 90)

    def lambda_974():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_974)
    OP_44(0x1F, 0x0)

    def lambda_98A():
        OP_6D(-12220, 0, 27400, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_98A)

    def lambda_9A2():
        OP_6C(270000, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_9A2)

    def lambda_9B2():
        OP_6B(2680, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_9B2)

    def lambda_9C2():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_9C2)
    WaitChrThread(0x1F, 0x0)
    Sleep(500)
    OP_6F(0x1, 0)

    ChrTalk(    #6
        0x10A,
        "#1317F#5P#3SY-You're Colonel Richard!#2S\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_59()

    def lambda_A21():
        OP_6D(-4059, 0, 27400, 3500)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_A21)

    def lambda_A39():
        OP_67(0, 4460, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_A39)

    def lambda_A51():
        OP_6B(2780, 3500)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_A51)

    def lambda_A61():
        OP_8E(0xFE, 0xFFFFF04D, 0x0, 0x6B08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_A61)
    Sleep(2500)

    def lambda_A81():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_A81)

    def lambda_A8F():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_A8F)
    WaitChrThread(0x1E, 0x0)
    Sleep(300)
    OP_8C(0x1E, 45, 400)
    Sleep(500)

    ChrTalk(    #7
        0x1E,
        (
            "#115F#5PI realize this may sound a little silly coming\x01",
            "from a man wearing this uniform...\x02\x03",

            "#110F...but I'm no longer a colonel, young lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        (
            "#1316F#12PS-Sorry...\x02\x03",

            "#818FSooo...Mr. Richard, then? Or Alan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x1E,
        (
            "#110F#5PYou can call me whatever you wish, though no\x01",
            "need for the 'Mr.' Meanwhile, I believe you are\x01",
            "Anelace, a senior bracer with the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10A,
        "#814F#12PYou know me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x1E,
        (
            "#119F#5PI'm not the former commander of the Intelligence\x01",
            "Division for nothing.\x02\x03",

            "#111FI know about all of the bracers in this country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10A,
        (
            "#819F#12PI-I see...\x02\x03",

            "#1317FBut how did you end up being here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#1120F#6PActually, Richard was who I was meeting just\x01",
            "before I spoke with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10A,
        "#814F#12PReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x1E,
        (
            "#119F#5PIn short, I've decided to start up a new research\x01",
            "company as a civilian.\x02\x03",

            "So while I may not be part of the army anymore,\x01",
            "I can definitely see myself continuing to need to\x01",
            "work with it in the future.\x02\x03",

            "#110FSo I decided to come here in order to discuss the\x01",
            "matter with Cassius in the hopes of maintaining a\x01",
            "good relationship between us in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10A,
        "#1310F#12POh, I get it now...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #17
        0x10A,
        (
            "#814F#12PW-Wait.\x02\x03",

            "Is the person you mentioned earlier...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 400)
    Sleep(300)

    ChrTalk(    #18
        0x10,
        (
            "#1125F#5PThat's right.\x02\x03",

            "#1120FI want the two of you to fight one another.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #19
        0x10A,
        (
            "#1317F#12PW-Wait a second! This is all a bit...sudden,\x01",
            "isn't it?\x02\x03",

            "#1316FEspecially if I'm going to be fighting the\x01",
            "famous Colonel Richard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#1122F#5PIs that so?\x02\x03",

            "...You don't want to know the answer to the\x01",
            "questions you asked me earlier, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10A,
        "#1317F#12P#3S...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#1125F#5PI believe any doubts you have toward swordsmanship\x01",
            "can only be dispelled through using it.\x02\x03",

            "#1120FFocus not on whether you win or lose, but on pouring\x01",
            "all you have into the battle, and you should find the\x01",
            "answers you seek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        "#813F#12P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10A)
    Sleep(500)

    ChrTalk(    #24
        0x10A,
        "#812F#12PAll right, then.\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)

    def lambda_123D():
        OP_96(0xFE, 0x794, 0x0, 0x6B08, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_123D)

    def lambda_125B():
        OP_6D(-2210, 0, 28870, 1000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_125B)

    def lambda_1273():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1273)

    def lambda_1283():
        OP_6B(2780, 1000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_1283)
    OP_8C(0x10A, 270, 0)
    OP_8C(0x1E, 90, 0)
    WaitChrThread(0x10A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x1F, 0x0)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10A, 6)
    SetChrSubChip(0x10A, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #25
        0x10A,
        (
            "#815F#12PI'm not sure I'll make much of an opponent,\x01",
            "but I'll do what I can!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_1332():
        OP_8F(0xFE, 0xFFFFFBF0, 0x0, 0x5FB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1332)
    Sleep(500)

    ChrTalk(    #26
        0x1E,
        (
            "#115F#5PIt's not every day one has the chance to\x01",
            "test their skills against a relative of the\x01",
            "Eight Leaves school's founder...\x02\x03",

            "#112FI'm eager to see what you can do!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1E, 13)
    SetChrSubChip(0x1E, 0)
    Sleep(500)
    OP_1D(0x2B)
    Sleep(500)

    ChrTalk(    #27
        0x1E,
        "#114F#5P#3SBegin!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #28
        0x10A,
        "#815F#3S#12PRight!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_148D():
        OP_6B(2300, 200)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_148D)

    def lambda_149D():
        OP_91(0xFE, 0xFFFFF060, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_149D)
    SetChrChipByIndex(0x1E, 14)

    def lambda_14BD():
        OP_91(0xFE, 0xFA0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_14BD)
    WaitChrThread(0x1F, 0x0)
    OP_44(0x10A, 0x0)
    OP_44(0x1E, 0x0)
    OP_41(0x9, 0x0, 0xFF)
    OP_31(0x9, 0x10, 0x5A)
    OP_31(0x9, 0x5, 0xC8)
    OP_31(0x9, 0xFE, 0x0)
    OP_35(0x9, 0xFFFF)
    OP_34(0x9, 0xFFFF)
    OP_35(0x9, 0x0)
    OP_BB(0x9, 0x6, 0x110)
    OP_37(0x9, 0x7F, 0x0)
    OP_37(0x9, 0x7F, 0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_153B")
    OP_41(0x9, 0x3E8, 0xFF)
    OP_34(0x9, 0x82)
    OP_34(0x9, 0x83)
    OP_34(0x9, 0x33)
    OP_34(0x9, 0xB)
    OP_34(0x9, 0x47)
    OP_3E(0x207, 2)
    Jump("loc_1607")

    label("loc_153B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1568")
    OP_41(0x9, 0x3E8, 0xFF)
    OP_34(0x9, 0x82)
    OP_34(0x9, 0x83)
    OP_34(0x9, 0x33)
    OP_34(0x9, 0xB)
    OP_34(0x9, 0x47)
    OP_3E(0x207, 2)
    Jump("loc_1607")

    label("loc_1568")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B4")
    OP_41(0x9, 0x146, 0xFF)
    OP_41(0x9, 0x58C, 0xFF)
    OP_34(0x9, 0x82)
    OP_34(0x9, 0x83)
    OP_34(0x9, 0x33)
    OP_34(0x9, 0xB)
    OP_34(0x9, 0x47)
    OP_3E(0x207, 2)
    OP_3E(0x1D7, 1)
    OP_3E(0x1D9, 1)
    OP_34(0x9, 0x50)
    OP_34(0x9, 0x63)
    OP_34(0x9, 0x60)
    OP_34(0x9, 0x6C)
    Jump("loc_1607")

    label("loc_15B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1607")
    OP_41(0x9, 0x146, 0xFF)
    OP_41(0x9, 0x58D, 0xFF)
    OP_34(0x9, 0x82)
    OP_34(0x9, 0x83)
    OP_34(0x9, 0x33)
    OP_34(0x9, 0xB)
    OP_34(0x9, 0x47)
    OP_3E(0x207, 2)
    OP_3E(0x1D7, 1)
    OP_3E(0x1D9, 1)
    OP_34(0x9, 0x50)
    OP_34(0x9, 0x63)
    OP_34(0x9, 0x60)
    OP_34(0x9, 0x6C)
    OP_3E(0x1FE, 1)
    OP_3E(0x1FF, 1)

    label("loc_1607")

    Battle(0x39C, 0x300003, 0x0, 0x0, 0xFF)
    Call(0, 7)
    Return()

    # Function_6_4ED end

    def Function_7_1619(): pass

    label("Function_7_1619")

    EventBegin(0x0)
    OP_20(0x0)
    FadeToDark(0, 0, -1)
    OP_31(0x9, 0xFC, 0x0)
    OP_31(0x9, 0xFE, 0x0)
    OP_44(0x10A, 0x0)
    OP_44(0x1E, 0x0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x18, 0x80)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3270, 0, 20110, 270)
    OP_6D(2090, 0, 20150, 0)
    OP_67(0, 4620, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(90000, 0)
    OP_6E(300, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_16EF"),
        (1, "loc_16FC"),
        (SWITCH_DEFAULT, "loc_1709"),
    )


    label("loc_16EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1709")

    label("loc_16FC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1709")

    label("loc_1709")

    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1723"),
        (1, "loc_18A3"),
        (SWITCH_DEFAULT, "loc_1A13"),
    )


    label("loc_1723")

    SetChrPos(0x10A, -1210, 0, 22350, 180)
    SetChrChipByIndex(0x10A, 6)
    SetChrSubChip(0x10A, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x800)
    SetChrPos(0x1E, -1210, 0, 17900, 0)
    SetChrChipByIndex(0x1E, 15)
    SetChrSubChip(0x1E, 3)
    FadeToBright(2000, 0)
    OP_6B(2960, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #29
        0x10A,
        (
            "#1316F#5P*pant*...*pant*...\x02\x03",

            "#1314FHoly crap... I-I did it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x1E,
        (
            "#119F#12PWell...it looks like my skills still have a lot\x01",
            "of room for improvement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#1125F#5PAll right. The victor is decided.\x02\x03",

            "#1122FSheathe your blades.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_99(0x1E, 0x3, 0x0, 0x3E8)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1E, 12)
    SetChrSubChip(0x1E, 0)
    OP_0D()
    Sleep(300)
    Jump("loc_1A13")

    label("loc_18A3")

    SetChrPos(0x10A, -1210, 0, 22350, 180)
    SetChrChipByIndex(0x10A, 8)
    SetChrSubChip(0x10A, 3)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x800)
    SetChrPos(0x1E, -1210, 0, 17900, 0)
    SetChrChipByIndex(0x1E, 13)
    SetChrSubChip(0x1E, 0)
    FadeToBright(2000, 0)
    OP_6B(2960, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #32
        0x10A,
        (
            "#1312F#6POwowowow...\x02\x03",

            "#813FI should've known I'd stand no chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x1E,
        (
            "#110F#11PI'm amazed by just how well you did fight,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "#1125F#5PAll right. The victor is decided.\x02\x03",

            "#1122FSheathe your blades.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_99(0x10A, 0x3, 0x0, 0x3E8)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1E, 12)
    SetChrSubChip(0x1E, 0)
    OP_0D()
    Sleep(300)
    Jump("loc_1A13")

    label("loc_1A13")

    OP_1D(0xF)

    def lambda_1A1B():
        OP_6D(720, 0, 18750, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_1A1B)

    def lambda_1A33():
        OP_67(0, 4620, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1A33)

    def lambda_1A4B():
        OP_6B(2960, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_1A4B)

    def lambda_1A5B():
        OP_6C(135000, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_1A5B)

    def lambda_1A6B():
        OP_6E(300, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1A6B)
    OP_8E(0x10, 0x4D8, 0x0, 0x4C9A, 0x5DC, 0x0)
    WaitChrThread(0x1F, 0x0)
    Sleep(300)
    TurnDirection(0x10, 0x10A, 400)
    Sleep(500)

    ChrTalk(    #35
        0x10,
        (
            "#1120F#5PSo, Anelace...\x02\x03",

            "How did his swordsmanship appear to you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x10A, 0x10, 500)

    ChrTalk(    #36
        0x10A,
        (
            "#812F#6PW-Well...\x02\x03",

            "#817F...he fights using the Eight Leaves School's fifth \x01",
            "form, Morning Moon.\x02\x03",

            "#816FHe's made a few changes to the standard form,\x01",
            "but it's largely a style based around sword-drawing\x01",
            "techniques.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10A)
    Sleep(500)

    ChrTalk(    #37
        0x10A,
        (
            "#813F#6PWell, okay, I noticed a bit more than just\x01",
            "technical details like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        "#1120F#5PHmm? What did you notice?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10A,
        (
            "#817F#6POne thing I realized while fighting him...\x02\x03",

            "...Richard swings his sword as if perfectly\x01",
            "synchronized to my breathing.\x02\x03",

            "The second I go on the offensive, he reacts\x01",
            "without fail.\x02\x03",

            "#813FIn that sense, it feels like his swordsmanship is \x01",
            "much more defensive than offensive, I suppose.\x02\x03",

            "#816FThat defensive stance matches perfectly with\x01",
            "the form he uses in combat, and the result is\x01",
            "very natural, very powerful swordsmanship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        "#1124F#5POho...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x1E,
        "#110F#11PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10A,
        (
            "#813F#6PWhat I can't work out is why you're so focused on\x01",
            "fighting defensively to begin with.\x02\x03",

            "I mean, I assume it's because you want to protect\x01",
            "something, but what?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(    #43
        0x1E,
        "#119F#11P...Anelace.\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A)
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x10A, 0x1E, 500)

    ChrTalk(    #44
        0x10A,
        "#1317F#6PY-Yes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x1E,
        (
            "#115F#11PI wield a sword for but one, single reason.\x02\x03",

            "#110FThat reason is to protect this country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10A,
        "#814F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x1E,
        (
            "#119F#11PEveryone has at least something that they wish\x01",
            "to protect in this world.\x02\x03",

            "Perhaps that is a person, such as their family or\x01",
            "loved ones.\x02\x03",

            "Perhaps it is a belief or ideology that they hold\x01",
            "dear.\x02\x03",

            "#110FAnd just as the things we seek to protect are \x01",
            "different, so, too, are the ways we choose to do\x01",
            "it.\x02\x03",

            "In my case, the way I choose to protect what \x01",
            "I care about just happens to perfectly suit the\x01",
            "defensive swordsmanship you noticed.\x02\x03",

            "#495FHeh... Although, I can only imagine how comical\x01",
            "it must sound to hear a criminal who threatened\x01",
            "this nation talk about wanting to protect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10A,
        "#813F#6PE-Erm, well, not really...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        "#1128F#5P...Richard, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x1E,
        (
            "#119F#11PPlease don't say anything, General.\x02\x03",

            "Her Majesty may have chosen to pardon me for\x01",
            "what I did, but that doesn't make those crimes\x01",
            "simply disappear.\x02\x03",

            "#110FStill, just as your desire to protect Liberl remained\x01",
            "even after leaving the army, I can't completely turn\x01",
            "my back on mine.\x02\x03",

            "It was so that I could do so that I resolved to leave\x01",
            "the army, even.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10A,
        "#1317F#6PIt was?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x1E,
        (
            "#115F#11PYou see, Anelace...\x02\x03",

            "...to me, one's position in life is just a means to\x01",
            "an end--a way in which to achieve whatever you\x01",
            "wish to do.\x02\x03",

            "#111FI think that's true for one's choice of weapon as\x01",
            "well. Wouldn't you agree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10A,
        "#814F#6P...Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#1125F#5PWhat's important isn't what weapon you choose \x01",
            "but what you use it to do--what inspires you to\x01",
            "take it up and use it to fight.\x02\x03",

            "The reason I chose to put my sword aside and\x01",
            "take up a staff is those feelings had changed.\x01",
            "That is all.\x02\x03",

            "#1120FSo, Anelace? Any more thoughts?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10A, 135, 300)
    Sleep(400)

    ChrTalk(    #55
        0x10A,
        (
            "#817F#6PI should just use my sword in the way that\x01",
            "best fits me to do what I want.\x02\x03",

            "#1314FThat's what you're trying to say, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10,
        (
            "#1121F#5PSure is. You beat me to it.\x02\x03",

            "#1120FYou're Master Ka-fai's granddaughter, all right.\x01",
            "Very quick to catch on to things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10A,
        (
            "#819F#6PHeehee. I'm just as quick at forgetting things,\x01",
            "too, though.\x02\x03",

            "#1314FBut I finally get where you're coming from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        (
            "#1125F#5PReally?\x02\x03",

            "#1120FHaha. I'm happy to hear that.\x02\x03",

            "Could I ask you to pass my answer on to\x01",
            "Master Ka-fai, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10A,
        (
            "#816F#6PConsider it done!\x02\x03",

            "I'm sure he'll understand.\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2878"),
        (SWITCH_DEFAULT, "loc_2E72"),
    )


    label("loc_2878")


    ChrTalk(    #60
        0x10,
        (
            "#1125F#5PHmm... Then again...\x02\x03",

            "#1128FWould you be opposed, Richard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x1E,
        (
            "#119F#11PHaha... Not at all.\x02\x03",

            "#111FI've already inherited the way of the sword itself\x01",
            "from you.\x02\x03",

            "It's only right that someone else should inherit\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10A,
        "#814F#6PWhat are you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "#1121F#5P...Well, that's settled.\x02\x03",

            "#1120FWould you accept this, Anelace?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_29E0():
        OP_6D(260, 0, 19210, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_29E0)
    OP_8F(0x10, 0xFFFFFF10, 0x0, 0x5280, 0x7D0, 0x0)
    WaitChrThread(0x10, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #64
        "\x07\x05Cassius handed Anelace the \x1F\x90\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_A2(0x2FA6)
    OP_8F(0x10, 0x15E, 0x0, 0x4F74, 0x5DC, 0x0)

    ChrTalk(    #65
        0x10A,
        "#1317F#6PWhat's this?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "#1125F#5PIt's a blade I once used myself.\x02\x03",

            "#1120FI think it would be much happier in the hands of\x01",
            "an active practitioner of swordsmanship than in\x01",
            "my own at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10A,
        (
            "#1317F#6PW-Wait a second!\x02\x03",

            "I couldn't possibly accept this!\x02\x03",

            "#813FThis... Surely if anyone should be taking this\x01",
            "off you, it should be Richard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x1E,
        (
            "#115F#11PPerhaps on the surface, but how things are on the\x01",
            "surface is not what is always most important.\x02\x03",

            "#110FI thought you had just learned that fact?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10A,
        (
            "#819F#6PI'm not sure the lessons I learned earlier have\x01",
            "anything to do with this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x1E,
        (
            "#119F#11PThere's no need to think so seriously about this,\x01",
            "Anelace.\x02\x03",

            "#110FAll you need to do is take up this blade and use\x01",
            "it to do what you want to do, in the way you\x01",
            "choose to do it.\x02\x03",

            "That's all anyone expects of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10A,
        (
            "#812F#6PTo do what I want to do, in the way I choose\x01",
            "to do it...\x02\x03",

            "#813F...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10A)
    Sleep(500)

    ChrTalk(    #72
        0x10A,
        (
            "#817F#6PWell, if you insist.\x02\x03",

            "#816FI'd be happy to accept it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2E72")


    ChrTalk(    #73
        0x1E,
        (
            "#119F#11PI feel I've learned a lot today from having the\x01",
            "opportunity to face off against you.\x02\x03",

            "#110FI do hope I'll have the chance again one day.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10A, 180, 400)
    Sleep(300)

    ChrTalk(    #74
        0x10A,
        "#1314F#6PSo do I!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10,
        (
            "#1121F#5PHaha. You'll both have to make sure you don't\x01",
            "neglect your training, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10A, 135, 400)
    Sleep(300)

    ChrTalk(    #76
        0x10A,
        (
            "#811F#6POf course!\x02\x03",

            "#1310FI wouldn't dream of giving it any less than 100%!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2FE8():
        OP_6B(3460, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_2FE8)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1619 end

    def Function_8_301E(): pass

    label("Function_8_301E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x10A, -1040, 500, 37340, 180)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_6D(15970, 0, 31320, 0)
    OP_67(0, 6330, -10000, 0)
    OP_6B(4400, 0)
    OP_6C(315000, 0)
    OP_6E(300, 0)

    def lambda_30BA():
        OP_6D(-3140, 0, 32590, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_30BA)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10A, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-2060, 500, 36480, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(314000, 0)
    OP_6E(310, 0)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -220, 0, 20640, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1630, 0, 20720, 90)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x9)
    OP_73(0x1)
    Sleep(300)

    def lambda_317B():
        OP_8E(0xFE, 0xFFFFFCEA, 0x1F4, 0x8962, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_317B)
    WaitChrThread(0x10A, 0x0)
    Sleep(300)

    ChrTalk(    #77
        0x10A,
        "#810F#2POh...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_31B8():
        OP_6D(-2110, 0, 22520, 2500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_31B8)

    def lambda_31D0():
        OP_6B(2800, 2500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_31D0)
    WaitChrThread(0x10, 0x0)

    def lambda_31E5():
        OP_8E(0xFE, 0xFFFFFA4C, 0x0, 0x58F2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_31E5)
    Sleep(1000)
    OP_8C(0x10, 0, 400)
    Sleep(300)
    OP_8C(0x11, 0, 400)
    WaitChrThread(0x10A, 0x0)

    ChrTalk(    #78
        0x10,
        (
            "#1120FAh, there you are.\x02\x03",

            "Are you all ready to begin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10A,
        (
            "#810F#2PYes, I am...\x02\x03",

            "What's Julia doing here, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x11,
        (
            "#170FHaha. It's been quite some time since we last met,\x01",
            "hasn't it?\x02\x03",

            "To answer your question, though, I was here for\x01",
            "training. I was just just on my way back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10,
        (
            "#1120FStill, you're here, so it wouldn't hurt to stay\x01",
            "for a while longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #82
        0x10,
        "#1120F#4PYou're up for it, then?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #83
        0x11,
        "#170F#5P...Certainly.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #84
        0x11,
        "#170FI'd be happy to fight her.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #85
        0x10A,
        (
            "#810F#2PF-Fight her?\x02\x03",

            "W-Wait... Fight ME?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 400)

    ChrTalk(    #86
        0x10,
        (
            "#1120FCome on, now...\x02\x03",

            "Who else is there here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10A,
        "#810F#2PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x10,
        (
            "#1120FI thought you wanted to know the answer to your\x01",
            "question from earlier?\x02\x03",

            "Have you changed your mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x10A,
        "#810F#2P?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10,
        (
            "#1120FDoubts regarding swordsmanship can only be\x01",
            "dispelled through swordsmanship.\x02\x03",

            "Focus not on whether you win or lose, but on \x01",
            "pouring all you have into the battle, and you \x01",
            "should find the answer you seek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10A,
        (
            "#810F#2PA-All right, then...\x02\x03",

            "I'll do what I can!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10A, 6)
    SetChrSubChip(0x10A, 0)
    OP_0D()
    Sleep(300)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_365C():
        OP_96(0xFE, 0xFFFFFAC4, 0x0, 0x6126, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_365C)
    WaitChrThread(0x10A, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    ChrTalk(    #92
        0x11,
        (
            "#170FHeh. Excellent.\x02\x03",

            "I look forward to seeing what someone related to a\x01",
            "famous master of the sword can do.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x11, 3)
    SetChrSubChip(0x11, 0)
    OP_0D()
    OP_43(0x10, 0x0, 0x0, 0x9)

    def lambda_3716():
        OP_6D(-2700, 0, 22770, 1500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3716)

    def lambda_372E():
        OP_67(0, 4940, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_372E)

    def lambda_3746():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3746)

    def lambda_3756():
        OP_6E(309, 1500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_3756)
    Sleep(300)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_3770():
        OP_96(0xFE, 0xFFFFF902, 0x0, 0x49D4, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3770)
    WaitChrThread(0x11, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x12, 0x0)

    ChrTalk(    #93
        0x11,
        "#170FBegin!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x10A,
        "#810F#2PRight!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_37D5():
        OP_6B(2300, 200)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_37D5)

    def lambda_37E5():
        OP_91(0xFE, 0xFFFFFED4, 0x0, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_37E5)
    SetChrChipByIndex(0x11, 4)

    def lambda_3805():
        OP_91(0xFE, 0x12C, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3805)
    WaitChrThread(0x10, 0x0)
    OP_44(0x10A, 0x0)
    OP_44(0x11, 0x0)
    Battle(0x39C, 0x300003, 0x0, 0x0, 0xFF)
    Call(0, 10)
    Return()

    # Function_8_301E end

    def Function_9_3839(): pass

    label("Function_9_3839")

    OP_8C(0x10, 270, 400)

    def lambda_3846():
        OP_8F(0xFE, 0xA82, 0x0, 0x5604, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3846)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_9_3839 end

    def Function_10_3861(): pass

    label("Function_10_3861")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x10A, 0x0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x18, 0x80)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3270, 0, 20110, 270)
    OP_6D(-170, 0, 21210, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(299, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3924"),
        (1, "loc_3931"),
        (SWITCH_DEFAULT, "loc_393E"),
    )


    label("loc_3924")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_393E")

    label("loc_3931")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_393E")

    label("loc_393E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3978")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[◇Won]\x01",       # 0
            "[◇Lost]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)

    label("loc_3978")

    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3992"),
        (1, "loc_3AAC"),
        (SWITCH_DEFAULT, "loc_3BFA"),
    )


    label("loc_3992")

    SetChrPos(0x10A, -1250, 0, 22350, 180)
    SetChrChipByIndex(0x10A, 6)
    SetChrSubChip(0x10A, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1210, 0, 17900, 0)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 3)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #95
        0x10A,
        (
            "#810F*pant*...*pant*...\x02\x03",

            "I-I did it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x11,
        (
            "#170FUgh...\x02\x03",

            "I was defeated...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x10,
        (
            "#1120FAll right. The victor is decided.\x02\x03",

            "Sheathe your blades.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_99(0x11, 0x3, 0x0, 0x3E8)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)
    Jump("loc_3BFA")

    label("loc_3AAC")

    SetChrPos(0x10A, -1250, 0, 22350, 180)
    SetChrChipByIndex(0x10A, 8)
    SetChrSubChip(0x10A, 3)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1210, 0, 17900, 0)
    SetChrChipByIndex(0x11, 3)
    SetChrSubChip(0x11, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #98
        0x10A,
        (
            "#810FOwowowow...\x02\x03",

            "Looks like that one didn't go well for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x11,
        (
            "#170FWhew...\x02\x03",

            "I was able to emerge victorious after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10,
        (
            "#1120FAll right. The victor is decided.\x02\x03",

            "Sheathe your blades.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_99(0x10A, 0x3, 0x0, 0x3E8)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)
    Jump("loc_3BFA")

    label("loc_3BFA")


    def lambda_3C00():
        OP_6D(2090, 0, 20150, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3C00)

    def lambda_3C18():
        OP_67(0, 4620, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3C18)

    def lambda_3C30():
        OP_6B(2960, 1500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3C30)

    def lambda_3C40():
        OP_6C(90000, 1500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_3C40)

    def lambda_3C50():
        OP_6E(300, 1500)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_3C50)
    OP_8C(0x10A, 135, 400)
    Sleep(300)
    OP_8C(0x11, 45, 400)
    Sleep(300)
    WaitChrThread(0x10, 0x0)
    Sleep(300)

    ChrTalk(    #101
        0x10,
        (
            "#1120FAnelace...\x02\x03",

            "How did her swordsmanship appear to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x10A,
        (
            "#810F#6PI-It was really fierce... But she wasn't all\x01",
            "focused on going on the offensive, either.\x02\x03",

            "It felt as if she was fighting to deflect her\x01",
            "opponent's attacks, rather than to attack by\x01",
            "herself.\x02\x03",

            "It was quite unusual in that sense.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #103
        0x11,
        (
            "#170FI see... So that's how my swordsmanship seemed to\x01",
            "you.\x02\x03",

            "You're probably right about it, too.\x02\x03",

            "After all, the reason I wield a sword is to\x01",
            "protect Her Majesty and Her Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10A,
        (
            "#810F#6P...Oh...\x02\x03",

            "Th-Then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10,
        (
            "#1120FThe weapon you use is simply the means to an end.\x02\x03",

            "What matters most is why you wield it -- the\x01",
            "feelings that drive you to fight, and you use\x01",
            "it to try and achieve.\x02\x03",

            "The reason I chose to put my sword aside and take\x01",
            "up a staff is those feelings had changed -- that\x01",
            "is all.\x02\x03",

            "So, Anelace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x10A,
        (
            "#810F#6P...I should just use my sword in the way that\x01",
            "best fits me to do what I want, then?\x02\x03",

            "That's what you're trying to say, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        (
            "#1120FSure is. You beat me to it.\x02\x03",

            "You're Master Ka-fai's granddaughter, all right.\x01",
            "Very quick to catch on to things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10A,
        (
            "#810F#6PHeehee. Unfortunately I'm just as quick at\x01",
            "forgetting things, too, though.\x02\x03",

            "Still, I think now I finally understand how you\x01",
            "feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x10,
        (
            "#1120FHaha. I'm happy to hear that.\x02\x03",

            "Could I ask you to pass my answer on to Master\x01",
            "Ka-fai, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x10A,
        (
            "#810F#6POf course!\x02\x03",

            "I'm sure he'll understand, too.\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4201"),
        (SWITCH_DEFAULT, "loc_43D8"),
    )


    label("loc_4201")


    ChrTalk(    #111
        0x10,
        (
            "#1120FHmm... Still...\x02\x03",

            "Perhaps you could take this as a parting gift of\x01",
            "sorts.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_4260():
        OP_6D(1650, 0, 21380, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4260)
    OP_8C(0x10, 315, 0)
    OP_8F(0x10, 0xFFFFFF9C, 0x0, 0x54F6, 0x7D0, 0x0)
    WaitChrThread(0x10, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #112
        "\x07\x05Obtained \x1F\x90\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_8F(0x10, 0x3DE, 0x0, 0x5154, 0x7D0, 0x0)

    ChrTalk(    #113
        0x10,
        (
            "#1120F#2PThis is a blade I used to fight with myself.\x02\x03",

            "I think it would be much happier in the hands of \x01",
            "an active practitioner of swordsmanship than in \x01",
            "my own at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x10A,
        (
            "#810F#6PWoooow!\x02\x03",

            "Th-Thank you very much!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D8")

    label("loc_43D8")


    ChrTalk(    #115
        0x11,
        (
            "#170FI learned a lot from being able to fight you\x01",
            "myself.\x02\x03",

            "Hopefully we will have the opportunity to fight\x01",
            "like this again one day in the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10A, 180, 400)
    Sleep(300)

    ChrTalk(    #116
        0x10A,
        "#810F#5PHeehee. I'd like that, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x10,
        (
            "#1120F#2PHaha. You'll both have to make sure you don't\x01",
            "neglect your training, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10A, 135, 400)
    Sleep(300)

    ChrTalk(    #118
        0x10A,
        (
            "#810F#6POf course!\x02\x03",

            "I wouldn't dream of giving it any less than 100!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_3861 end

    SaveToFile()

Try(main)
