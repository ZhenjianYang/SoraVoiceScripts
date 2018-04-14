from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3401   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
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
        '测量仪',                               # 9
        '亚妮拉丝',                             # 10
        '阿加特',                               # 11
        '雪拉扎德',                             # 12
        '艾尔·雷登关所方向',                   # 13
        '蔡斯方向',                             # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        'ED6_DT09/CH10130 ._CH',             # 00
        'ED6_DT09/CH10131 ._CH',             # 01
        'ED6_DT09/CH10750 ._CH',             # 02
        'ED6_DT09/CH10751 ._CH',             # 03
        'ED6_DT09/CH10760 ._CH',             # 04
        'ED6_DT09/CH10761 ._CH',             # 05
        'ED6_DT09/CH10770 ._CH',             # 06
        'ED6_DT09/CH10771 ._CH',             # 07
        'ED6_DT29/CH12410 ._CH',             # 08
        'ED6_DT29/CH12411 ._CH',             # 09
        'ED6_DT06/CH20020 ._CH',             # 0A
        'ED6_DT07/CH00065 ._CH',             # 0B
        'ED6_DT27/CH03090 ._CH',             # 0C
        'ED6_DT06/CH20053 ._CH',             # 0D
        'ED6_DT07/CH00020 ._CH',             # 0E
        'ED6_DT27/CH03091 ._CH',             # 0F
        'ED6_DT26/CH20284 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT09/CH10130P._CP',             # 00
        'ED6_DT09/CH10131P._CP',             # 01
        'ED6_DT09/CH10750P._CP',             # 02
        'ED6_DT09/CH10751P._CP',             # 03
        'ED6_DT09/CH10760P._CP',             # 04
        'ED6_DT09/CH10761P._CP',             # 05
        'ED6_DT09/CH10770P._CP',             # 06
        'ED6_DT09/CH10771P._CP',             # 07
        'ED6_DT29/CH12410P._CP',             # 08
        'ED6_DT29/CH12411P._CP',             # 09
        'ED6_DT06/CH20020P._CP',             # 0A
        'ED6_DT07/CH00065P._CP',             # 0B
        'ED6_DT27/CH03090P._CP',             # 0C
        'ED6_DT06/CH20053P._CP',             # 0D
        'ED6_DT07/CH00020P._CP',             # 0E
        'ED6_DT27/CH03091P._CP',             # 0F
        'ED6_DT26/CH20284P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 169300,
        Z                   = 0,
        Y                   = -27030,
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

    DeclNpc(
        X                   = 330710,
        Z                   = 0,
        Y                   = -37560,
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


    DeclMonster(
        X                   = 257600,
        Z                   = 70,
        Y                   = -24310,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 286240,
        Z                   = 20,
        Y                   = -35830,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 215540,
        Z                   = 0,
        Y                   = -31930,
        Unknown_0C          = 90,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 275760,
        Y                   = -2000,
        Z                   = -27140,
        Range               = 280150,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF7482,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    DeclActor(
        TriggerX            = 257600,
        TriggerZ            = -70,
        TriggerY            = -24310,
        TriggerRange        = 3000,
        ActorX              = 257600,
        ActorZ              = -70,
        ActorY              = -24310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 284880,
        TriggerZ            = 50,
        TriggerY            = -26870,
        TriggerRange        = 1000,
        ActorX              = 284880,
        ActorZ              = 1050,
        ActorY              = -26870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 267860,
        TriggerZ            = 0,
        TriggerY            = -29500,
        TriggerRange        = 1000,
        ActorX              = 268340,
        ActorZ              = 0,
        ActorY              = -25650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2D2",          # 00, 0
        "Function_1_2D3",          # 01, 1
        "Function_2_408",          # 02, 2
        "Function_3_940",          # 03, 3
        "Function_4_ADC",          # 04, 4
        "Function_5_B15",          # 05, 5
        "Function_6_B4E",          # 06, 6
        "Function_7_B87",          # 07, 7
        "Function_8_4011",         # 08, 8
        "Function_9_40AA",         # 09, 9
        "Function_10_4110",        # 0A, 10
        "Function_11_4346",        # 0B, 11
    )


    def Function_0_2D2(): pass

    label("Function_0_2D2")

    Return()

    # Function_0_2D2 end

    def Function_1_2D3(): pass

    label("Function_1_2D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34C")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_79(0xFF, 0x2)
    OP_64(0x2, 0x1)
    OP_82(0x80, 0x0)
    OP_C4(0x0, 0x1)
    OP_78(0x0, 0x0, 0x0)
    Jump("loc_35E")

    label("loc_34C")

    OP_16(0x2, 0xFA0, 0x1F018, 0xFFFD9AB8, 0x230038)

    label("loc_35E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_371")
    OP_64(0x0, 0x1)
    Jump("loc_375")

    label("loc_371")

    OP_65(0x0, 0x1)

    label("loc_375")

    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A7")
    OP_72(0x12, 0x4)
    OP_72(0x13, 0x4)
    OP_72(0x14, 0x4)
    OP_72(0x15, 0x4)
    OP_22(0x9E, 0x1, 0x64)
    OP_24(0x9E, 0x50)

    label("loc_3A7")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_407")
    LoadEffect(0x2, "map\\\\mp027_00.eff")
    PlayEffect(0x2, 0x2, 0xFF, 284880, 1050, -26870, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_407")

    Return()

    # Function_1_2D3 end

    def Function_2_408(): pass

    label("Function_2_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_415")
    Return()

    label("loc_415")

    EventBegin(0x0)
    OP_A2(0x141A)
    Fade(1000)
    OP_6D(279460, 150, -31510, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x101, 279920, 150, -32780, 0)
    SetChrPos(0xF7, 278990, 150, -31880, 42)
    SetChrPos(0x107, 279800, 150, -30480, 188)
    SetChrPos(0xF9, 281010, 0, -31850, 321)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#1011F嗯……\x02\x03",

            "卡鲁迪亚隧道的第一座桥\x01",
            "应该就是这里了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x107,
        (
            "#061F嗯，让我想想设置在\x01",
            "桥的哪一边比较好。\x02\x03",

            "#064F嗯……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)
    Sleep(500)
    OP_8C(0x107, 90, 400)
    OP_8C(0x107, 45, 400)
    Sleep(500)
    OP_8C(0x101, 50, 400)
    OP_8C(0xF7, 50, 400)
    OP_8C(0xF9, 50, 400)

    ChrTalk(    #2
        0x107,
        (
            "#060F这里有回复装置，\x01",
            "还是不要放在这里了。\x02\x03",

            "这样的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)
    Sleep(500)

    def lambda_5A4():

        label("loc_5A4")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_5A4")

    QueueWorkItem2(0x101, 1, lambda_5A4)

    def lambda_5B5():

        label("loc_5B5")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_5B5")

    QueueWorkItem2(0xF7, 1, lambda_5B5)

    def lambda_5C6():

        label("loc_5C6")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_5C6")

    QueueWorkItem2(0xF9, 1, lambda_5C6)

    def lambda_5D7():
        OP_8E(0xFE, 0x3F854, 0x0, 0xFFFF88AA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5D7)

    def lambda_5F2():
        OP_6D(271840, 150, -30100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F2)

    def lambda_60A():
        OP_67(0, 8330, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_60A)
    Sleep(3500)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)

    def lambda_62F():
        OP_8E(0xFE, 0x3F98A, 0xFFFFFFF6, 0xFFFF89E0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_62F)
    Fade(1000)
    OP_6D(259010, 20, -28410, 0)
    OP_67(0, 8330, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(89000, 0)
    OP_6E(262, 0)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)
    Sleep(1000)
    OP_43(0x101, 0x0, 0x0, 0x4)
    Sleep(200)
    OP_43(0xF7, 0x0, 0x0, 0x5)
    Sleep(200)
    OP_43(0xF9, 0x0, 0x0, 0x6)
    WaitChrThread(0x107, 0x1)

    def lambda_6C1():
        OP_8E(0xFE, 0x3EF76, 0x32, 0xFFFF9AB6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_6C1)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 90, 400)
    Sleep(500)
    OP_8C(0x107, 297, 400)
    Sleep(500)

    ChrTalk(    #3
        0x107,
        (
            "#064F#5P哎…让天线对着\x01",
            "蔡斯的方向……\x02\x03",

            "#060F嗯……这里就可以了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF9, 0x0)
    OP_8C(0x107, 140, 400)

    ChrTalk(    #4
        0x107,
        (
            "#061F姐姐。\x01",
            "我想这里应该可以哦。\x02\x03",

            "现在就开始设置测量仪吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【设置测量仪】\x01",      # 0
            "【先不设置】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_829")

    ChrTalk(    #5
        0x107,
        (
            "#061F那么我就开始\x01",
            "进行设置工作了哦。\x02\x03",

            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_930")

    label("loc_829")


    ChrTalk(    #6
        0x107,
        (
            "#064F哎……先不设置吗？\x02\x03",

            "#060F那就等准备好以后\x01",
            "再来这个地方调查吧。\x02\x03",

            "到时再进行设置工作。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(261190, -20, -31590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 259760, 0, -30960, 270)
    SetChrPos(0x1, 259760, 0, -30960, 270)
    SetChrPos(0x2, 259760, 0, -30960, 270)
    SetChrPos(0x3, 259760, 0, -30960, 270)
    OP_69(0x0, 0x0)
    OP_65(0x0, 0x1)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    label("loc_930")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 7)
    Return()

    # Function_2_408 end

    def Function_3_940(): pass

    label("Function_3_940")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(257060, 50, -25420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 256130, 30, -26520, 45)
    SetChrPos(0xF7, 257709, 50, -25940, 315)
    SetChrPos(0x107, 256660, 40, -25120, 45)
    SetChrPos(0xF9, 255050, 0, -25780, 47)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【设置测量仪】\x01",      # 0
            "【先不设置】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A60")

    ChrTalk(    #7
        0x107,
        (
            "#061F#5P那么，\x01",
            "进行设置工作了哦。\x02\x03",

            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACC")

    label("loc_A60")

    OP_8C(0x107, 225, 400)

    ChrTalk(    #8
        0x107,
        (
            "#064F#5P哎……先不设置吗？\x02\x03",

            "#060F那就等准备好以后\x01",
            "再来这个地方调查吧。\x02\x03",

            "到时再进行设置工作。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_ACC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 7)
    Return()

    # Function_3_940 end

    def Function_4_ADC(): pass

    label("Function_4_ADC")

    SetChrPos(0x101, 270570, 0, -31410, 265)

    def lambda_AF3():
        OP_8E(0xFE, 0x3F6B0, 0x0, 0xFFFF8710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF3)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 323, 400)
    Return()

    # Function_4_ADC end

    def Function_5_B15(): pass

    label("Function_5_B15")

    SetChrPos(0xF7, 271930, 0, -30560, 268)

    def lambda_B2C():
        OP_8E(0xFE, 0x3FBA5, 0xFFFFFFE2, 0xFFFF8A4E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_B2C)
    WaitChrThread(0xF7, 0x1)
    OP_8C(0xF7, 323, 400)
    Return()

    # Function_5_B15 end

    def Function_6_B4E(): pass

    label("Function_6_B4E")

    SetChrPos(0xF9, 272280, 0, -32150, 272)

    def lambda_B65():
        OP_8E(0xFE, 0x3FC50, 0xFFFFFFEC, 0xFFFF83D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_B65)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0xF9, 323, 400)
    Return()

    # Function_6_B4E end

    def Function_7_B87(): pass

    label("Function_7_B87")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(257060, 50, -25420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(80000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 256130, 30, -26520, 45)
    SetChrPos(0xF7, 257709, 50, -25940, 315)
    SetChrPos(0x107, 256660, 40, -25120, 45)
    SetChrPos(0xF9, 255050, 0, -25780, 47)
    OP_72(0x12, 0x4)
    OP_72(0x13, 0x4)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #9
        0x107,
        "#061F#5P嗯，这样就好了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5F")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇第一次设置测量仪】\x01",                          # 0
            "【◇设置了托兰特平原的测量仪】\x01",                  # 1
            "【◇设置了雷斯顿要塞的测量仪】\x01",                  # 2
            "【◇设置了托兰特平原和雷斯顿要塞的测量仪】\x01",      # 3
            "【◇不变更】\x01",                                    # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D2F"),
        (1, "loc_D3B"),
        (2, "loc_D47"),
        (3, "loc_D53"),
        (SWITCH_DEFAULT, "loc_D5F"),
    )


    label("loc_D2F")

    OP_A3(0x1419)
    OP_A3(0x141B)
    OP_A3(0x141F)
    Jump("loc_D5F")

    label("loc_D3B")

    OP_A2(0x1419)
    OP_A3(0x141B)
    OP_A3(0x141F)
    Jump("loc_D5F")

    label("loc_D47")

    OP_A3(0x1419)
    OP_A3(0x141B)
    OP_A2(0x141F)
    Jump("loc_D5F")

    label("loc_D53")

    OP_A2(0x1419)
    OP_A3(0x141B)
    OP_A2(0x141F)
    Jump("loc_D5F")

    label("loc_D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D1")

    ChrTalk(    #10
        0x101,
        (
            "#1004F哎～装好之后\x01",
            "原来是这样的啊。\x02\x03",

            "#1015F不过……\x01",
            "这个像盘子一样的东西是什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 225, 400)

    ChrTalk(    #11
        0x107,
        (
            "#060F#5P这个叫做抛物面天线\x01",
            "是一种可以集中导力波的天线。\x02\x03",

            "通过它可以把强力的导力波\x01",
            "传送到很远的地方……\x02\x03",

            "即使在卡鲁迪亚隧道这种地方\x01",
            "也都一样可以传送到呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB1")
    OP_8C(0x104, 90, 400)

    ChrTalk(    #12
        0x104,
        (
            "#033F#6P嗯……\x01",
            "那可是很厉害的东西啊。\x02\x03",

            "#030F那么…\x01",
            "在市场中也能买到这东西吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #13
        0x107,
        (
            "#560F#5P啊，我也不是\x01",
            "很清楚呢，\x02\x03",

            "不过爷爷的发明一般在问世半年后\x01",
            "就会在市面贩卖了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x104,
        "#031F#6P呼，那可太令人期待了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_FAE")
    OP_8C(0x103, 270, 400)

    ChrTalk(    #15
        0x103,
        "#027F#5P哎呀……想用在『工作联络』中吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x104,
        "#035F#6P哈～你在说什么嘛。\x02",
    )

    CloseMessageWindow()

    label("loc_FAE")

    Jump("loc_1113")

    label("loc_FB1")

    OP_8C(0x105, 90, 400)

    ChrTalk(    #17
        0x105,
        (
            "#044F#6P那个…提妲。\x02\x03",

            "我以前听说过，导力波遇到障碍物\x01",
            "就会减弱，不过……\x02\x03",

            "这个装置为什么在洞窟\x01",
            "这样的地方也可以使用呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #18
        0x107,
        (
            "#560F#5P嗯，这种天线\x01",
            "会赋予导力波指向性，\x01",
            "所以可以顺利进行传送。\x02\x03",

            "即使是像洞窟这种地方，\x01",
            "导力波似乎也能藉由墙壁反射\x01",
            "一路传送到出口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x105,
        (
            "#040F#6P原来如此……\x02\x03",

            "#041F不愧是拉赛尔博士啊，\x01",
            "天才的称号果然名不虚传。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1113")


    ChrTalk(    #20
        0x101,
        (
            "#1007F嗯…看起来只是个\x01",
            "不起眼的东西，竟然……\x02\x03",

            "#1006F不过这样一来就可以\x01",
            "把地震情报传送出去了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 225, 400)

    ChrTalk(    #21
        0x107,
        (
            "#560F#5P啊……嗯。\x01",
            "不过现在还没有启动，\x02\x03",

            "那我现在就按下开关了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 45, 400)
    Jump("loc_1216")

    label("loc_11D1")


    ChrTalk(    #22
        0x101,
        (
            "#1006F那么只剩下\x01",
            "打开开关了对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x107,
        "#560F#5P嗯，请等一下……\x02",
    )

    CloseMessageWindow()

    label("loc_1216")

    Fade(500)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 11)
    OP_0D()
    OP_8C(0xF7, 315, 400)
    OP_8C(0xF9, 45, 400)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x14, 0x4)
    OP_72(0x15, 0x4)
    OP_22(0x9E, 0x1, 0x64)
    OP_24(0x9E, 0x50)
    Sleep(2000)
    Fade(500)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1377")
    OP_8C(0x107, 225, 400)

    ChrTalk(    #24
        0x107,
        "#061F#5P呼，已经启动完毕了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1006F辛苦啦，提妲。\x02\x03",

            "#1015F不过…放在这种地方，\x01",
            "难道不会被魔兽破坏吗？\x02\x03",

            "这种装置应该脆弱易损吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x107,
        (
            "#560F#5P啊，这个不用担心。\x02\x03",

            "因为装置具备了\x01",
            "类似路灯的驱赶魔兽功能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1011F是吗，那就放心了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_1377")

    OP_8C(0x107, 225, 400)

    ChrTalk(    #28
        0x107,
        "#061F#5P呼，已经启动完毕了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_13C1")

    ChrTalk(    #29
        0x106,
        "#051F喔，辛苦啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_13C1")


    ChrTalk(    #30
        0x103,
        "#021F呵呵，辛苦啦。\x02",
    )

    CloseMessageWindow()

    label("loc_13DA")

    SetChrPos(0x9, 269420, 0, -30490, 0)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1410")
    SetChrPos(0xB, 269390, 0, -31690, 0)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_1426")

    label("loc_1410")

    SetChrPos(0xA, 269390, 0, -31690, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_1426")


    NpcTalk(    #31
        0x9,
        "女孩的声音",
        (
            "#3P啊！\x01",
            "艾丝蒂尔！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 135, 400)

    ChrTalk(    #32
        0x101,
        "#1004F#6P哎……！？\x02",
    )

    CloseMessageWindow()

    def lambda_148D():

        label("loc_148D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_148D")

    QueueWorkItem2(0xF7, 1, lambda_148D)

    def lambda_149E():

        label("loc_149E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_149E")

    QueueWorkItem2(0x107, 1, lambda_149E)

    def lambda_14AF():

        label("loc_14AF")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_14AF")

    QueueWorkItem2(0xF9, 1, lambda_14AF)

    def lambda_14C0():
        OP_6D(258339, 30, -28020, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14C0)

    def lambda_14D8():
        OP_67(0, 8300, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_14D8)

    def lambda_14F0():
        OP_6C(90000, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_14F0)

    def lambda_1500():
        OP_8E(0x9, 0x3FA29, 0xFFFFFFF6, 0xFFFF88E6, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1500)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_153F")

    def lambda_1527():
        OP_8E(0xB, 0x3FA3E, 0x1E, 0xFFFF8436, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1527)
    Jump("loc_155A")

    label("loc_153F")


    def lambda_1545():
        OP_8E(0xA, 0x3FA3E, 0x1E, 0xFFFF8436, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1545)

    label("loc_155A")

    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x9, 0x1)

    def lambda_156A():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_156A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_15B5")

    ChrTalk(    #33
        0x101,
        (
            "#1004F#6P亚妮拉丝！\x01",
            "还有雪拉姐！\x02",
        )
    )

    WaitChrThread(0xB, 0x2)

    def lambda_15A9():
        TurnDirection(0xB, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_15A9)
    CloseMessageWindow()
    Jump("loc_160C")

    label("loc_15B5")


    ChrTalk(    #34
        0x101,
        (
            "#1004F#6P亚妮拉丝！\x01",
            "还有阿加特也……\x02",
        )
    )

    WaitChrThread(0xA, 0x2)

    def lambda_15E9():
        TurnDirection(0xA, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15E9)
    CloseMessageWindow()

    ChrTalk(    #35
        0x107,
        "#064F#5P啊啊……！？\x02",
    )

    CloseMessageWindow()

    label("loc_160C")

    OP_44(0x107, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_161E():
        OP_8E(0xFE, 0x3F534, 0x14, 0xFFFF8FC6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_161E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1720")
    Sleep(50)

    def lambda_1645():
        OP_8E(0xFE, 0x3EBBF, 0x14, 0xFFFF91F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1645)
    Sleep(50)

    def lambda_1665():
        OP_8E(0xFE, 0x3F0A1, 0x0, 0xFFFF8CBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1665)
    Sleep(200)

    def lambda_1685():
        OP_8E(0xFE, 0x3F2D1, 0x0, 0xFFFF95E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1685)
    Sleep(100)

    def lambda_16A5():
        OP_8E(0xFE, 0x3EBE8, 0x14, 0xFFFF96BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_16A5)
    Sleep(100)

    def lambda_16C5():
        OP_8E(0xFE, 0x3E60C, 0x14, 0xFFFF9444, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_16C5)
    WaitChrThread(0x9, 0x0)

    def lambda_16E5():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_16E5)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x101, 135, 400)
    WaitChrThread(0xF7, 0x0)
    OP_8C(0xF7, 225, 400)
    WaitChrThread(0x107, 0x0)
    OP_8C(0x107, 135, 400)
    WaitChrThread(0xF9, 0x0)
    OP_8C(0xF9, 135, 400)
    Jump("loc_1827")

    label("loc_1720")

    Sleep(50)

    def lambda_172B():
        OP_8E(0xFE, 0x3EBBF, 0x14, 0xFFFF91F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_172B)
    Sleep(50)

    def lambda_174B():
        OP_8E(0xFE, 0x3F0A1, 0x0, 0xFFFF8CBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_174B)
    Sleep(200)

    def lambda_176B():
        OP_8E(0xFE, 0x3F2D1, 0x0, 0xFFFF95E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_176B)
    Sleep(100)

    def lambda_178B():
        OP_8E(0xFE, 0x3EBE8, 0x14, 0xFFFF96BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_178B)
    Sleep(100)

    def lambda_17AB():
        OP_8E(0xFE, 0x3E60C, 0x14, 0xFFFF9444, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_17AB)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x101, 135, 400)
    WaitChrThread(0x9, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_17E9")

    def lambda_17DE():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_17DE)
    Jump("loc_17F7")

    label("loc_17E9")


    def lambda_17EF():
        TurnDirection(0x9, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_17EF)

    label("loc_17F7")

    WaitChrThread(0x101, 0x0)
    OP_8C(0x101, 135, 400)
    WaitChrThread(0xF7, 0x0)
    OP_8C(0xF7, 225, 400)
    WaitChrThread(0x107, 0x0)
    OP_8C(0x107, 135, 400)
    WaitChrThread(0xF9, 0x0)
    OP_8C(0xF9, 135, 400)

    label("loc_1827")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2C4D")

    ChrTalk(    #36
        0x9,
        (
            "#811F#5P嘿嘿，好久不见了啊。\x02\x03",

            "真没想到竟然能在这种地方\x01",
            "再次相遇。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_198D")

    ChrTalk(    #37
        0xB,
        (
            "#021F不过…那边的那个男人\x01",
            "好像在哪里见过嘛……\x02\x03",

            "#020F你现在不是应该还在\x01",
            "亚尔摩的温泉逗留吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x104,
        (
            "#035F#6P呵，这件事\x01",
            "可就说来话长了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        "#027F知道啦，我只是好奇而已嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1016F嗯，看来似乎是这样。\x02",
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #41
        0x104,
        "#036F#6P你们两个好过分啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A77")

    label("loc_198D")


    ChrTalk(    #42
        0xB,
        (
            "#021F呵呵，真是偶然的相遇啊。\x02\x03",

            "#023F呀……\x01",
            "那边的不是公主殿下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x105,
        (
            "#041F#6P好久不见了。\x01",
            "雪拉扎德小姐。\x02\x03",

            "#542F我现在正在协助艾丝蒂尔\x01",
            "一起调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xB,
        (
            "#027F是吗，那可谢谢你啦。\x01",
            "请多帮助艾丝蒂尔吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x105,
        "#048F#6P呵呵，不用客气。\x02",
    )

    CloseMessageWindow()

    label("loc_1A77")


    ChrTalk(    #46
        0x107,
        (
            "#560F#6P那个那个……\x01",
            "好久不见了，雪拉姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        "#814F#5P哈……\x02",
    )

    OP_9E(0x9, 0x14, 0x0, 0x1F4, 0xFA0)
    CloseMessageWindow()
    TurnDirection(0x9, 0x107, 600)

    ChrTalk(    #48
        0xB,
        (
            "#023F哎呀呀。\x01",
            "提妲也在一起啊。\x02\x03",

            "#021F对了，我记得雾香小姐说\x01",
            "拉赛尔博士向协会提出了\x01",
            "协助调查地震的请求。\x02\x03",

            "所以你们就来帮忙了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x107,
        "#067F#6P嘿嘿，正是那样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        "#1317F#5P…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x101,
        (
            "#1015F亚妮拉丝？\x02\x03",

            "怎么了？\x01",
            "为什么突然发呆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "#1316F#5P……不行……\x02\x03",

            "#812F我已经无法忍耐了！！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#1004F哎？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)

    def lambda_1C3A():
        OP_6D(257339, 30, -27020, 1000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1C3A)

    def lambda_1C52():

        label("loc_1C52")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1C52")

    QueueWorkItem2(0x101, 1, lambda_1C52)

    def lambda_1C63():

        label("loc_1C63")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1C63")

    QueueWorkItem2(0xF7, 1, lambda_1C63)

    def lambda_1C74():

        label("loc_1C74")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1C74")

    QueueWorkItem2(0xF9, 1, lambda_1C74)
    SetChrChipByIndex(0x9, 15)
    OP_92(0x9, 0x107, 0x190, 0x1388, 0x0)

    def lambda_1C98():
        OP_94(0x1, 0x9, 0x0, 0xC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C98)
    OP_48()
    OP_8C(0x9, 315, 0)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 16)
    SetChrSubChip(0x9, 0)
    TurnDirection(0x107, 0x9, 0)
    OP_94(0x1, 0x107, 0xB4, 0xC8, 0x7D0, 0x0)
    WaitChrThread(0x9, 0x3)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)
    OP_62(0x9, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(200)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x9, 1)
    OP_0D()

    ChrTalk(    #54
        0x9,
        (
            "#1311F#5P啊啊啊～好可爱～！！\x02\x03",

            "这么可爱的孩子\x01",
            "实在让人忍不住想要抱抱啊～！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #55
        0x107,
        "#064F#6P哇哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1016F（对、对了……）\x02\x03",

            "（亚妮拉丝她…一看到\x01",
            "可爱的东西就会失控…）\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x9, 0)
    OP_0D()

    ChrTalk(    #57
        0x9,
        (
            "#811F#5P你是叫提妲对吧？\x01",
            "我是亚妮拉丝·艾尔菲德！\x02\x03",

            "叫我亚妮拉丝姐姐就好啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x107,
        "#065F#6P呜、呜哎哎哎～……\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x9, 1)
    OP_0D()

    ChrTalk(    #59
        0x9,
        (
            "#819F#5P啊啊啊啊！\x01",
            "现在的表情也好可爱～！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 12)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 257260, 20, -27260, 315)
    OP_0D()
    OP_8C(0x9, 135, 400)
    OP_8C(0x101, 45, 400)

    ChrTalk(    #60
        0x9,
        (
            "#812F#6P雪拉前辈！\x01",
            "我可以把她带回家吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        (
            "#027F我明白你的心情，但还是克制一下吧。\x02\x03",

            "那位老兄可是很可怕的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 225, 400)

    ChrTalk(    #62
        0x106,
        "#552F#5P……为什么要扯上我。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    OP_8C(0xF9, 135, 400)

    ChrTalk(    #63
        0x101,
        (
            "#1011F#6P对了，雪拉姐\x01",
            "你们为什么会在这里？\x02\x03",

            "难道\x01",
            "是来找我们的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        (
            "#020F不，只是偶然遇到而已。\x02\x03",

            "我们正在追捕\x01",
            "空贼团和特务兵。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #65
        0x101,
        (
            "#1020F#6P哎！？\x02\x03",

            "空贼和特务兵……\x01",
            "是逃亡中的余党吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x106,
        (
            "#052F#5P的确，王国军也没有\x01",
            "把他们全部抓捕归案呢。\x02\x03",

            "你们现在有什么线索了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20D6():
        OP_6D(258339, 30, -28020, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20D6)
    OP_8E(0x9, 0x3F534, 0x14, 0xFFFF8FC6, 0x9C4, 0x0)
    TurnDirection(0x9, 0x107, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #67
        0x9,
        (
            "#810F协会那里倒是接到了\x01",
            "几份目击情报，\x02\x03",

            "但可信程度都不太高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "#020F不过我们还是从中\x01",
            "挑出了一些比较可疑的情报，\x01",
            "目前正在各地展开调查。\x02\x03",

            "#022F而且……我听说了，\x02\x03",

            "『噬身之蛇』的爪牙似乎\x01",
            "已经在卢安地区现身了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1007F嗯、嗯……\x02\x03",

            "#1019F是个自称『怪盗绅士』，\x01",
            "戴着假面具的奇怪家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x106,
        (
            "#555F#5P虽然装束和性格比较怪异，\x01",
            "但实力可是相当了得。\x02\x03",

            "如果真的和他展开正面较量的话，\x01",
            "恐怕会相当危险啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#812F嗯嗯，连阿加特前辈\x01",
            "都那么说的话……\x02\x03",

            "看来『噬身之蛇』──\x01",
            "确实是个非常危险的组织呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xB,
        (
            "#026F与其说危险，\x01",
            "倒不如说他们的身份来历\x01",
            "都无从得知比较正确呢……\x02\x03",

            "#020F如果以后需要我们帮忙的话\x01",
            "请别客气，尽管开口就是。\x02\x03",

            "通过协会的话\x01",
            "马上就可以联络到我们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1006F嗯，我们会的。\x02\x03",

            "雪拉姐也是！如果需要我们帮忙的话\x01",
            "就随时联系哦。\x02\x03",

            "我们马上就会赶到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xB,
        (
            "#021F呵呵，到时就拜托你们了。\x02\x03",

            "#027F虽然是难得的再会，\x01",
            "不过这种地方也不适合聊天……\x02\x03",

            "我们就\x01",
            "先失陪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1017F啊，嗯……\x01",
            "虽然很遗憾，但也没有办法呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F6")

    ChrTalk(    #76
        0x104,
        (
            "#036F#6P啊啊～太残忍了！\x02\x03",

            "面对着久别重逢的恋人，\x01",
            "竟然会如此冷淡薄情？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xB,
        (
            "#021F啊，既然你这样说的话，\x01",
            "不如就和我们一起走吧？\x02\x03",

            "今天晚上一起去喝酒，好好庆祝一下\x01",
            "美妙的重逢，这样总行了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        (
            "#811F啊，这主意不错⊙\x01",
            "毕竟我也算是个酒豪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x104,
        (
            "#034F#6P……两位\x01",
            "一路上请多加小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1019F真是的……\x01",
            "一说到喝酒就原形毕露了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F6")


    ChrTalk(    #81
        0x106,
        (
            "#050F#5P我并不是故意轻视你们，\x01",
            "不过你们毕竟是两个女人结伴同行。\x02\x03",

            "遇到什么事的话还是不要太乱来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "#814F哇～阿加特前辈\x01",
            "竟然会这么关心我…\x02\x03",

            "究竟在想什么呢？难道说…\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #83
        0x106,
        "#552F#5P可恶，你是皮痒了吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x9,
        (
            "#1315F嘿嘿嘿……\x01",
            "开个玩笑而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xB,
        (
            "#027F呵呵，说得也是。\x01",
            "我们会牢记你的忠告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        (
            "#1310F阿加特前辈，多保重哦！\x02\x03",

            "#811F艾丝蒂尔、提妲。\x01",
            "下次再见面时要一起去玩哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#1006F嗯！非常期待！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x107,
        "#560F#6P嗯嗯～再见啦！\x02",
    )

    CloseMessageWindow()

    def lambda_27C4():

        label("loc_27C4")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_27C4")

    QueueWorkItem2(0x101, 1, lambda_27C4)

    def lambda_27D5():

        label("loc_27D5")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_27D5")

    QueueWorkItem2(0xF7, 1, lambda_27D5)

    def lambda_27E6():

        label("loc_27E6")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_27E6")

    QueueWorkItem2(0x107, 1, lambda_27E6)

    def lambda_27F7():

        label("loc_27F7")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_27F7")

    QueueWorkItem2(0xF9, 1, lambda_27F7)

    def lambda_2808():
        OP_8E(0xFE, 0x3B6D2, 0x0, 0xFFFF9C3C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2808)
    Sleep(200)

    def lambda_2828():
        OP_8E(0xFE, 0x3E8AA, 0xA, 0xFFFF8DFA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2828)
    WaitChrThread(0x9, 0x1)

    def lambda_2848():
        OP_6D(255210, 20, -27320, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2848)

    def lambda_2860():
        OP_8E(0xFE, 0x3B6D2, 0x0, 0xFFFF9C3C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2860)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    Fade(500)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)
    OP_6D(257070, 20, -26960, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF7, 257800, 30, -27320, 270)
    OP_0D()
    OP_8C(0x101, 0, 400)
    OP_8C(0x107, 180, 400)
    OP_8C(0xF9, 90, 400)

    ChrTalk(    #89
        0x101,
        (
            "#1017F#6P哈～在这种地方\x01",
            "竟然能遇到雪拉姐她们，\x01",
            "真是完全没想到啊。\x02\x03",

            "#1004F提妲，你没关系吧？\x02\x03",

            "亚妮拉丝突然就\x01",
            "那么抱住你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x107,
        (
            "#067F嘿嘿，我没事的。\x02\x03",

            "……虽然说…\x01",
            "吓了一大跳……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1016F#6P嗯～她并没有恶意的，\x01",
            "你就原谅她好啦。\x02\x03",

            "#1015F话说回来，\x01",
            "空贼和特务兵的余党……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x106,
        (
            "#051F都是和『结社』一样，\x01",
            "只会在暗中鬼祟行动的家伙啊。\x02\x03",

            "他们两个继续追查下去的话，\x01",
            "说不定能获得什么重要的线索。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 400)
    OP_8C(0x107, 90, 400)

    ChrTalk(    #93
        0x101,
        (
            "#1006F#6P那么我们也要加油了，\x01",
            "绝对不可以输给他们。\x02\x03",

            "#1011F总之……\x01",
            "这里就已经ＯＫ了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B53")

    ChrTalk(    #94
        0x106,
        (
            "#051F好！就保持这样的干劲，\x01",
            "把剩下的测量仪也设置好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#1006F#6P了解！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4A")

    label("loc_2B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2BB3")

    ChrTalk(    #96
        0x106,
        (
            "#051F啊啊～这是第２个了。\x02\x03",

            "去把最后一个也搞定吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#1006F#6P  ＯＫ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4A")

    label("loc_2BB3")


    ChrTalk(    #98
        0x106,
        (
            "#051F啊啊，这样就把\x01",
            "全部测量仪设置完毕了。\x02\x03",

            "老爷子还在等着我们，\x01",
            "赶快去中央工房的演算室吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1006F#6P  ＯＫ～！\x01",
            "就在中央工房的５楼吧。\x02",
        )
    )

    OP_28(0x87, 0x1, 0x200)
    CloseMessageWindow()

    label("loc_2C4A")

    Jump("loc_4001")

    label("loc_2C4D")


    ChrTalk(    #100
        0x9,
        (
            "#811F#5P好久不见了！\x01",
            "雪拉前辈！艾丝蒂尔！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x103,
        (
            "#021F#5P呵呵，好久不见了呢。\x01",
            "你还是一样，这么有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "#051F怎么回事，竟然\x01",
            "这么多人一起行动啊。\x02\x03",

            "#052F噢。\x01",
            "提妲也在一起吗。\x02\x03",

            "#051F好久不见了啊，小家伙。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #103
        0x107,
        (
            "#062F#6P呜……\x01",
            "谁是小家伙啊，真过分。\x02\x03",

            "#560F不过，真的是好久不见了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #104
        0x9,
        (
            "#814F哇！！真可爱！！\x02\x03",

            "#1310F这孩子是谁呀！？\x01",
            "艾丝蒂尔的妹妹吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1016F嘿嘿，可以算是吧。\x02\x03",

            "#1006F她叫提妲，\x01",
            "拉赛尔博士的孙女。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x9,
        (
            "#810F嗯，是这样啊。\x02\x03",

            "#811F我叫亚妮拉丝！\x01",
            "亚妮拉丝·艾尔菲德！\x02\x03",

            "请多多指教哦！提妲！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x107,
        (
            "#560F#6P是、是的……\x01",
            "请多多指教。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302D")

    ChrTalk(    #108
        0xA,
        (
            "#555F怎么回事，在那边站着的\x01",
            "不是埃雷波尼亚帝国的演奏家吗。\x02\x03",

            "为什么连你也在一起啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x104,
        (
            "#035F#6P呵，如此浅显易见\x01",
            "的事情何必再问。\x02\x03",

            "#037F帮助我可爱的小猫咪们\x01",
            "难道还需要什么理由吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        (
            "#552F该说什么才好……\x01",
            "看来你们也很辛苦啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x103,
        "#027F#5P呵呵，是有一点呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1007F是非～常～辛苦啊。\x02\x03",

            "#1011F话说回来，阿加特你们\x01",
            "为什么会出现在这里呢？\x02\x03",

            "难不成是\x01",
            "来找我们的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3133")

    label("loc_302D")


    ChrTalk(    #113
        0xA,
        (
            "#052F什么啊，站在那边的\x01",
            "不就是公主吗。\x02\x03",

            "怎么连你也在一起的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x105,
        (
            "#041F#6P好久不见了，阿加特先生。\x02\x03",

            "#542F其实我现在正在\x01",
            "协助艾丝蒂尔进行调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        (
            "#051F哈哈，公主还是\x01",
            "这么热心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1011F对了，阿加特你们\x01",
            "为什么会出现在这里呢？\x02\x03",

            "难不成是\x01",
            "来找我们的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3133")


    ChrTalk(    #117
        0xA,
        (
            "#051F不，只是偶然相遇而已。\x02\x03",

            "我们正在追捕\x01",
            "空贼团和特务兵。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #118
        0x101,
        (
            "#1020F哎！？\x02\x03",

            "空贼和特务兵……\x01",
            "那些家伙的余党吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        (
            "#023F#5P的确连王国军也没有\x01",
            "把他们全部抓捕归案呢。\x02\x03",

            "你们有什么线索了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        (
            "#810F协会那里倒是接到了\x01",
            "几份目击情报…\x02\x03",

            "但可信程度都不太高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xA,
        (
            "#551F但谨慎起见，还是要在各地巡视，\x01",
            "调查一些可疑的场所。\x02\x03",

            "#050F而且……我也听说了。\x02\x03",

            "『噬身之蛇』的爪牙似乎\x01",
            "已经在卢安地区现身了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1007F嗯、嗯……\x02\x03",

            "#1019F嗯，是个叫做『怪盗绅士』，\x01",
            "戴着假面具的奇怪家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x103,
        (
            "#022F#5P虽然打扮和性格比较怪异，\x01",
            "但实力却是非常厉害的。\x02\x03",

            "如果真的和他展开正面较量的话，\x01",
            "恐怕胜算不高呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        (
            "#812F嗯嗯…连雪拉前辈\x01",
            "都那么说的话……\x02\x03",

            "看来『噬身之蛇』──\x01",
            "确实是个非常危险的组织呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xA,
        (
            "#552F与其说危险\x01",
            "倒不如说他们的身份来历\x01",
            "都无从得知比较正确啊……\x02\x03",

            "#050F如果以后需要我们帮忙的话，\x01",
            "不要客气，尽管开口就是。\x02\x03",

            "通过协会的话，\x01",
            "应该可以马上联络到我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1006F嗯，我们会的。\x02\x03",

            "阿加特你们也是，需要帮忙的话\x01",
            "就随时联络我们哦。\x02\x03",

            "我们马上就会赶到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xA,
        (
            "#053F哦！应该没那个必要，\x01",
            "不过万一有需要的话我会去找你们的。\x02\x03",

            "#051F好了，这里也不是\x01",
            "适合聊天的地方。\x02\x03",

            "我们差不多也该走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#1017F啊，嗯……\x01",
            "虽然很遗憾，但也没有办法呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x107)

    ChrTalk(    #129
        0x107,
        (
            "#063F#6P啊……\x01",
            "那个…阿加特哥哥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xA,
        "#052F喔？怎么了？\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #131
        0x107,
        (
            "#560F#6P嗯，那个……\x02\x03",

            "……………………………\x02\x03",

            "#562F对不起……\x01",
            "没什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xA,
        (
            "#555F什么嘛，奇怪的家伙。\x02\x03",

            "#051F算了，替我向拉赛尔老爷子\x01",
            "问声好吧。\x02\x03",

            "还有啊，你也不要整天\x01",
            "都琢磨那些机械了。\x02\x03",

            "小孩子就应该有小孩子的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        (
            "#067F#6P嘿嘿……我知道啦。\x02\x03",

            "#560F不过，阿加特哥哥\x01",
            "也不能太莽撞哦！\x02\x03",

            "你总是喜欢意气用事，\x01",
            "那样是很危险的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xA,
        (
            "#055F哦……?\x01",
            "竟然变得这么能言善道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x107,
        (
            "#067F#6P嘿嘿，那是当然的啦。\x02\x03",

            "#066F我又不会……\x01",
            "永远都是个小孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x9,
        (
            "#811F呵呵～对手是提妲的话，\x01",
            "阿加特前辈也只能乖乖服输了啊。\x02\x03",

            "#1310F那我们这就走了，大家都要保重啊！\x02\x03",

            "艾丝蒂尔，提妲。\x01",
            "下次再见面时要一起去玩哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#1006F嗯！非常期待！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x107,
        "#560F#6P是、是的……\x02",
    )

    CloseMessageWindow()

    def lambda_38B3():

        label("loc_38B3")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_38B3")

    QueueWorkItem2(0x107, 1, lambda_38B3)

    def lambda_38C4():

        label("loc_38C4")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_38C4")

    QueueWorkItem2(0xF7, 1, lambda_38C4)

    def lambda_38D5():

        label("loc_38D5")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_38D5")

    QueueWorkItem2(0x101, 1, lambda_38D5)

    def lambda_38E6():

        label("loc_38E6")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_38E6")

    QueueWorkItem2(0xF9, 1, lambda_38E6)

    def lambda_38F7():
        OP_8E(0xFE, 0x3B6D2, 0x0, 0xFFFF9C3C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_38F7)
    Sleep(200)

    def lambda_3917():
        OP_8E(0xFE, 0x3E8AA, 0xA, 0xFFFF8DFA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3917)
    WaitChrThread(0x9, 0x1)

    def lambda_3937():
        OP_6D(255210, 20, -27320, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3937)

    def lambda_394F():
        OP_8E(0xFE, 0x3B6D2, 0x0, 0xFFFF9C3C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_394F)
    WaitChrThread(0xA, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    Fade(1000)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)
    OP_6D(257070, 20, -26960, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF7, 257800, 30, -27320, 270)
    OP_0D()
    OP_8C(0x101, 45, 400)
    OP_8C(0xF9, 90, 400)

    ChrTalk(    #139
        0x101,
        (
            "#1017F#6P哈～在这种地方\x01",
            "竟然会遇到阿加特他们，\x01",
            "真是完全没想到啊。\x02\x03",

            "#1016F阿加特和亚妮拉丝都还是老样子啊。\x02\x03",

            "实在没有办法想象他们两人\x01",
            "在旅行时是如何相处的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x103,
        (
            "#027F亚妮拉丝的性格\x01",
            "那么地率直活泼。\x02\x03",

            "就算是和阿加特这种别扭的家伙相处\x01",
            "应该也不是什么困难的事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x107,
        "#063F………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #142
        0x101,
        "#1004F#6P提妲？\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #143
        0x107,
        "#065F哎……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8C(0x107, 180, 600)

    ChrTalk(    #144
        0x107,
        (
            "#067F怎、怎么了！？\x01",
            "艾丝蒂尔姐姐！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1015F#6P你怎么啦？\x01",
            "为什么一副若有所思的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x107,
        (
            "#560F没、没有啦！！\x02\x03",

            "只是……\x01",
            "稍微有些吃惊而已……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1004F#6P吃惊……为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x107,
        (
            "#065F哎……那个……\x02\x03",

            "#067F阿加特哥哥……\x01",
            "竟然已经有恋人了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#1004F#6P恋人？？是指亚妮拉丝吗？\x02\x03",

            "#1016F啊哈哈，你搞错了啦，\x01",
            "他们只是工作上的搭档。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x107,
        "#064F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x103,
        (
            "#027F呵呵，只是为了调查『结社』\x01",
            "而联手行动而已。\x02\x03",

            "完全不是你想的那样啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x107,
        (
            "#560F是、是这样吗？\x02\x03",

            "#067F原来如此……嘿嘿嘿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1016F#6P（原来……是这样吗。）\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 400)
    Sleep(400)

    ChrTalk(    #154
        0x101,
        (
            "#1015F#6P话说回来，\x01",
            "空贼和特务兵的余党啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 225, 400)

    ChrTalk(    #155
        0x103,
        (
            "#020F都是和『结社』一样\x01",
            "藏身在暗地里行动的家伙。\x02\x03",

            "阿加特他们继续追查下去的话，\x01",
            "应该能获得什么重要的线索才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#1006F#6P那么我们也要加油了，\x01",
            "绝对不能输给她们。\x02\x03",

            "#1011F总之……\x01",
            "这里就已经ＯＫ了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EFF")

    ChrTalk(    #157
        0x103,
        (
            "#027F嗯，继续\x01",
            "把剩下的测量仪设置好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        "#1006F#6P了解！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4001")

    label("loc_3EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F5D")

    ChrTalk(    #159
        0x103,
        (
            "#526F嗯，这是第２个了。\x02\x03",

            "马上去设置最后一个吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        "#1006F#6P  ＯＫ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4001")

    label("loc_3F5D")


    ChrTalk(    #161
        0x103,
        (
            "#026F嗯，这样一来，\x01",
            "全部测量仪都设置完毕了。\x02\x03",

            "#020F拉赛尔博士还在等着我们，\x01",
            "现在就回中央工房的演算室吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        (
            "#1006F#6P  ＯＫ～！\x01",
            "就在中央工房的５楼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x87, 0x1, 0x200)

    label("loc_4001")

    OP_64(0x0, 0x1)
    OP_A2(0x141B)
    OP_28(0x87, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_7_B87 end

    def Function_8_4011(): pass

    label("Function_8_4011")

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
        (0, "loc_408B"),
        (1, "loc_4091"),
        (SWITCH_DEFAULT, "loc_4097"),
    )


    label("loc_408B")

    OP_A2(0x1200)
    Jump("loc_4097")

    label("loc_4091")

    OP_A2(0x1201)
    Jump("loc_4097")

    label("loc_4097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_40A5")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_40A9")

    label("loc_40A5")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_40A9")

    Return()

    # Function_8_4011 end

    def Function_9_40AA(): pass

    label("Function_9_40AA")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_40E4")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_40FE")

    label("loc_40E4")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_40FE")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_9_40AA end

    def Function_10_4110(): pass

    label("Function_10_4110")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4187")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x150, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4157")

    AnonymousTalk(    #163
        "\x07\x05黑漆漆的，看不清楚。\x02",
    )

    Jump("loc_416C")

    label("loc_4157")


    AnonymousTalk(    #164
        "\x07\x05导力好像停止了。\x02",
    )


    label("loc_416C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_4345")

    label("loc_4187")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #165
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_432A")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x2, 0x2)
    PlayEffect(0x2, 0x2, 0xFF, 284880, 1050, -26870, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x32)
    OP_73(0x11)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 284880, 1050, -26870, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x2, 0x2, 0xFF, 284880, 1050, -26870, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_432A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4344")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_4344")

    Return()

    label("loc_4345")

    Return()

    # Function_10_4110 end

    def Function_11_4346(): pass

    label("Function_11_4346")

    EventBegin(0x1)

    ChrTalk(    #166
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_4372():
        OP_6D(268050, -1000, -27370, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4372)

    def lambda_438A():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_438A)

    def lambda_439A():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_439A)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #167
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_443F")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_C0(0xE, 0x1E, 0x4160E, 0x0, 0xFFFF8CC4, 0x0, 0x41834, 0xFFFFFAEC, 0xFFFF9BCE)
    OP_51(0x101, 0x28, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    EventEnd(0x1)
    Jump("loc_444E")

    label("loc_443F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_444E")
    EventEnd(0x1)

    label("loc_444E")

    Return()

    # Function_11_4346 end

    SaveToFile()

Try(main)
