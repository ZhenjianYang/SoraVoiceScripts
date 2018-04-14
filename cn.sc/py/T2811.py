from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2811   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2811.x',
        MapIndex            = 1,
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '乔儿',                                 # 9
        '汉斯',                                 # 10
        '德波拉',                               # 11
        '目标用照相机',                         # 12
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH01130 ._CH',             # 02
        'ED6_DT07/CH02393 ._CH',             # 03
        'ED6_DT07/CH02553 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH01130P._CP',             # 02
        'ED6_DT07/CH02393P._CP',             # 03
        'ED6_DT07/CH02553P._CP',             # 04
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 3060,
        TriggerZ            = 0,
        TriggerY            = 2500,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_176",          # 00, 0
        "Function_1_18A",          # 01, 1
        "Function_2_1DD",          # 02, 2
        "Function_3_35A",          # 03, 3
        "Function_4_35F",          # 04, 4
        "Function_5_53F",          # 05, 5
        "Function_6_689",          # 06, 6
        "Function_7_81D",          # 07, 7
        "Function_8_841",          # 08, 8
        "Function_9_F33",          # 09, 9
        "Function_10_15C9",        # 0A, 10
    )


    def Function_0_176(): pass

    label("Function_0_176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_189")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_189")

    Return()

    # Function_0_176 end

    def Function_1_18A(): pass

    label("Function_1_18A")

    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x8, -1810, 300, -1250, 269)
    SetChrPos(0x9, -3520, 300, 200, 158)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    Return()

    # Function_1_18A end

    def Function_2_1DD(): pass

    label("Function_2_1DD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_202")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_344")

    label("loc_202")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_344")

    label("loc_21B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_234")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_344")

    label("loc_234")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_344")

    label("loc_24D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_266")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_344")

    label("loc_266")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_344")

    label("loc_27F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_298")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_344")

    label("loc_298")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B1")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_344")

    label("loc_2B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_344")

    label("loc_2CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_344")

    label("loc_2E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_344")

    label("loc_2FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_315")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_344")

    label("loc_315")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_344")

    label("loc_32E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_344")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_359")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_344")

    label("loc_359")

    Return()

    # Function_2_1DD end

    def Function_3_35A(): pass

    label("Function_3_35A")

    Call(0, 4)
    Return()

    # Function_3_35A end

    def Function_4_35F(): pass

    label("Function_4_35F")

    TalkBegin(0xA)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                               # 0
            "买东西\x01",                             # 1
            "招牌菜『大小姐料理』　800米拉\x01",      # 2
            "离开\x01",                               # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x72)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_3DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4B3")
    SubMira(800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06\x07\x02大小姐料理\x07\x00已经品尝过了。\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x4B0)
    OP_31(0x1, 0xFD, 0x4B0)
    OP_31(0x2, 0xFD, 0x4B0)
    OP_31(0x3, 0xFD, 0x4B0)
    OP_31(0x4, 0xFD, 0x4B0)
    OP_31(0x5, 0xFD, 0x4B0)
    OP_31(0x6, 0xFD, 0x4B0)
    OP_31(0x7, 0xFD, 0x4B0)
    OP_31(0x8, 0xFD, 0x4B0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x9)"), scpexpr(EXPR_END)), "loc_47B")
    Jump("loc_4A5")

    label("loc_47B")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06\x07\x02大小姐料理\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_4A5")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_4D9")

    label("loc_4B3")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_4D9")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xA)
    Return()

    label("loc_4EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_505")
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_505")

    FadeToBright(300, 0)

    ChrTalk(    #3
        0xA,
        "现在要去哪儿？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "外边很暗\x01",
            "要当心哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_4_35F end

    def Function_5_53F(): pass

    label("Function_5_53F")

    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_564")
    SetChrSubChip(0x8, 2)
    Jump("loc_595")

    label("loc_564")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57A")
    SetChrSubChip(0x8, 1)
    Jump("loc_595")

    label("loc_57A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_590")
    SetChrSubChip(0x8, 0)
    Jump("loc_595")

    label("loc_590")

    SetChrSubChip(0x8, 2)

    label("loc_595")

    OP_8C(0x8, 269, 0)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 2)), scpexpr(EXPR_END)), "loc_62A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5F0")

    ChrTalk(    #5
        0x8,
        (
            "#640F嗯～秘密的地下室啊。\x02\x03",

            "还有卡片的谜题\x01",
            "真令人开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_627")

    label("loc_5F0")

    OP_A2(0x0)

    ChrTalk(    #6
        0x8,
        (
            "#640F嗯～秘密的地下室啊。\x02\x03",

            "相当有趣\x01",
            "的发展嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_627")

    Jump("loc_680")

    label("loc_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_680")

    ChrTalk(    #7
        0x8,
        (
            "#640F我们就在这里等吧。\x01",
            "碍手碍脚就不好了。\x02\x03",

            "那么，当心。\x01",
            "期待冒险见闻哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_680")

    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_5_53F end

    def Function_6_689(): pass

    label("Function_6_689")

    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6AE")
    SetChrSubChip(0x9, 1)
    Jump("loc_6DF")

    label("loc_6AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6C4")
    SetChrSubChip(0x9, 0)
    Jump("loc_6DF")

    label("loc_6C4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6DA")
    SetChrSubChip(0x9, 2)
    Jump("loc_6DF")

    label("loc_6DA")

    SetChrSubChip(0x9, 0)

    label("loc_6DF")

    OP_8C(0x9, 172, 0)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 2)), scpexpr(EXPR_END)), "loc_7D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_747")

    ChrTalk(    #8
        0x9,
        (
            "#730F听说旧校舍是\x01",
            "由古老的城塞改建的，\x02\x03",

            "即使有秘密地下室\x01",
            "也不奇怪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D4")

    label("loc_747")

    OP_A2(0x1)

    ChrTalk(    #9
        0x9,
        (
            "#730F隐藏的楼梯吗……\x02\x03",

            "资料中也没有\x01",
            "记载那些东西啊。\x02\x03",

            "只是听说旧校舍是\x01",
            "以前的城塞改建的。\x02\x03",

            "即使有秘密地下室\x01",
            "所以即使如此也很正常吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D4")

    Jump("loc_814")

    label("loc_7D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_814")

    ChrTalk(    #10
        0x9,
        (
            "#730F在这种时候\x01",
            "先在原地待命吧。\x02\x03",

            "一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_814")

    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Return()

    # Function_6_689 end

    def Function_7_81D(): pass

    label("Function_7_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82E")
    Call(0, 10)

    label("loc_82E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_83C")
    Call(0, 8)
    Jump("loc_840")

    label("loc_83C")

    Call(0, 9)

    label("loc_840")

    Return()

    # Function_7_81D end

    def Function_8_841(): pass

    label("Function_8_841")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    SetChrPos(0x101, 240, 0, -2890, 225)
    SetChrPos(0xF7, 560, 0, -3920, 275)
    SetChrPos(0x105, -600, 0, -2190, 185)
    SetChrPos(0x104, -260, 0, -5270, 0)
    SetChrPos(0x127, -1510, 0, -5190, 45)
    SetChrPos(0x8, -1990, 0, -4400, 45)
    SetChrPos(0x9, -8610, 0, -3090, 90)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    OP_6D(1300, 0, 4690, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)

    def lambda_92E():
        OP_6D(-120, 0, -3010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_92E)

    def lambda_946():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_946)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_97C():

        label("loc_97C")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_97C")

    QueueWorkItem2(0x101, 1, lambda_97C)

    def lambda_98D():

        label("loc_98D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_98D")

    QueueWorkItem2(0xF7, 1, lambda_98D)

    def lambda_99E():

        label("loc_99E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_99E")

    QueueWorkItem2(0x105, 1, lambda_99E)

    def lambda_9AF():

        label("loc_9AF")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_9AF")

    QueueWorkItem2(0x104, 1, lambda_9AF)

    def lambda_9C0():

        label("loc_9C0")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_9C0")

    QueueWorkItem2(0x127, 1, lambda_9C0)

    def lambda_9D1():

        label("loc_9D1")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_9D1")

    QueueWorkItem2(0x8, 1, lambda_9D1)

    def lambda_9E2():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_9E2)

    def lambda_9F4():
        OP_8E(0xFE, 0xFFFFF63C, 0x0, 0xFFFFF36C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9F4)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #11
        0x9,
        (
            "#730F给，老师那里\x01",
            "借来的后门钥匙。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x9, 0x101, 0x3E8, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #12
        "\x1F\xF3\x03\x07\x00收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x3F3, 1)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x127, 0x1)
    OP_44(0x8, 0x1)
    OP_8F(0x9, 0xFFFFF768, 0x0, 0xFFFFF36C, 0x7D0, 0x0)

    ChrTalk(    #13
        0x101,
        "#1006F多谢，汉斯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x106,
        (
            "#552F精神十足是不错……\x01",
            "情况不要紧吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #15
        0x101,
        (
            "#1019F当然的啦！\x02\x03",

            "赶快调查旧校舍\x01",
            "整治幽灵才行！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x106,
        "#055F是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x104,
        (
            "#031F呵呵，艾丝蒂尔\x01",
            "也到了大显身手的时候呢。\x02\x03",

            "#030F好了……\x01",
            "赶快去试胆吧。\x02\x03",

            "说不定有魔兽，\x01",
            "某种程度来说\x01",
            "会武术的人去会比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #18
        0x106,
        (
            "#053F啊啊，当然了。\x02\x03",

            "#050F摄影师小姐倒还好说，\x01",
            "学生们就请回避吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#648F#6P知道啦。\x01",
            "可能会碍手碍脚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "#730F在这种时候\x01",
            "就待在这里待命啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x105,
        (
            "#043F那个，阿加特先生。\x02\x03",

            "我也……\x01",
            "一起去可以吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CB1():
        TurnDirection(0x101, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CB1)

    ChrTalk(    #22
        0x106,
        (
            "#052F喂喂，公主。\x02\x03",

            "你还是不要做出\x01",
            "轻率之举比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x105,
        (
            "#047F孤儿院的孩子们也在看着我，\x01",
            "以我个人来说也不能置之不理。\x02\x03",

            "#040F而且以前我去过\x01",
            "好几次旧校舍，\x01",
            "应该能帮上忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x106,
        (
            "#053F……真没办法。\x02\x03",

            "#051F算了，你的本事\x01",
            "要同行也还是够的。\x02\x03",

            "小心别乱来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x105,
        "#542F是，我会谨记于心。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(    #26
        0x101,
        (
            "#1006F好，那就决定了！\x02\x03",

            "为了抓住幽灵\x01",
            "去旧校舍吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x127,
        "#151FＧＯ～！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-2290, 0, -3350, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -2290, 0, -3350, 270)
    SetChrPos(0xF7, -2290, 0, -3350, 270)
    SetChrPos(0x105, -2290, 0, -3350, 270)
    SetChrPos(0x104, -2290, 0, -3350, 270)
    SetChrPos(0x127, -2290, 0, -3350, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x8, -1810, 300, -1250, 269)
    SetChrPos(0x9, -3520, 300, 200, 158)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    OP_0D()
    FadeToBright(1000, 0)
    OP_A2(0x1222)
    OP_28(0x83, 0x1, 0x80)
    OP_28(0x84, 0x4, 0x2)
    OP_28(0x84, 0x4, 0x8)
    EventEnd(0x0)
    Return()

    # Function_8_841 end

    def Function_9_F33(): pass

    label("Function_9_F33")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    SetChrPos(0x101, 240, 0, -2890, 225)
    SetChrPos(0xF7, 560, 0, -3920, 275)
    SetChrPos(0x105, -600, 0, -2190, 185)
    SetChrPos(0x104, -260, 0, -5270, 0)
    SetChrPos(0x127, -1510, 0, -5190, 45)
    SetChrPos(0x8, -1990, 0, -4400, 45)
    SetChrPos(0x9, -8610, 0, -3090, 90)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    OP_6D(1300, 0, 4690, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)

    def lambda_1020():
        OP_6D(-120, 0, -3010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1020)

    def lambda_1038():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1038)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_106E():

        label("loc_106E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_106E")

    QueueWorkItem2(0x101, 1, lambda_106E)

    def lambda_107F():

        label("loc_107F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_107F")

    QueueWorkItem2(0xF7, 1, lambda_107F)

    def lambda_1090():

        label("loc_1090")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1090")

    QueueWorkItem2(0x105, 1, lambda_1090)

    def lambda_10A1():

        label("loc_10A1")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_10A1")

    QueueWorkItem2(0x104, 1, lambda_10A1)

    def lambda_10B2():

        label("loc_10B2")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_10B2")

    QueueWorkItem2(0x127, 1, lambda_10B2)

    def lambda_10C3():

        label("loc_10C3")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_10C3")

    QueueWorkItem2(0x8, 1, lambda_10C3)

    def lambda_10D4():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_10D4)

    def lambda_10E6():
        OP_8E(0x9, 0xFFFFF63C, 0x0, 0xFFFFF36C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10E6)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #28
        0x9,
        (
            "#730F给，老师那里\x01",
            "借来的后门钥匙。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x9, 0x101, 0x3E8, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x1F\xF3\x03\x07\x00收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x3F3, 1)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x127, 0x1)
    OP_44(0x8, 0x1)
    OP_8F(0x9, 0xFFFFF768, 0x0, 0xFFFFF36C, 0x7D0, 0x0)

    ChrTalk(    #30
        0x101,
        (
            "#1006F多谢，汉斯！\x02\x03",

            "赶快调查旧校舍\x01",
            "整治幽灵才行！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x104,
        (
            "#031F呵呵，艾丝蒂尔\x01",
            "也到了大显身手的时候呢。\x02\x03",

            "#030F好了……\x01",
            "赶快去试胆吧。\x02\x03",

            "说不定有魔兽，\x01",
            "某种程度来说\x01",
            "会武术的人去会比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #32
        0x103,
        (
            "#020F那当然了。\x02\x03",

            "朵洛希姑且不论，\x01",
            "学生们还是回避吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#648F#6P知道啦。\x01",
            "可能会碍手碍脚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "#730F在这种时候\x01",
            "就待在这里待命啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x105,
        (
            "#043F那个，雪拉扎德小姐。\x02\x03",

            "我也……\x01",
            "一起去可以吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1338():
        TurnDirection(0x101, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1338)

    ChrTalk(    #36
        0x103,
        (
            "#023F哎呀，公主殿下？\x02\x03",

            "#522F嗯～虽然觉得\x01",
            "还是不要轻举妄动为好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x105,
        (
            "#047F孤儿院的孩子们都在看着，\x01",
            "以我个人来说也不能置之不理。\x02\x03",

            "#040F而且以前我进过\x01",
            "好几次旧校舍，\x01",
            "应该能帮上忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        (
            "#026F唔，原来如此啊。\x02\x03",

            "#020F你的本事应该没有问题……\x02\x03",

            "嗯，好吧。\x01",
            "可别太乱来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x105,
        "#542F是，我会谨记于心。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(    #40
        0x101,
        (
            "#1006F好，那就决定了！\x02\x03",

            "为了抓住幽灵\x01",
            "去旧校舍吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x127,
        "#151FＧＯ～！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-2290, 0, -3350, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -2290, 0, -3350, 270)
    SetChrPos(0xF7, -2290, 0, -3350, 270)
    SetChrPos(0x105, -2290, 0, -3350, 270)
    SetChrPos(0x104, -2290, 0, -3350, 270)
    SetChrPos(0x127, -2290, 0, -3350, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x8, -1810, 300, -1250, 269)
    SetChrPos(0x9, -3520, 300, 200, 158)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    OP_0D()
    FadeToBright(1000, 0)
    OP_A2(0x1222)
    OP_28(0x83, 0x1, 0x80)
    OP_28(0x84, 0x4, 0x2)
    OP_28(0x84, 0x4, 0x8)
    EventEnd(0x0)
    Return()

    # Function_9_F33 end

    def Function_10_15C9(): pass

    label("Function_10_15C9")

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
        (0, "loc_1643"),
        (1, "loc_1649"),
        (SWITCH_DEFAULT, "loc_164F"),
    )


    label("loc_1643")

    OP_A2(0x1200)
    Jump("loc_164F")

    label("loc_1649")

    OP_A2(0x1201)
    Jump("loc_164F")

    label("loc_164F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_165D")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1661")

    label("loc_165D")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1661")

    Return()

    # Function_10_15C9 end

    SaveToFile()

Try(main)
