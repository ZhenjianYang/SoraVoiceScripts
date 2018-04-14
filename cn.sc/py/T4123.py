from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4123   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4123.x',
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
        '艾南',                                 # 9
        '管家菲利普',                           # 10
        '雪拉扎德',                             # 11
        '阿加特',                               # 12
        '奥利维尔',                             # 13
        '科洛丝',                               # 14
        '提妲',                                 # 15
        '金',                                   # 16
        '亚妮拉丝',                             # 17
        '信',                                   # 18
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
        'ED6_DT07/CH02580 ._CH',             # 00
        'ED6_DT07/CH02470 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
        'ED6_DT06/CH20053 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT07/CH00040 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT07/CH00070 ._CH',             # 07
        'ED6_DT07/CH01630 ._CH',             # 08
        'ED6_DT26/CH20301 ._CH',             # 09
        'ED6_DT07/CH00024 ._CH',             # 0A
        'ED6_DT07/CH00054 ._CH',             # 0B
        'ED6_DT07/CH00034 ._CH',             # 0C
        'ED6_DT07/CH00044 ._CH',             # 0D
        'ED6_DT07/CH00064 ._CH',             # 0E
        'ED6_DT07/CH00074 ._CH',             # 0F
        'ED6_DT07/CH00033 ._CH',             # 10
        'ED6_DT07/CH00073 ._CH',             # 11
        'ED6_DT06/CH20021 ._CH',             # 12
        'ED6_DT27/CH03085 ._CH',             # 13
        'ED6_DT27/CH03091 ._CH',             # 14
        'ED6_DT26/CH20415 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT07/CH02580P._CP',             # 00
        'ED6_DT07/CH02470P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
        'ED6_DT06/CH20053P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT07/CH00040P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT07/CH00070P._CP',             # 07
        'ED6_DT07/CH01630P._CP',             # 08
        'ED6_DT26/CH20301P._CP',             # 09
        'ED6_DT07/CH00024P._CP',             # 0A
        'ED6_DT07/CH00054P._CP',             # 0B
        'ED6_DT07/CH00034P._CP',             # 0C
        'ED6_DT07/CH00044P._CP',             # 0D
        'ED6_DT07/CH00064P._CP',             # 0E
        'ED6_DT07/CH00074P._CP',             # 0F
        'ED6_DT07/CH00033P._CP',             # 10
        'ED6_DT07/CH00073P._CP',             # 11
        'ED6_DT06/CH20021P._CP',             # 12
        'ED6_DT27/CH03085P._CP',             # 13
        'ED6_DT27/CH03091P._CP',             # 14
        'ED6_DT26/CH20415P._CP',             # 15
    )

    DeclNpc(
        X                   = -4460,
        Z                   = 0,
        Y                   = 960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 1966096,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 4970,
        TriggerZ            = 0,
        TriggerY            = -1040,
        TriggerRange        = 1400,
        ActorX              = 4970,
        ActorZ              = 2000,
        ActorY              = -1040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2BE",          # 00, 0
        "Function_1_3F8",          # 01, 1
        "Function_2_405",          # 02, 2
        "Function_3_582",          # 03, 3
        "Function_4_602",          # 04, 4
        "Function_5_664",          # 05, 5
        "Function_6_6AC",          # 06, 6
        "Function_7_6F2",          # 07, 7
        "Function_8_73A",          # 08, 8
        "Function_9_782",          # 09, 9
        "Function_10_7C8",         # 0A, 10
        "Function_11_80A",         # 0B, 11
        "Function_12_2D66",        # 0C, 12
        "Function_13_2DB5",        # 0D, 13
        "Function_14_2E04",        # 0E, 14
        "Function_15_2E53",        # 0F, 15
        "Function_16_2E83",        # 10, 16
        "Function_17_2EC0",        # 11, 17
        "Function_18_2EFD",        # 12, 18
        "Function_19_2F4F",        # 13, 19
        "Function_20_2F88",        # 14, 20
        "Function_21_2FBD",        # 15, 21
        "Function_22_2FFE",        # 16, 22
        "Function_23_303F",        # 17, 23
        "Function_24_3079",        # 18, 24
        "Function_25_30A9",        # 19, 25
        "Function_26_30CF",        # 1A, 26
        "Function_27_3156",        # 1B, 27
    )


    def Function_0_2BE(): pass

    label("Function_0_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_3C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_2E2")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -5450, 0, 310, 0)

    label("loc_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_310")
    OP_4A(0xB, 255)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 54780, 200, -3510, 90)
    SetChrChipByIndex(0xB, 11)
    Jump("loc_334")

    label("loc_310")

    OP_4A(0xA, 255)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 54780, 200, -3510, 90)
    SetChrChipByIndex(0xA, 10)

    label("loc_334")

    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xF, 0x4)
    SetChrPos(0xC, 57160, 200, -5120, 270)
    SetChrPos(0xD, 60800, 0, 2300, 0)
    SetChrPos(0xE, 58950, 0, 2510, 180)
    SetChrPos(0xF, 54780, 200, -5080, 90)
    SetChrChipByIndex(0xC, 12)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 14)
    SetChrChipByIndex(0xF, 15)
    OP_4A(0x8, 255)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 0)

    label("loc_3C5")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3D1"),
        (SWITCH_DEFAULT, "loc_3F7"),
    )


    label("loc_3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x2000000)
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_3F4")

    Jump("loc_3F7")

    label("loc_3F7")

    Return()

    # Function_0_2BE end

    def Function_1_3F8(): pass

    label("Function_1_3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_404")
    OP_72(0x5, 0x4)

    label("loc_404")

    Return()

    # Function_1_3F8 end

    def Function_2_405(): pass

    label("Function_2_405")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_56C")

    label("loc_42A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_443")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_56C")

    label("loc_443")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_56C")

    label("loc_45C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_475")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_56C")

    label("loc_475")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_56C")

    label("loc_48E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A7")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_56C")

    label("loc_4A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C0")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_56C")

    label("loc_4C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_56C")

    label("loc_4D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F2")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_56C")

    label("loc_4F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_56C")

    label("loc_50B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_524")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_56C")

    label("loc_524")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53D")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_56C")

    label("loc_53D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_556")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_56C")

    label("loc_556")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_56C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_581")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_56C")

    label("loc_581")

    Return()

    # Function_2_405 end

    def Function_3_582(): pass

    label("Function_3_582")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_5C3")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #0
        "\x07\x05艾南倒下睡着了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_5FE")

    label("loc_5C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_5FE")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #1
        "\x07\x05艾南倒下睡着了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_5FE")

    TalkEnd(0x8)
    Return()

    # Function_3_582 end

    def Function_4_602(): pass

    label("Function_4_602")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        (
            "#720F艾丝蒂尔大人，各位的看护\x01",
            "请交给我菲利普吧。\x02\x03",

            "公爵阁下的事，\x01",
            "就请你们多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_602 end

    def Function_5_664(): pass

    label("Function_5_664")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        (
            "\x07\x05雪拉扎德在桌子上\x01",
            "趴着睡着了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFE)
    Return()

    # Function_5_664 end

    def Function_6_6AC(): pass

    label("Function_6_6AC")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #4
        (
            "\x07\x05阿加特在桌子上\x01",
            "趴着睡着了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFE)
    Return()

    # Function_6_6AC end

    def Function_7_6F2(): pass

    label("Function_7_6F2")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #5
        (
            "\x07\x05奥利维尔在桌子上\x01",
            "趴着睡着了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFE)
    Return()

    # Function_7_6F2 end

    def Function_8_73A(): pass

    label("Function_8_73A")

    TalkBegin(0xD)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #6
        (
            "\x07\x05科洛丝在书架旁\x01",
            "倚靠着睡着了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xD)
    Return()

    # Function_8_73A end

    def Function_9_782(): pass

    label("Function_9_782")

    TalkBegin(0xE)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #7
        (
            "\x07\x05提妲在书架旁\x01",
            "倚靠着睡着了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xE)
    Return()

    # Function_9_782 end

    def Function_10_7C8(): pass

    label("Function_10_7C8")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #8
        (
            "\x07\x05金在桌子上\x01",
            "趴着睡着了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFE)
    Return()

    # Function_10_7C8 end

    def Function_11_80A(): pass

    label("Function_11_80A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81D")
    Call(0, 26)

    label("loc_81D")

    OP_4A(0x8, 255)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x143, 0x80)
    SetChrFlags(0xF7, 0x80)
    OP_6D(30, -250, -5270, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x5, 0x4)
    FadeToBright(1500, 0)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0xC)
    Sleep(800)
    OP_43(0x109, 0x1, 0x0, 0xD)
    Sleep(800)
    OP_43(0x143, 0x1, 0x0, 0xE)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #9
        0x101,
        "#1011F艾南先生，我们回来……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x7D0)
    OP_6D(-4460, 0, 960, 2000)
    Sleep(1000)
    Fade(1000)
    OP_6D(-2420, 0, -1880, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(277, 0)
    OP_0D()
    OP_1D(0x51)

    ChrTalk(    #10
        0x101,
        "#1020F#5P艾、艾南先生！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x143,
        "#721F怎么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        "#1069F哼，来这套啊！\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0x143, 0x1, 0x0, 0x11)
    Sleep(200)
    OP_43(0x109, 0x1, 0x0, 0x10)

    def lambda_9D5():
        OP_6D(-5430, 0, 690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9D5)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #13
        0x101,
        (
            "#1020F#5P艾南先生！？\x01",
            "艾南先生！\x02",
        )
    )

    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x101, 0x2)
    Fade(250)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 3)
    OP_0D()
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #14
        0x109,
        (
            "#1067F呼吸还很平稳……\x01",
            "看来是睡着了吧。\x02\x03",

            "#1063F这个人就是王都支部的接待吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1026F嗯、嗯……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 135, 400)

    ChrTalk(    #16
        0x101,
        "#1020F……大家！？\x02",
    )

    CloseMessageWindow()

    def lambda_AE3():

        label("loc_AE3")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_AE3")

    QueueWorkItem2(0x143, 2, lambda_AE3)
    OP_8E(0x101, 0xFFFFEF7A, 0x0, 0xFFFFF4FC, 0x1770, 0x0)

    def lambda_B08():
        OP_6D(-1050, 0, 3360, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B08)
    OP_8E(0x101, 0xFFFFFC18, 0x0, 0xFFFFF4B6, 0x1770, 0x0)
    OP_8E(0x101, 0x10AE, 0x0, 0x1202, 0x1770, 0x0)
    OP_8E(0x101, 0xFFFFF2A4, 0xDAC, 0x1388, 0x1770, 0x0)
    Fade(1000)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 56220, 600, -3080, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B9F")
    OP_4A(0xB, 255)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 54780, 200, -3510, 90)
    SetChrChipByIndex(0xB, 11)
    Jump("loc_BC3")

    label("loc_B9F")

    OP_4A(0xA, 255)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 54780, 200, -3510, 90)
    SetChrChipByIndex(0xA, 10)

    label("loc_BC3")

    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 65535)
    OP_44(0x143, 0x2)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xF, 0x4)
    SetChrPos(0xC, 57160, 200, -5120, 270)
    SetChrPos(0xD, 60800, 0, 2300, 0)
    SetChrPos(0xE, 58950, 0, 2510, 180)
    SetChrPos(0xF, 54780, 200, -5080, 90)
    SetChrChipByIndex(0xC, 12)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 14)
    SetChrChipByIndex(0xF, 15)
    OP_6D(56580, 0, -270, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_43(0x101, 0x1, 0x0, 0x17)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #17
        0x101,
        "#1020F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_CB9():
        OP_6D(54530, 0, -560, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CB9)
    OP_8E(0x101, 0xD624, 0x0, 0xFFFFFAEC, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D17")

    ChrTalk(    #18
        0x101,
        "#1020F#5P阿加特、奥利维尔、金先生！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D40")

    label("loc_D17")


    ChrTalk(    #19
        0x101,
        "#1020F#5P雪拉姐、奥利维尔、金先生！\x02",
    )

    CloseMessageWindow()

    label("loc_D40")

    OP_8C(0x101, 45, 600)
    Sleep(500)

    def lambda_D52():
        OP_6D(57790, 0, 1880, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D52)
    OP_8E(0x101, 0xE8E4, 0x0, 0x38E, 0xFA0, 0x0)
    TurnDirection(0x101, 0xE, 400)
    Sleep(500)
    TurnDirection(0x101, 0xD, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #20
        0x101,
        "#1020F#6P提妲、科洛丝！\x02",
    )

    CloseMessageWindow()
    OP_43(0x109, 0x1, 0x0, 0x12)
    Sleep(800)
    OP_43(0x143, 0x1, 0x0, 0x13)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #21
        0x109,
        (
            "#1068F#6P糟糕……\x01",
            "看来全员都中招了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    WaitChrThread(0x143, 0x1)
    OP_43(0x143, 0x1, 0x0, 0x14)
    Sleep(400)
    OP_8E(0x109, 0xE47A, 0x0, 0x348, 0xBB8, 0x0)
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #22
        0x109,
        "#1063F#5P怎样，没事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1026F#6P嗯、嗯……\x01",
            "好像都睡着了……\x02\x03",

            "#1007F到底大家，\x01",
            "这是怎么了啊～！？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x143, 0x1)

    def lambda_EAA():

        label("loc_EAA")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_EAA")

    QueueWorkItem2(0x143, 1, lambda_EAA)
    Sleep(500)

    ChrTalk(    #24
        0x143,
        (
            "#720F#5P唔，看来是\x01",
            "中招了啊。\x02\x03",

            "大家看起来像突然被睡魔袭击\x01",
            "一样倒地不起了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 315, 400)

    ChrTalk(    #25
        0x101,
        "#1015F#6P确、确实……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)

    ChrTalk(    #26
        0x109,
        "#1064F#6P哦哦，真敏锐。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x11, 400)
    Sleep(1000)

    def lambda_F7E():

        label("loc_F7E")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_F7E")

    QueueWorkItem2(0x109, 1, lambda_F7E)

    def lambda_F8F():
        OP_6D(56030, 0, 20, 1500)
        ExitThread()

    QueueWorkItem(0x143, 2, lambda_F8F)
    OP_8E(0x101, 0xDBE2, 0x0, 0xFFFFF70E, 0xBB8, 0x0)
    TurnDirection(0x101, 0x11, 400)
    WaitChrThread(0x143, 0x2)
    WaitChrThread(0x143, 0x3)

    ChrTalk(    #27
        0x101,
        "#1004F#5P咦，这封信……\x02",
    )

    CloseMessageWindow()
    OP_44(0x109, 0x1)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1009():
        OP_8E(0xFE, 0xDDCC, 0x0, 0xFFFFFC86, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1009)
    WaitChrThread(0x109, 0x0)
    TurnDirection(0x109, 0x11, 400)

    ChrTalk(    #28
        0x109,
        (
            "#1064F#2P等一下……\x02\x03",

            "这个，和我们收到的\x01",
            "信封不是一样的吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1020F#6P嗯、嗯！\x02",
    )

    CloseMessageWindow()
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0x11, 0x80)
    Sleep(500)
    TurnDirection(0x101, 0x109, 400)
    Sleep(500)
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(200)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x05艾丝蒂尔打开信封确认了信的内容。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240097, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "\x07\x05小女孩和公爵在我们手上。\x02\x03",

            "想要回他们的话，\x01",
            "就请参加『茶会』吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #32
        0x101,
        "#1005F#6P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x143,
        "#721F#8P公、公爵阁下……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        (
            "#1065F#2P茶会的地点\x01",
            "果然还是王都吗……\x02\x03",

            "#1063F这里写的\x01",
            "女孩是谁，知道吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #35
        0x101,
        "#1004F#6P啊……！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 600)
    Sleep(500)
    OP_8C(0x101, 90, 600)
    Sleep(500)

    ChrTalk(    #36
        0x101,
        (
            "#1020F#5P玲！？\x02\x03",

            "玲，你在哪儿！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1273():

        label("loc_1273")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_1273")

    QueueWorkItem2(0x109, 1, lambda_1273)

    def lambda_1284():
        OP_6D(63130, 0, 4190, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1284)
    OP_8E(0x101, 0xFB22, 0x0, 0x140, 0x1770, 0x0)
    OP_8E(0x101, 0xFC4E, 0x7D0, 0x1284, 0x1770, 0x0)
    OP_8E(0x101, 0xF0D2, 0xF0A, 0x1284, 0x1770, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x143, 0x1)
    Fade(1000)
    OP_6D(119700, 0, 4700, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 125400, -2000, 4700, 270)
    OP_8E(0x101, 0x1D394, 0x0, 0x125C, 0x1388, 0x0)
    OP_69(0x101, 0x0)

    def lambda_134E():

        label("loc_134E")

        OP_69(0x101, 0x0)
        OP_48()
        Jump("loc_134E")

    QueueWorkItem2(0x101, 1, lambda_134E)
    OP_8E(0x101, 0x1D394, 0x0, 0xFFFFFA92, 0x1388, 0x0)
    OP_8C(0x101, 270, 600)
    Sleep(500)
    OP_8C(0x101, 90, 600)
    Sleep(500)
    OP_43(0x109, 0x1, 0x0, 0x15)
    OP_8C(0x101, 180, 600)
    Sleep(500)
    OP_44(0x101, 0x1)
    Sleep(300)
    OP_43(0x143, 0x1, 0x0, 0x16)

    def lambda_13AE():
        OP_6D(119410, 0, -320, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13AE)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #37
        0x109,
        (
            "#1063F#2P看来是把那孩子\x01",
            "掳走了啊……\x02\x03",

            "艾丝蒂尔的朋友吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #38
        0x101,
        (
            "#1026F#6P不，是因为某些原因\x01",
            "暂时照看的孩子……\x02\x03",

            "#1027F居然偏偏\x01",
            "被卷进这种事……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x109,
        "#1067F#2P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x143,
        "#722F艾丝蒂尔大人……\x02",
    )

    CloseMessageWindow()
    OP_61(0x101)

    ChrTalk(    #41
        0x101,
        (
            "#1003F#6P对不起，菲利普先生……\x02\x03",

            "说不定公爵\x01",
            "也是受连累的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x143,
        (
            "#720F不，这不一定。\x02\x03",

            "即便是这样\x01",
            "到这时候还一个人\x01",
            "到处转悠的阁下也有责任。\x02\x03",

            "请别这么自责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x109,
        (
            "#1063F#2P对啊，艾丝蒂尔。\x02\x03",

            "首先要去追查\x01",
            "信中所说的茶会才是啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1002F#6P嗯、嗯……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(200)
    Sleep(200)
    FadeToDark(300, 0, 100)
    OP_AD(0x240097, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetChrName("")
    SetMessageWindowPos(-1, 300, -1, 3)

    AnonymousTalk(    #45
        (
            "\x07\x05小女孩和公爵在我们手上。\x02\x03",

            "想要回他们的话，\x01",
            "就请参加『茶会』吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1500)
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #46
        0x101,
        (
            "#1015F#6P这么说来茶会这话\x01",
            "好像在谈到特务兵余党的时候\x01",
            "艾南先生说过似的……\x02\x03",

            "#1004F……对了，凯文先生。\x02\x03",

            "刚才读信的时候，\x01",
            "你是不是说了句\x01",
            "果然还是在王都吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        (
            "#1064F#2P怎么，你听到了啊。\x02\x03",

            "#1066F嗯～其实是\x01",
            "有点内情的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2249")
    SetChrPos(0xA, 125400, 0, 4700, 270)

    NpcTalk(    #48
        0xA,
        "女性的声音",
        (
            "#5P……这个内情\x01",
            "让我来说明吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_4A(0xA, 255)
    SetChrChipByIndex(0xA, 2)
    SetChrPos(0xA, 125400, -2000, 4700, 270)
    ClearChrFlags(0xA, 0x80)

    def lambda_17BF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17BF)

    def lambda_17CD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x143, 1, lambda_17CD)

    def lambda_17DB():
        OP_6D(118950, 0, 1040, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17DB)
    OP_8E(0xA, 0x1D394, 0x0, 0x125C, 0xBB8, 0x0)
    OP_8E(0xA, 0x1D394, 0x0, 0x6EA, 0xBB8, 0x0)

    ChrTalk(    #49
        0x109,
        "#1062F#6P哦，时机正好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1004F#6P啊……\x02\x03",

            "雪，雪拉姐！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "#027F好久不见了，艾丝蒂尔。\x02\x03",

            "好像发生了\x01",
            "很严重的事嘛？\x02\x03",

            "#025F不过凯文先生。\x01",
            "我们彼此都没赶上呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x109,
        "#1068F#6P嗯嗯，真没面子啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1020F#6P为、为什么\x01",
            "雪拉姐会在这里……\x02\x03",

            "而且，为什么能和凯文先生\x01",
            "这么自然的说话！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "#020F我和亚妮拉丝\x01",
            "发现了特务兵的大本营\x01",
            "这你可能听说了……\x02\x03",

            "就在那时，\x01",
            "认识了这个人的。\x02\x03",

            "在搜索消失的余党上\x01",
            "现在还要请他帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1025F#6P是、是吗……\x01",
            "所以才这么清楚状况啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x109,
        "#1060F#5P嘿嘿，就是这样。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10, 125400, 0, 4700, 270)

    NpcTalk(    #57
        0x10,
        "女孩的声音",
        "#5P雪拉前辈！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x10, 400)

    def lambda_1A49():

        label("loc_1A49")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_1A49")

    QueueWorkItem2(0xA, 1, lambda_1A49)
    SetChrPos(0x10, 125400, -2000, 4700, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 20)
    OP_8E(0x10, 0x1D394, 0x0, 0x125C, 0x1388, 0x0)
    OP_8E(0x10, 0x1D77C, 0x0, 0x672, 0x1388, 0x0)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 0)
    OP_44(0xA, 0x1)

    ChrTalk(    #58
        0x101,
        "#1004F#6P啊，亚妮拉丝！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "#811F#2P艾丝蒂尔！\x01",
            "太好了，你没事啊！\x02\x03",

            "#1310F还有凯文先生\x01",
            "也来了这边啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x109,
        (
            "#1060F#6P啊啊，我也\x01",
            "没赶上啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        "#020F#5P对了，下面的通信器怎么样了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xA, 400)

    ChrTalk(    #62
        0x10,
        (
            "#1316F#4P不行……\x01",
            "好像被拿走了零件\x01",
            "无法马上使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        "#026F#5P这么说来……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 225, 500)

    def lambda_1BC7():

        label("loc_1BC7")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1BC7")

    QueueWorkItem2(0x101, 1, lambda_1BC7)

    def lambda_1BD8():

        label("loc_1BD8")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1BD8")

    QueueWorkItem2(0x109, 1, lambda_1BD8)

    def lambda_1BE9():

        label("loc_1BE9")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1BE9")

    QueueWorkItem2(0x143, 1, lambda_1BE9)

    def lambda_1BFA():

        label("loc_1BFA")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1BFA")

    QueueWorkItem2(0x10, 1, lambda_1BFA)
    OP_8E(0xA, 0x1CB6A, 0x0, 0x19A, 0xBB8, 0x0)

    def lambda_1C1F():
        OP_6D(116400, 0, 3390, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C1F)

    def lambda_1C37():
        OP_67(0, 3500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1C37)

    def lambda_1C4F():
        OP_6B(3140, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1C4F)

    def lambda_1C5F():
        OP_6E(306, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1C5F)
    OP_8E(0xA, 0x1BFDA, 0xFA, 0x230, 0xBB8, 0x0)
    OP_8E(0xA, 0x1C14C, 0xFA, 0x12F2, 0xBB8, 0x0)
    Sleep(1000)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0x143, 0x1)
    OP_44(0x10, 0x1)

    ChrTalk(    #64
        0xA,
        "#522F#6P不行，这边也一样。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(118020, 0, 400, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(315000, 0)
    OP_6E(306, 0)
    OP_8C(0xA, 180, 400)
    OP_43(0xA, 0x0, 0x0, 0x18)
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0x19)

    def lambda_1D2D():

        label("loc_1D2D")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1D2D")

    QueueWorkItem2(0x101, 1, lambda_1D2D)

    def lambda_1D3E():

        label("loc_1D3E")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1D3E")

    QueueWorkItem2(0x109, 1, lambda_1D3E)

    def lambda_1D4F():

        label("loc_1D4F")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1D4F")

    QueueWorkItem2(0x143, 1, lambda_1D4F)
    WaitChrThread(0xA, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0x143, 0x1)
    OP_44(0x10, 0x1)

    ChrTalk(    #65
        0x101,
        (
            "#1002F这么说……\x01",
            "是敌人破坏的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#022F#5P不会错的。\x02\x03",

            "到底是为了什么\x01",
            "要做这种事……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x101,
        (
            "#1004F对了，雪拉姐！\x01",
            "这个留下的信……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #68
        (
            "\x07\x05艾丝蒂尔给雪拉扎德等人\x01",
            "说明了之前发现信的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #69
        0xA,
        (
            "#026F#5P茶会……\x01",
            "总算全部连接起来了。\x02\x03",

            "#022F掳走那孩子和公爵的\x01",
            "是特务兵的余党没错。\x02\x03",

            "而且背后\x01",
            "应该是『噬身之蛇』在搞鬼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1026F嗯，我们也\x01",
            "被奇怪的机械袭击了……\x02\x03",

            "但是参加茶会\x01",
            "应该去哪里才好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "#026F#5P总之只有去想得到的地方\x01",
            "找找看了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 45, 400)
    Sleep(400)

    ChrTalk(    #72
        0xA,
        (
            "#020F#5P亚妮拉丝。\x01",
            "能不能拜托你件事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        "#814F好，什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "#022F#5P希望你去艾尔贝离宫的警备本部\x01",
            "联络一下这个情况。\x02\x03",

            "出现在周游道上的武装集团\x01",
            "恐怕是表面佯攻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1002F原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x109,
        "#1063F#4P果然真正目的是王都啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10,
        (
            "#816F明白了！\x02\x03",

            "那么我立刻\x01",
            "冲去离宫！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #78
        0x101,
        "#1002F亚妮拉丝，小心啊！\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #79
        0x10,
        "#811F嗯，艾丝蒂尔也是！\x02",
    )

    CloseMessageWindow()

    def lambda_20DC():

        label("loc_20DC")

        TurnDirection(0x109, 0x10, 400)
        OP_48()
        Jump("loc_20DC")

    QueueWorkItem2(0x109, 0, lambda_20DC)

    def lambda_20ED():

        label("loc_20ED")

        TurnDirection(0x143, 0x10, 400)
        OP_48()
        Jump("loc_20ED")

    QueueWorkItem2(0x143, 0, lambda_20ED)
    OP_8C(0x10, 0, 400)

    def lambda_2105():
        OP_6D(119000, 0, 1990, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2105)
    SetChrChipByIndex(0x10, 20)
    OP_8E(0x10, 0x1D394, 0x0, 0x125C, 0x1388, 0x0)
    OP_8E(0x10, 0x1E9D8, 0xFFFFF830, 0x125C, 0x1388, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    def lambda_2154():
        OP_6D(118020, 0, 400, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2154)
    OP_8C(0xA, 90, 400)

    def lambda_2173():
        OP_8C(0x101, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2173)
    Sleep(50)

    def lambda_2186():
        OP_8C(0x109, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2186)
    Sleep(50)

    def lambda_2199():
        OP_8C(0x143, 270, 400)
        ExitThread()

    QueueWorkItem(0x143, 0, lambda_2199)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #80
        0xA,
        (
            "#020F#5P管家先生，不好意思\x01",
            "你能在协会待命吗？\x02\x03",

            "我们一定会找回公爵阁下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x143,
        (
            "#720F#4P……明白了。\x02\x03",

            "待命期间，就让我\x01",
            "负责各位的护理吧。\x02\x03",

            "阁下就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4E")

    label("loc_2249")

    SetChrPos(0xB, 125400, 0, 4700, 270)

    NpcTalk(    #82
        0xB,
        "青年的声音",
        (
            "#5P……这个内情\x01",
            "让我来说明吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_4A(0xB, 255)
    SetChrChipByIndex(0xB, 3)
    SetChrPos(0xB, 125400, -2000, 4700, 270)
    ClearChrFlags(0xB, 0x80)

    def lambda_22CA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_22CA)

    def lambda_22D8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x143, 1, lambda_22D8)

    def lambda_22E6():
        OP_6D(118950, 0, 1040, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22E6)
    OP_8E(0xB, 0x1D394, 0x0, 0x125C, 0xBB8, 0x0)
    OP_8E(0xB, 0x1D394, 0x0, 0x6EA, 0xBB8, 0x0)

    ChrTalk(    #83
        0x109,
        "#1062F#6P哦，时机正好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1004F#6P啊……\x02\x03",

            "阿、阿、阿加特！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xB,
        (
            "#051F好久不见了啊，艾丝蒂尔。\x02\x03",

            "事情变得\x01",
            "相当麻烦了嘛。\x02\x03",

            "#053F不过凯文。\x01",
            "我们彼此都没赶上啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x109,
        "#1068F#6P嗯嗯，真没面子啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1020F#6P为、为什么\x01",
            "阿加特会在这里……\x02\x03",

            "而且，为什么能和凯文先生\x01",
            "说得通话！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xB,
        (
            "#051F我和亚妮拉丝\x01",
            "发现了特务兵的大本营\x01",
            "这你听艾南说过吧？\x02\x03",

            "和这个不良神父\x01",
            "就是那时候认识的。\x02\x03",

            "在搜索消失的余党上\x01",
            "现在还要请他帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1025F#6P是、是吗……\x01",
            "所以才这么清楚状况啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x109,
        "#1060F#5P嘿嘿，就是这样。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10, 125400, 0, 4700, 270)

    NpcTalk(    #91
        0x10,
        "女孩的声音",
        "#5P阿加特前辈！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x10, 400)

    def lambda_2556():

        label("loc_2556")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_2556")

    QueueWorkItem2(0xB, 1, lambda_2556)
    SetChrPos(0x10, 125400, -2000, 4700, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 20)
    OP_8E(0x10, 0x1D394, 0x0, 0x125C, 0x1388, 0x0)
    OP_8E(0x10, 0x1D77C, 0x0, 0x672, 0x1388, 0x0)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 0)
    OP_44(0xB, 0x1)

    ChrTalk(    #92
        0x101,
        "#1004F#6P啊，亚妮拉丝！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10,
        (
            "#811F#2P艾丝蒂尔！\x01",
            "太好了，你没事啊！\x02\x03",

            "#1310F还有凯文先生\x01",
            "也来了这边啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x109,
        (
            "#1060F#6P啊啊，我也\x01",
            "没赶上啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xB,
        "#050F#5P对了，下面的通信器怎么样？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xB, 400)

    ChrTalk(    #96
        0x10,
        (
            "#1316F#4P不行……\x01",
            "好像被拿走了零件\x01",
            "无法马上使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xB,
        "#552F#5P是吗……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 225, 500)

    def lambda_26CE():

        label("loc_26CE")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_26CE")

    QueueWorkItem2(0x101, 1, lambda_26CE)

    def lambda_26DF():

        label("loc_26DF")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_26DF")

    QueueWorkItem2(0x109, 1, lambda_26DF)

    def lambda_26F0():

        label("loc_26F0")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_26F0")

    QueueWorkItem2(0x143, 1, lambda_26F0)

    def lambda_2701():

        label("loc_2701")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2701")

    QueueWorkItem2(0x10, 1, lambda_2701)
    OP_8E(0xB, 0x1CB6A, 0x0, 0x19A, 0xBB8, 0x0)

    def lambda_2726():
        OP_6D(116400, 0, 3390, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2726)

    def lambda_273E():
        OP_67(0, 3500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_273E)

    def lambda_2756():
        OP_6B(3140, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2756)

    def lambda_2766():
        OP_6E(306, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2766)
    OP_8E(0xB, 0x1BFDA, 0xFA, 0x230, 0xBB8, 0x0)
    OP_8E(0xB, 0x1C14C, 0xFA, 0x12F2, 0xBB8, 0x0)
    Sleep(1000)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0x143, 0x1)
    OP_44(0x10, 0x1)

    ChrTalk(    #98
        0xB,
        "#555F#6P哼，这边也一样。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(118020, 0, 400, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(315000, 0)
    OP_6E(306, 0)
    OP_8C(0xB, 180, 400)
    OP_43(0xB, 0x0, 0x0, 0x18)
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0x19)

    def lambda_2832():

        label("loc_2832")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2832")

    QueueWorkItem2(0x101, 1, lambda_2832)

    def lambda_2843():

        label("loc_2843")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2843")

    QueueWorkItem2(0x109, 1, lambda_2843)

    def lambda_2854():

        label("loc_2854")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2854")

    QueueWorkItem2(0x143, 1, lambda_2854)
    WaitChrThread(0xB, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0x143, 0x1)
    OP_44(0x10, 0x1)

    ChrTalk(    #99
        0x101,
        (
            "#1002F这么说……\x01",
            "是敌人破坏的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xB,
        (
            "#050F#5P没错吧。\x02\x03",

            "问题是到底为了什么\x01",
            "做这种事……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #101
        0x101,
        (
            "#1004F对了，阿加特！\x01",
            "这个留下的信……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #102
        (
            "\x07\x05艾丝蒂尔对阿加特等人\x01",
            "说明了之前发现信的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #103
        0xB,
        (
            "#053F#5P茶会……\x01",
            "总算全部连接起来了。\x02\x03",

            "#057F掳走那孩子和公爵的\x01",
            "肯定是特务兵的余党吧。\x02\x03",

            "而且背后\x01",
            "应该是『噬身之蛇』在搞鬼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1026F嗯，我们也\x01",
            "被奇怪的机械袭击了……\x02\x03",

            "但是参加茶会\x01",
            "应该去哪里才好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xB,
        (
            "#053F#5P总之只有去想得到的地方\x01",
            "从头找找看了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 45, 400)
    Sleep(400)

    ChrTalk(    #106
        0xB,
        "#050F#5P亚妮拉丝，有件事想拜托你。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        "#814F好，什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xB,
        (
            "#050F#5P去艾尔贝离宫的警备本部\x01",
            "联络一下这个情况。\x02\x03",

            "出现在周游道上的武装集团\x01",
            "恐怕是表面佯攻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1002F原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x109,
        "#1063F#4P果然真正目的是王都啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x10,
        (
            "#816F明白了！\x02\x03",

            "那么我立刻\x01",
            "冲去离宫！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)
    Sleep(400)

    ChrTalk(    #112
        0x101,
        "#1002F亚妮拉丝，小心啊！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #113
        0x10,
        "#811F嗯，艾丝蒂尔也是！\x02",
    )

    CloseMessageWindow()

    def lambda_2BDE():

        label("loc_2BDE")

        TurnDirection(0x109, 0x10, 400)
        OP_48()
        Jump("loc_2BDE")

    QueueWorkItem2(0x109, 0, lambda_2BDE)

    def lambda_2BEF():

        label("loc_2BEF")

        TurnDirection(0x143, 0x10, 400)
        OP_48()
        Jump("loc_2BEF")

    QueueWorkItem2(0x143, 0, lambda_2BEF)
    OP_8C(0x10, 0, 400)

    def lambda_2C07():
        OP_6D(119000, 0, 1990, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C07)
    SetChrChipByIndex(0x10, 20)
    OP_8E(0x10, 0x1D394, 0x0, 0x125C, 0x1388, 0x0)
    OP_8E(0x10, 0x1E9D8, 0xFFFFF830, 0x125C, 0x1388, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    def lambda_2C56():
        OP_6D(118020, 0, 400, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C56)
    OP_8C(0xB, 90, 400)

    def lambda_2C75():
        OP_8C(0x101, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C75)
    Sleep(50)

    def lambda_2C88():
        OP_8C(0x109, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2C88)
    Sleep(50)

    def lambda_2C9B():
        OP_8C(0x143, 270, 400)
        ExitThread()

    QueueWorkItem(0x143, 0, lambda_2C9B)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #114
        0xB,
        (
            "#050F#5P记得你是菲利普吧。\x02\x03",

            "不好意思\x01",
            "你就待在协会待命吧。\x02\x03",

            "我们一定找回公爵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x143,
        (
            "#720F#4P……明白了。\x02\x03",

            "待命期间，就让我\x01",
            "负责各位的护理吧。\x02\x03",

            "阁下就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D4E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4310   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_11_80A end

    def Function_12_2D66(): pass

    label("Function_12_2D66")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 90, -500, -7250, 0)

    def lambda_2D8D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D8D)
    OP_8E(0xFE, 0xFFFFFFEC, 0xFFFFFF7E, 0xFFFFEEA8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_12_2D66 end

    def Function_13_2DB5(): pass

    label("Function_13_2DB5")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 90, -500, -7250, 0)

    def lambda_2DDC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DDC)
    OP_8E(0xFE, 0x442, 0xFFFFFF7E, 0xFFFFEE94, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_13_2DB5 end

    def Function_14_2E04(): pass

    label("Function_14_2E04")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 90, -500, -7250, 0)

    def lambda_2E2B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E2B)
    OP_8E(0xFE, 0xFFFFFFD8, 0xFFFFFF06, 0xFFFFEA5C, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_14_2E04 end

    def Function_15_2E53(): pass

    label("Function_15_2E53")

    OP_8E(0xFE, 0xFFFFEE80, 0x0, 0xFFFFF47A, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFE9BC, 0x0, 0x26C, 0x1388, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_15_2E53 end

    def Function_16_2E83(): pass

    label("Function_16_2E83")

    OP_8E(0xFE, 0xFFFFF5CE, 0x0, 0xFFFFF2F4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFECC8, 0x0, 0xFFFFF36C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFED86, 0x0, 0x0, 0xFA0, 0x0)
    Return()

    # Function_16_2E83 end

    def Function_17_2EC0(): pass

    label("Function_17_2EC0")

    OP_8E(0xFE, 0xFFFFF5CE, 0x0, 0xFFFFF2F4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFECC8, 0x0, 0xFFFFF36C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFE99E, 0x0, 0xFFFFFC0E, 0xFA0, 0x0)
    Return()

    # Function_17_2EC0 end

    def Function_18_2EFD(): pass

    label("Function_18_2EFD")

    SetChrPos(0xFE, 60250, -2000, 4530, 270)
    OP_8E(0xFE, 0xD746, 0x0, 0x128E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xD764, 0x0, 0x744, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_18_2EFD end

    def Function_19_2F4F(): pass

    label("Function_19_2F4F")

    SetChrPos(0xFE, 60250, -2000, 4530, 270)
    OP_8E(0xFE, 0xD746, 0x0, 0x128E, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    TurnDirection(0xFE, 0xE, 400)
    Return()

    # Function_19_2F4F end

    def Function_20_2F88(): pass

    label("Function_20_2F88")

    Sleep(1000)
    OP_8E(0xFE, 0xD764, 0x0, 0xA3C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xE15A, 0x0, 0xA3C, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xE, 400)
    Return()

    # Function_20_2F88 end

    def Function_21_2FBD(): pass

    label("Function_21_2FBD")

    SetChrPos(0xFE, 125400, -2000, 4700, 270)
    OP_8E(0xFE, 0x1D394, 0x0, 0x125C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1D61E, 0x0, 0xFFFFFF6A, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_21_2FBD end

    def Function_22_2FFE(): pass

    label("Function_22_2FFE")

    SetChrPos(0xFE, 125400, -2000, 4700, 270)
    OP_8E(0xFE, 0x1D394, 0x0, 0x125C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1D1C8, 0x0, 0xFFFFFF4C, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_22_2FFE end

    def Function_23_303F(): pass

    label("Function_23_303F")

    SetChrPos(0xFE, 58740, -2000, 4560, 270)
    OP_8E(0xFE, 0xD6B0, 0x0, 0x1310, 0x1388, 0x0)
    OP_8E(0xFE, 0xD5C0, 0x0, 0xE42, 0x1388, 0x0)
    Return()

    # Function_23_303F end

    def Function_24_3079(): pass

    label("Function_24_3079")

    OP_8E(0xFE, 0x1BFDA, 0xFA, 0x230, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1C9BC, 0x0, 0xFFFFFE0C, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 500)
    Return()

    # Function_24_3079 end

    def Function_25_30A9(): pass

    label("Function_25_30A9")

    OP_8E(0xFE, 0x1D1B4, 0x0, 0x5DC, 0x7D0, 0x0)

    def lambda_30C3():

        label("loc_30C3")

        OP_8C(0xFE, 225, 400)
        OP_48()
        Jump("loc_30C3")

    QueueWorkItem2(0xFE, 1, lambda_30C3)
    Return()

    # Function_25_30A9 end

    def Function_26_30CF(): pass

    label("Function_26_30CF")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3149"),
        (1, "loc_314F"),
        (SWITCH_DEFAULT, "loc_3155"),
    )


    label("loc_3149")

    OP_A2(0x1200)
    Jump("loc_3155")

    label("loc_314F")

    OP_A2(0x1201)
    Jump("loc_3155")

    label("loc_3155")

    Return()

    # Function_26_30CF end

    def Function_27_3156(): pass

    label("Function_27_3156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3167")
    OP_2A(0xBD, 0xBE, 0xFFFF)
    Jump("loc_31B4")

    label("loc_3167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_317E")
    OP_2A(0xAA, 0xAC, 0xC4, 0xAB, 0xA9, 0xFFFF)
    Jump("loc_31B4")

    label("loc_317E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_3193")
    OP_2A(0xAA, 0xAC, 0xC4, 0xAB, 0xFFFF)
    Jump("loc_31B4")

    label("loc_3193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_31A6")
    OP_2A(0xAA, 0xAC, 0xC4, 0xFFFF)
    Jump("loc_31B4")

    label("loc_31A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_31B4")
    OP_2A(0xAA, 0xAC, 0xFFFF)

    label("loc_31B4")

    TalkEnd(0xFF)
    Return()

    # Function_27_3156 end

    SaveToFile()

Try(main)
