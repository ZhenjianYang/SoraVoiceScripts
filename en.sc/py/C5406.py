from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5406   ._SN',
        MapName             = 'Other',
        Location            = 'C5406.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        'Campanella',                           # 9
        'Pale Apache',                          # 10
        'Enhanced Jaeger',                      # 11
        'Enhanced Jaeger',                      # 12
        'Enhanced Jaeger',                      # 13
        'Enhanced Jaeger',                      # 14
        'Enhanced Jaeger',                      # 15
        'Enhanced Jaeger',                      # 16
        'Enhanced Jaeger',                      # 17
        'Enhanced Jaeger',                      # 18
        'Enhanced Jaeger',                      # 19
        'Enhanced Jaeger',                      # 20
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
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
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03600 ._CH',             # 00
        'ED6_DT27/CH04010 ._CH',             # 01
        'ED6_DT29/CH12390 ._CH',             # 02
        'ED6_DT27/CH04000 ._CH',             # 03
        'ED6_DT29/CH12390 ._CH',             # 04
        'ED6_DT27/CH04620 ._CH',             # 05
        'ED6_DT27/CH04621 ._CH',             # 06
        'ED6_DT27/CH04622 ._CH',             # 07
        'ED6_DT26/CH20298 ._CH',             # 08
        'ED6_DT27/CH04000 ._CH',             # 09
        'ED6_DT27/CH04011 ._CH',             # 0A
        'ED6_DT27/CH04001 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT27/CH03600P._CP',             # 00
        'ED6_DT27/CH04010P._CP',             # 01
        'ED6_DT29/CH12390P._CP',             # 02
        'ED6_DT27/CH04000P._CP',             # 03
        'ED6_DT29/CH12390P._CP',             # 04
        'ED6_DT27/CH04620P._CP',             # 05
        'ED6_DT27/CH04621P._CP',             # 06
        'ED6_DT27/CH04622P._CP',             # 07
        'ED6_DT26/CH20298P._CP',             # 08
        'ED6_DT27/CH04000P._CP',             # 09
        'ED6_DT27/CH04011P._CP',             # 0A
        'ED6_DT27/CH04001P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 1130,
        Y                   = 3000,
        Z                   = -178880,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 35,
    )

    DeclEvent(
        X                   = -2550,
        Y                   = -2000,
        Z                   = 7130,
        Range               = 4630,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x1252,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_2CA",          # 00, 0
        "Function_1_2FC",          # 01, 1
        "Function_2_378",          # 02, 2
        "Function_3_4F5",          # 03, 3
        "Function_4_510",          # 04, 4
        "Function_5_1510",         # 05, 5
        "Function_6_15EC",         # 06, 6
        "Function_7_1D80",         # 07, 7
        "Function_8_1DC8",         # 08, 8
        "Function_9_1F60",         # 09, 9
        "Function_10_1FD1",        # 0A, 10
        "Function_11_200E",        # 0B, 11
        "Function_12_238A",        # 0C, 12
        "Function_13_23A4",        # 0D, 13
        "Function_14_2685",        # 0E, 14
        "Function_15_26CC",        # 0F, 15
        "Function_16_2718",        # 10, 16
        "Function_17_275F",        # 11, 17
        "Function_18_278F",        # 12, 18
        "Function_19_27BF",        # 13, 19
        "Function_20_2801",        # 14, 20
        "Function_21_2848",        # 15, 21
        "Function_22_2878",        # 16, 22
        "Function_23_28A8",        # 17, 23
        "Function_24_28D8",        # 18, 24
        "Function_25_291E",        # 19, 25
        "Function_26_2969",        # 1A, 26
        "Function_27_29B4",        # 1B, 27
        "Function_28_29FF",        # 1C, 28
        "Function_29_2A36",        # 1D, 29
        "Function_30_2A68",        # 1E, 30
        "Function_31_2A9F",        # 1F, 31
        "Function_32_2AD6",        # 20, 32
        "Function_33_2B0D",        # 21, 33
        "Function_34_2B44",        # 22, 34
        "Function_35_2D1B",        # 23, 35
    )


    def Function_0_2CA(): pass

    label("Function_0_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2E4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 11)
    Jump("loc_2FB")

    label("loc_2E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_2FB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 34)

    label("loc_2FB")

    Return()

    # Function_0_2CA end

    def Function_1_2FC(): pass

    label("Function_1_2FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31A")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x385, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_354")
    OP_72(0x0, 0x8)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 0)
    OP_72(0x1, 0x8)
    OP_72(0x1, 0x20)
    OP_6F(0x1, 0)
    OP_71(0x1, 0x4)
    Jump("loc_377")

    label("loc_354")

    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_71(0x8, 0x4)

    label("loc_377")

    Return()

    # Function_1_2FC end

    def Function_2_378(): pass

    label("Function_2_378")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4DF")

    label("loc_39D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B6")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4DF")

    label("loc_3B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CF")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4DF")

    label("loc_3CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E8")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4DF")

    label("loc_3E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_401")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4DF")

    label("loc_401")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4DF")

    label("loc_41A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_433")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4DF")

    label("loc_433")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4DF")

    label("loc_44C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_465")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4DF")

    label("loc_465")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4DF")

    label("loc_47E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_497")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4DF")

    label("loc_497")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B0")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4DF")

    label("loc_4B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C9")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4DF")

    label("loc_4C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DF")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4DF")

    label("loc_4F4")

    Return()

    # Function_2_378 end

    def Function_3_4F5(): pass

    label("Function_3_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x385, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_507")
    Return()

    label("loc_507")

    Call(0, 4)
    Call(0, 6)
    Return()

    # Function_3_4F5 end

    def Function_4_510(): pass

    label("Function_4_510")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(1070, -1000, 4640, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 1240, -1000, 20540, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 1880, -1000, 4290, 0)
    SetChrPos(0x102, 370, -1000, 4390, 0)
    OP_0D()

    NpcTalk(    #0
        0x8,
        "Young Voice",
        (
            "#4PHeeheehee...\x01",
            "You're a bit late, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_60B():
        OP_6D(1780, -1000, 9150, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60B)

    def lambda_623():
        OP_67(0, 6240, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_623)

    def lambda_63B():
        OP_6B(2800, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_63B)

    def lambda_64B():
        OP_6E(323, 3500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_64B)
    OP_8E(0x8, 0x500, 0xFFFFFC18, 0x2EE0, 0x9C4, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #1
        0x101,
        "#1020F#2PYou!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#1032F#2P...Campanella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#854F#3PJoshua! How cold.\x02\x03",

            "You have that nice, long heart-to-heart with Loewe\x01",
            "and you don't even stop by to say hello to your\x01",
            "old friend Campanella?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#1035F#2PI didn't think you were still\x01",
            "on the ship.\x02\x03",

            "#1030FLet me guess, you knew I was\x01",
            "coming this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#851F#3PHaha! Well, I AM the one the Grandmaster\x01",
            "sent to observe the plan.\x02\x03",

            "It's my job to notice more than the\x01",
            "others do, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        "#1032F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#850F#3PHeheh. It's impressive, though.\x02\x03",

            "You've changed quite a bit in the, what,\x01",
            "half-decade since last we met.\x02\x03",

            "You've become much more of a man, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1031F#2PAnd you...literally haven't changed at all.\x02\x03",

            "Even your appearance is exactly the same,\x01",
            "as though you haven't aged a day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#851F#3PHahaha. Well, I make sure to NEVER skip\x01",
            "my daily skin-care, after all!\x02\x03",

            "#854FI've heard you enjoy a good romp in a\x01",
            "dress every now and then. Perhaps I could\x01",
            "introduce you to some cosmetics?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        "#1030F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1022F#2PArgh!\x01",
            "Could you be any more aggravating?!\x02\x03",

            "#1005FYou were waiting here for us because you\x01",
            "wanted to fight, right?\x02\x03",

            "Just FIGHT US already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#851FHaha. Oh, my goodness, what a strong little girl.\x02\x03",

            "#850FI'd wondered what kind of girl could pluck your\x01",
            "heart like a grape, Joshua.\x02\x03",

            "She's a good match for you, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1013F#2PW-W-Wait, who plucked whose heart like--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#854FAhhh, I forget myself, though. Your proper\x01",
            "girlfriend is that bandit girl, isn't it?\x02\x03",

            "#851FOooh, Joshua, you're such a stud. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1019F#2P.   .   .\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1035F#2P...That's quite enough of your nonsense.\x02\x03",

            "I have no idea how you even know about\x01",
            "Josette. But either way...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 1)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #17
        0x102,
        (
            "#1030F#2POur abilities in combat should be about the\x01",
            "same...and I doubt Estelle will just sit idly by.\x02\x03",

            "Do you still intend to stop us with force?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#851F#3PAhaha! No, no, that wasn't my intent at all!\x02\x03",

            "#850FAs I said, I'm simply here to observe\x01",
            "the plan unfold.\x02\x03",

            "I've no duty to impede you two directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        "#1032F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1015F#2PWait, really?\x02\x03",

            "Then why bother waiting for us here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#853F#3PHaha. To say my farewells, of course.\x02\x03",

            "#854FBut, you know, just saying 'goodbye' isn't\x01",
            "very exciting at all.\x02\x03",

            "So I thought I'd help make your escape\x01",
            "story a bit more...riveting!\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_F5A():
        OP_6D(1800, -1000, 11000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F5A)

    def lambda_F72():
        OP_6B(2500, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F72)
    Sleep(500)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_99(0x8, 0x1, 0x2, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    OP_1F(0x5A, 0x3E8)
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x135, 0x1, 0x32)
    Sleep(200)
    OP_24(0x135, 0x3C)
    Sleep(200)
    OP_24(0x135, 0x46)
    Sleep(200)
    OP_24(0x135, 0x50)
    Sleep(200)
    OP_24(0x135, 0x5A)
    Sleep(200)
    OP_24(0x135, 0x64)
    Sleep(200)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(70)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_1F(0x64, 0x3E8)

    def lambda_103D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_103D)
    Sleep(50)

    def lambda_1050():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1050)
    LoadEffect(0x1, "map\\\\mp003_00.eff")
    OP_6D(1160, -1000, 2460, 1500)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 1390, -1000, -1260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 1050, -1000, 420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_10FC():
        OP_96(0xFE, 0xFFFFFDE4, 0xFFFFFC18, 0x141E, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10FC)
    Sleep(100)

    def lambda_111F():
        OP_96(0xFE, 0xBA4, 0xFFFFFC18, 0x1310, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_111F)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 1420, -1000, 2270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 1100, -1000, 3760, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 1600, -1000, 5220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 1050, -1000, 6410, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)

    def lambda_1265():
        OP_6D(6550, 890, 5910, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1265)

    def lambda_127D():
        OP_67(0, 3790, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_127D)

    def lambda_1295():
        OP_6B(4030, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1295)

    def lambda_12A5():
        OP_6C(90000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12A5)

    def lambda_12B5():
        OP_6E(271, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12B5)
    SetChrPos(0x9, 7200, 3370, -17760, 0)
    ClearChrFlags(0x9, 0x80)

    def lambda_12DB():

        label("loc_12DB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_12DB")

    QueueWorkItem2(0x9, 3, lambda_12DB)

    def lambda_12EE():

        label("loc_12EE")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_12EE")

    QueueWorkItem2(0x101, 0, lambda_12EE)

    def lambda_12FF():

        label("loc_12FF")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_12FF")

    QueueWorkItem2(0x102, 0, lambda_12FF)
    OP_43(0x9, 0x0, 0x0, 0x5)
    Sleep(3000)

    def lambda_131C():
        OP_8C(0xFE, 270, 100)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_131C)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x102, 10)
    OP_44(0x102, 0x0)
    OP_8E(0x102, 0x988, 0xFFFFFC18, 0x19A0, 0xFA0, 0x0)
    OP_8C(0x102, 90, 400)
    SetChrChipByIndex(0x102, 1)
    WaitChrThread(0x9, 0x0)
    OP_44(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #22
        0x101,
        "#1020F#2PWh-Wh-Whaaaa...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1034F#5PThe Pale Apache flying orbal puppet?!\x02\x03",

            "The society already has working models?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(7630, -1000, 9550, 0)
    OP_67(0, 3790, -10000, 0)
    OP_6B(4630, 0)
    OP_6C(42000, 0)
    OP_6E(271, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #24
        0x8,
        (
            "#853F#5PAnd so a new obstacle arises to block\x01",
            "the reunited heroes!\x02\x03",

            "#854FHow will this affect their legend?\x01",
            "Let's find out!\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_14BB():
        OP_8F(0xFE, 0x198C, 0x12C, 0x161C, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14BB)

    def lambda_14D6():
        OP_6B(3270, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14D6)
    WaitChrThread(0x101, 0x2)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Battle(0x429, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_150A"),
        (SWITCH_DEFAULT, "loc_150F"),
    )


    label("loc_150A")

    OP_B4(0x0)
    Jump("loc_150F")

    label("loc_150F")

    Return()

    # Function_4_510 end

    def Function_5_1510(): pass

    label("Function_5_1510")


    def lambda_1516():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1516)
    Sleep(300)

    def lambda_1536():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1536)
    Sleep(300)

    def lambda_1556():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1556)
    Sleep(300)

    def lambda_1576():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1576)
    Sleep(300)

    def lambda_1596():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1596)
    Sleep(300)

    def lambda_15B6():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_15B6)
    Sleep(300)

    def lambda_15D6():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_15D6)
    Return()

    # Function_5_1510 end

    def Function_6_15EC(): pass

    label("Function_6_15EC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2600D2, 0x2600D7, 0xC)
    OP_44(0x9, 0x2)
    OP_44(0x8, 0x0)
    SetChrPos(0x8, 1280, -1000, 12000, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 11540, 900, 5660, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 2110, -1000, 3460, 90)
    SetChrPos(0x102, 950, -1000, 4990, 90)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 1)
    SetChrSubChip(0x102, 0)
    OP_6D(6550, -400, 6000, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(57000, 0)
    OP_6E(365, 0)
    LoadEffect(0x2, "battle\\btbomb00.eff")
    LoadEffect(0x3, "map\\mp090_00.eff")
    OP_43(0x9, 0x3, 0x0, 0x8)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x9, 0x3)
    Sleep(300)

    ChrTalk(    #25
        0x8,
        "#2PHahaha! Well done, well done!\x02",
    )

    CloseMessageWindow()

    def lambda_1719():
        OP_6D(2270, -1000, 8930, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1719)

    def lambda_1731():
        OP_67(0, 6740, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1731)

    def lambda_1749():
        OP_6B(2500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1749)

    def lambda_1759():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1759)

    def lambda_1769():
        OP_6E(365, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1769)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #26
        0x8,
        (
            "#851F#3PI expected no less of Joshua, but the\x01",
            "missy's really very good as well.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)

    def lambda_17DD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17DD)
    Sleep(100)
    OP_8C(0x102, 0, 400)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x101, 11)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x1000)
    OP_8F(0x101, 0x87A, 0xFFFFFC18, 0x125C, 0x1388, 0x0)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    Sleep(500)

    ChrTalk(    #27
        0x101,
        (
            "#1005F#2PYou, you... Enough of your stupid\x01",
            "messing around!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#853F#3PNow, now, there's no need to be so angry.\x02\x03",

            "#850FAnyway, it's time for the Fool whose\x01",
            "act is done to exit, stage right.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    LoadEffect(0x2, "map\\\\mp055_00.eff")
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1923():
        OP_6D(1800, -1000, 10200, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1923)

    def lambda_193B():
        OP_6B(2300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_193B)
    Sleep(500)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_99(0x8, 0x1, 0x2, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x2, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #29
        0x101,
        "#1020F#2PWha?!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 12)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #30
        0x8,
        (
            "#854F#3PHaha... Well, then, you two.\x02\x03",

            "Let's meet again. Soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    SetChrFlags(0x8, 0x80)
    OP_82(0x0, 0x2)
    OP_43(0x8, 0x3, 0x0, 0x7)
    Sleep(1500)

    def lambda_1A58():
        OP_6D(2550, -1000, 7750, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A58)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #31
        0x101,
        "#1020F#2PHe's gone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        (
            "#1035F#5PThat's just a little escape trick he knows.\x01",
            "Don't worry about it.\x02\x03",

            "#1030FMore importantly...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 990, -1000, -17770, 0)

    NpcTalk(    #33
        0x8,
        "Man's Voice",
        "#1S#1PHey! You sure they came this way?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x7D0)

    def lambda_1B83():
        OP_6D(1020, -1000, -10820, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1B83)

    def lambda_1B9B():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B9B)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    Sleep(100)

    def lambda_1BB8():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BB8)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    WaitChrThread(0x101, 0x3)

    NpcTalk(    #34
        0x8,
        "Man's Voice",
        (
            "#1S#1PDidn't you hear the sounds, idiot?!\x01",
            "No doubt about it!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x2B)
    Sleep(500)
    Fade(500)
    OP_6D(1210, -1000, 5170, 0)
    OP_67(0, 6990, -10000, 0)
    OP_6B(3090, 0)
    OP_6C(60000, 0)
    OP_6E(311, 0)
    OP_0D()
    TurnDirection(0x102, 0x101, 600)
    Sleep(400)

    ChrTalk(    #35
        0x102,
        "#1036F#6PEstelle, we have to hurry!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 600)
    Sleep(400)

    ChrTalk(    #36
        0x101,
        "#1002F#4PRight!\x02",
    )

    CloseMessageWindow()

    def lambda_1CC8():
        OP_6D(12680, -910, 27340, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CC8)

    def lambda_1CE0():
        OP_67(0, 9500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1CE0)

    def lambda_1CF8():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CF8)

    def lambda_1D08():
        OP_6E(375, 6000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1D08)
    OP_43(0x102, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0xA)
    WaitChrThread(0x102, 0x3)
    Sleep(300)
    OP_8E(0x101, 0x2EFE, 0xFFFFFC72, 0x67CA, 0x1388, 0x0)
    SetChrFlags(0x101, 0x80)
    OP_72(0x0, 0x20)
    OP_22(0xFD, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x77)
    OP_73(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_15EC end

    def Function_7_1D80(): pass

    label("Function_7_1D80")

    Sleep(300)
    OP_24(0x10A, 0x5A)
    Sleep(300)
    OP_24(0x10A, 0x50)
    Sleep(300)
    OP_24(0x10A, 0x46)
    Sleep(300)
    OP_24(0x10A, 0x3C)
    Sleep(300)
    OP_24(0x10A, 0x32)
    Sleep(300)
    OP_24(0x10A, 0x28)
    Sleep(300)
    OP_24(0x10A, 0x1E)
    Sleep(300)
    OP_23(0x10A)
    Return()

    # Function_7_1D80 end

    def Function_8_1DC8(): pass

    label("Function_8_1DC8")


    def lambda_1DCE():
        OP_D1(254, 0, 90000, -45000, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1DCE)

    def lambda_1DE8():
        OP_8F(0xFE, 0x2D14, 0xFFFFF060, 0x161C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1DE8)
    PlayEffect(0x2, 0xFF, 0x9, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0x9, 300, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x2, 0xFF, 0x9, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x2, 0xFF, 0x9, 100, 200, 200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0x9, 500, 200, 100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x9, 0x0)
    PlayEffect(0x3, 0xFF, 0x9, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
    Return()

    # Function_8_1DC8 end

    def Function_9_1F60(): pass

    label("Function_9_1F60")

    OP_8E(0xFE, 0x258, 0xFFFFFC18, 0x3A70, 0x1770, 0x0)
    OP_8E(0xFE, 0x2EFE, 0xFFFFFC18, 0x3EDA, 0x1770, 0x0)
    OP_8E(0xFE, 0x2E86, 0xFFFFFB82, 0x61DA, 0x1770, 0x0)
    OP_72(0x0, 0x20)
    OP_22(0xFD, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    OP_8E(0xFE, 0x2EFE, 0xFFFFFC72, 0x67CA, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_1F60 end

    def Function_10_1FD1(): pass

    label("Function_10_1FD1")

    OP_8E(0xFE, 0x726, 0xFFFFFC18, 0x3A02, 0x1770, 0x0)
    OP_8E(0xFE, 0x2EFE, 0xFFFFFC18, 0x3EDA, 0x1770, 0x0)
    OP_8E(0xFE, 0x2E5E, 0xFFFFFB82, 0x5CD0, 0x1770, 0x0)
    Return()

    # Function_10_1FD1 end

    def Function_11_200E(): pass

    label("Function_11_200E")

    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_6D(12550, -1000, 29240, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_71(0x4, 0x4)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 140)
    OP_70(0x0, 0x2EE)
    OP_43(0x8, 0x1, 0x0, 0xC)
    FadeToBright(1000, 0)
    OP_0D()
    LoadEffect(0x1, "map\\\\mp003_00.eff")
    LoadEffect(0x4, "monster\\\\msc0555.eff")
    SetChrPos(0xA, 2200, -1000, 5060, 0)
    SetChrPos(0xB, 2200, -1000, 5060, 0)
    SetChrPos(0xC, 2200, -1000, 5060, 0)
    SetChrPos(0xD, 2200, -1000, 5060, 0)
    SetChrPos(0xE, 2200, -1000, 5060, 0)
    SetChrPos(0xF, 310, -1000, 4040, 0)
    SetChrPos(0x10, 310, -1000, 4040, 0)
    SetChrPos(0x11, 310, -1000, 4040, 0)
    SetChrPos(0x12, 310, -1000, 4040, 0)
    SetChrPos(0x13, 310, -1000, 4040, 0)

    def lambda_2160():
        OP_6D(9470, -1150, 23720, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2160)

    def lambda_2178():
        OP_67(0, 4190, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2178)

    def lambda_2190():
        OP_6E(360, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2190)
    Sleep(1500)
    OP_43(0xA, 0x1, 0x0, 0xE)
    OP_43(0xF, 0x1, 0x0, 0x13)
    Sleep(200)
    OP_43(0xB, 0x1, 0x0, 0xF)
    OP_43(0x10, 0x1, 0x0, 0x14)
    Sleep(200)
    OP_43(0xC, 0x1, 0x0, 0x10)
    OP_43(0x11, 0x1, 0x0, 0x15)
    Sleep(200)
    OP_43(0xD, 0x1, 0x0, 0x11)
    OP_43(0x12, 0x1, 0x0, 0x16)
    Sleep(200)
    OP_43(0xE, 0x1, 0x0, 0x12)
    OP_43(0x13, 0x1, 0x0, 0x17)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x101, 0x3)
    Sleep(1000)

    ChrTalk(    #37
        0xF,
        "#5PIt's them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        "#5PFire! Don't let them escape!\x02",
    )

    CloseMessageWindow()

    def lambda_2246():
        OP_6D(9390, -1000, 24480, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2246)

    def lambda_225E():
        OP_67(0, 6620, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_225E)

    def lambda_2276():
        OP_6E(338, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2276)
    OP_43(0xA, 0x1, 0x0, 0x18)
    OP_43(0xF, 0x1, 0x0, 0x1D)
    Sleep(100)
    OP_43(0xB, 0x1, 0x0, 0x19)
    OP_43(0x10, 0x1, 0x0, 0x1E)
    Sleep(100)
    OP_43(0xC, 0x1, 0x0, 0x1A)
    OP_43(0x11, 0x1, 0x0, 0x1F)
    Sleep(100)
    OP_43(0xD, 0x1, 0x0, 0x1B)
    OP_43(0x12, 0x1, 0x0, 0x20)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x1C)
    OP_43(0x13, 0x1, 0x0, 0x21)
    WaitChrThread(0x101, 0x3)
    Sleep(2000)
    OP_73(0x0)
    OP_6F(0x0, 750)
    OP_70(0x0, 0x348)
    OP_22(0x136, 0x0, 0x64)
    OP_73(0x0)
    Sleep(500)
    OP_6F(0x0, 840)
    OP_70(0x0, 0x3D4)
    OP_22(0x136, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_44(0xA, 0x1)
    Sleep(100)
    OP_44(0xB, 0x1)
    Sleep(100)
    OP_44(0xC, 0x1)
    Sleep(100)
    OP_44(0xD, 0x1)
    Sleep(100)
    OP_44(0xE, 0x1)
    Sleep(100)
    OP_44(0xF, 0x1)
    Sleep(100)
    OP_44(0x10, 0x1)
    Sleep(100)
    OP_44(0x11, 0x1)
    Sleep(100)
    OP_44(0x12, 0x1)
    Sleep(100)
    OP_44(0x13, 0x1)
    OP_73(0x0)
    OP_0D()
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0610   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_11_200E end

    def Function_12_238A(): pass

    label("Function_12_238A")

    Sleep(500)
    OP_22(0x133, 0x0, 0x64)
    Sleep(4500)
    OP_22(0x133, 0x0, 0x64)
    Sleep(5000)
    Return()

    # Function_12_238A end

    def Function_13_23A4(): pass

    label("Function_13_23A4")

    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)

    label("loc_23AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2684")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2450")
    Sleep(400)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 9790, -1300, 27370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_2681")

    label("loc_2450")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24DD")
    Sleep(500)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 9870, -1200, 29300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_2681")

    label("loc_24DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_256A")
    Sleep(600)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 9840, 2500, 27360, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_2681")

    label("loc_256A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F7")
    Sleep(700)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 10850, 2500, 25410, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_2681")

    label("loc_25F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2681")
    Sleep(800)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 10920, -1150, 25380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_2681")

    Jump("loc_23AE")

    label("loc_2684")

    Return()

    # Function_13_23A4 end

    def Function_14_2685(): pass

    label("Function_14_2685")

    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x97E, 0xFFFFFC18, 0x3C6E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Return()

    # Function_14_2685 end

    def Function_15_26CC(): pass

    label("Function_15_26CC")

    Sleep(50)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xBC2, 0xFFFFFC18, 0x3778, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Return()

    # Function_15_26CC end

    def Function_16_2718(): pass

    label("Function_16_2718")

    Sleep(70)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x794, 0xFFFFFC18, 0x3200, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_16_2718 end

    def Function_17_275F(): pass

    label("Function_17_275F")

    Sleep(100)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x88E, 0xFFFFFC18, 0x2BFC, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_17_275F end

    def Function_18_278F(): pass

    label("Function_18_278F")

    Sleep(120)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x6D6, 0xFFFFFC18, 0x251C, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_278F end

    def Function_19_27BF(): pass

    label("Function_19_27BF")

    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x2E4, 0xFFFFFC18, 0x3B06, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_19_27BF end

    def Function_20_2801(): pass

    label("Function_20_2801")

    Sleep(50)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x136, 0xFFFFFC18, 0x34A8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_20_2801 end

    def Function_21_2848(): pass

    label("Function_21_2848")

    Sleep(70)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFFFFDE4, 0xFFFFFC18, 0x2E22, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_21_2848 end

    def Function_22_2878(): pass

    label("Function_22_2878")

    Sleep(100)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFA, 0xFFFFFC18, 0x2A08, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_22_2878 end

    def Function_23_28A8(): pass

    label("Function_23_28A8")

    Sleep(120)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFFFFF56, 0xFFFFFC18, 0x2440, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_23_28A8 end

    def Function_24_28D8(): pass

    label("Function_24_28D8")

    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFA, 0xFFFFFC18, 0x3ECF, 0x1388, 0x0)
    OP_8E(0xFE, 0x2378, 0xFFFFFC18, 0x3F48, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 0, 400)
    OP_43(0xA, 0x1, 0x0, 0xD)
    Return()

    # Function_24_28D8 end

    def Function_25_291E(): pass

    label("Function_25_291E")

    Sleep(50)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFA, 0xFFFFFC18, 0x3ECF, 0x1388, 0x0)
    OP_8E(0xFE, 0x1EE6, 0xFFFFFC18, 0x4132, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 0, 400)
    OP_43(0xB, 0x1, 0x0, 0xD)
    Return()

    # Function_25_291E end

    def Function_26_2969(): pass

    label("Function_26_2969")

    Sleep(70)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFA, 0xFFFFFC18, 0x3ECF, 0x1388, 0x0)
    OP_8E(0xFE, 0x19A0, 0xFFFFFC18, 0x4236, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 0, 400)
    OP_43(0xC, 0x1, 0x0, 0xD)
    Return()

    # Function_26_2969 end

    def Function_27_29B4(): pass

    label("Function_27_29B4")

    Sleep(100)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFA, 0xFFFFFC18, 0x3ECF, 0x1388, 0x0)
    OP_8E(0xFE, 0x1284, 0xFFFFFC18, 0x3FB5, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0xD, 0x1, 0x0, 0xD)
    Return()

    # Function_27_29B4 end

    def Function_28_29FF(): pass

    label("Function_28_29FF")

    Sleep(120)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xE4C, 0xFFFFFC18, 0x41F0, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0xE, 0x1, 0x0, 0xD)
    Return()

    # Function_28_29FF end

    def Function_29_2A36(): pass

    label("Function_29_2A36")

    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x8CA, 0xFFFFFC18, 0x54D8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0xF, 0x1, 0x0, 0xD)
    Return()

    # Function_29_2A36 end

    def Function_30_2A68(): pass

    label("Function_30_2A68")

    Sleep(50)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x74E, 0xFFFFFC18, 0x4F9C, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0x10, 0x1, 0x0, 0xD)
    Return()

    # Function_30_2A68 end

    def Function_31_2A9F(): pass

    label("Function_31_2A9F")

    Sleep(70)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xB18, 0xFFFFFC18, 0x4E02, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0x11, 0x1, 0x0, 0xD)
    Return()

    # Function_31_2A9F end

    def Function_32_2AD6(): pass

    label("Function_32_2AD6")

    Sleep(100)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x726, 0xFFFFFC18, 0x46B4, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0x12, 0x1, 0x0, 0xD)
    Return()

    # Function_32_2AD6 end

    def Function_33_2B0D(): pass

    label("Function_33_2B0D")

    Sleep(120)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xB68, 0xFFFFFC18, 0x4614, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0x13, 0x1, 0x0, 0xD)
    Return()

    # Function_33_2B0D end

    def Function_34_2B44(): pass

    label("Function_34_2B44")

    EventBegin(0x0)
    OP_72(0x0, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 980)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0xA, 9080, -1000, 16200, 0)
    SetChrPos(0xB, 7910, -1000, 16690, 0)
    SetChrPos(0xC, 6560, -1000, 16950, 0)
    SetChrPos(0xD, 4740, -1000, 16309, 45)
    SetChrPos(0xE, 3660, -1000, 16880, 45)
    SetChrPos(0xF, 2250, -1000, 21720, 45)
    SetChrPos(0x10, 1870, -1000, 20380, 45)
    SetChrPos(0x11, 2840, -1000, 19970, 45)
    SetChrPos(0x12, 1830, -1000, 18100, 45)
    SetChrPos(0x13, 2920, -1000, 17940, 45)
    OP_6D(6900, -1000, 20600, 0)
    OP_67(0, 6420, -10000, 0)
    OP_6B(3820, 0)
    OP_6C(45000, 0)
    OP_6E(248, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #39
        0xF,
        (
            "#5PRrr! Think they can just fly away?\x01",
            "Hell with that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        (
            "#5PSortie the airships!\x01",
            "We're going after them!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_34_2B44 end

    def Function_35_2D1B(): pass

    label("Function_35_2D1B")

    Return()

    # Function_35_2D1B end

    SaveToFile()

Try(main)
