from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5901   ._SN',
        MapName             = 'Other',
        Location            = 'C5901.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        '奈尔',                                 # 9
        '朵洛希',                               # 10
        '公园区域『卡尔玛丽』1',                # 11
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT06/CH20063 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT06/CH20063P._CP',             # 01
    )

    DeclNpc(
        X                   = 550,
        Z                   = -8000,
        Y                   = -84180,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = -8000,
        Y                   = -74410,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -10,
        Z                   = 0,
        Y                   = -46260,
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


    DeclEvent(
        X                   = 0,
        Y                   = -6000,
        Z                   = -105000,
        Range               = 2000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = 28020,
        TriggerZ            = -7650,
        TriggerY            = -71570,
        TriggerRange        = 1000,
        ActorX              = 28320,
        ActorZ              = -6350,
        ActorY              = -71070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_1E0",          # 01, 1
        "Function_2_21B",          # 02, 2
        "Function_3_23F",          # 03, 3
        "Function_4_3EB",          # 04, 4
        "Function_5_62E",          # 05, 5
        "Function_6_6A2",          # 06, 6
        "Function_7_9D3",          # 07, 7
        "Function_8_AC6",          # 08, 8
        "Function_9_AFC",          # 09, 9
        "Function_10_C58",         # 0A, 10
        "Function_11_DD2",         # 0B, 11
        "Function_12_E59",         # 0C, 12
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170")
    Jump("loc_190")

    label("loc_170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B")
    Jump("loc_190")

    label("loc_17B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_190")

    label("loc_190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1A1")
    OP_A3(0x10F0)
    Event(0, 5)
    Jump("loc_1DF")

    label("loc_1A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1B2")
    OP_A3(0x10F1)
    Event(0, 7)
    Jump("loc_1DF")

    label("loc_1B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_1C3")
    OP_A3(0x10F2)
    Event(0, 10)
    Jump("loc_1DF")

    label("loc_1C3")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_1CF"),
        (SWITCH_DEFAULT, "loc_1DF"),
    )


    label("loc_1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DF")
    Event(0, 6)

    label("loc_1DF")

    Return()

    # Function_0_15E end

    def Function_1_1E0(): pass

    label("Function_1_1E0")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFCD380, 0x23007A)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 5)), scpexpr(EXPR_END)), "loc_215")
    OP_71(0x3, 0x10)
    OP_64(0x0, 0x1)
    OP_71(0x4, 0x4)

    label("loc_215")

    OP_22(0x1CA, 0x1, 0x64)
    Return()

    # Function_1_1E0 end

    def Function_2_21B(): pass

    label("Function_2_21B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23E")
    OP_8D(0xFE, -1490, -89750, 1490, -74630, 2000)
    Jump("Function_2_21B")

    label("loc_23E")

    Return()

    # Function_2_21B end

    def Function_3_23F(): pass

    label("Function_3_23F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #0
        0x101,
        (
            "#1004F咦，奈尔……\x01",
            "你在这里干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "#140F哦，我稍微走远一点来看看。\x02\x03",

            "飞船的周围\x01",
            "基本上都拍过了。\x02\x03",

            "不过这风景还真让人\x01",
            "想不到是在天上呢……\x02\x03",

            "看来这里的确是\x01",
            "公园区域呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x22D3)
    Jump("loc_3E7")

    label("loc_30D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F")

    ChrTalk(    #2
        0x8,
        (
            "#140F哦，空中的湖泊和\x01",
            "从那里流下的瀑布啊……\x02\x03",

            "看来这里的确是\x01",
            "公园区域呢。\x02\x03",

            "总之让朵洛希那家伙\x01",
            "先拍几张照片吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_3E7")

    label("loc_38F")


    ChrTalk(    #3
        0x8,
        (
            "#140F空中的湖和\x01",
            "从那里流下的瀑布啊……\x02\x03",

            "#141F嘿嘿，这或许正合适\x01",
            "作为特刊的封面呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E7")

    TalkEnd(0xFE)
    Return()

    # Function_3_23F end

    def Function_4_3EB(): pass

    label("Function_4_3EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_500")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #4
        0x101,
        (
            "#1004F咦，朵洛希……\x01",
            "你在这里干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#150F嗯，我正在拍\x01",
            "杂志封面用的照片～\x02\x03",

            "但是到处都是我想拍的风景，\x01",
            "所以有点眼花缭乱的～\x02\x03",

            "接下来去拍拍\x01",
            "那个升降梯吧～\x02\x03",

            "#151F啊，反正机会难得，\x01",
            "上去看看或许也不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1016F你、你可别就这么\x01",
            "走丢了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x22D3)
    Jump("loc_62A")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B6")

    ChrTalk(    #7
        0x9,
        (
            "#150F嗯～到处都是我想拍的风景，\x01",
            "所以有点眼花缭乱的～\x02\x03",

            "先听前辈的话\x01",
            "去拍那个瀑布吧～\x02\x03",

            "接下来去那边拍拍\x01",
            "那个升降梯吧～\x02\x03",

            "#151F啊，反正机会难得，\x01",
            "上去看看或许也不错。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_62A")

    label("loc_5B6")


    ChrTalk(    #8
        0x9,
        (
            "#150F先听前辈的话\x01",
            "去拍那个瀑布吧～\x02\x03",

            "接下来去拍拍\x01",
            "那个升降梯吧～\x02\x03",

            "坐那个升降梯……\x01",
            "看起来好像非常舒服的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62A")

    TalkEnd(0xFE)
    Return()

    # Function_4_3EB end

    def Function_5_62E(): pass

    label("Function_5_62E")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-980, 0, -103450, 0)
    OP_67(0, 5900, -10000, 0)
    OP_6B(27200, 0)
    OP_6C(21000, 0)
    OP_6E(236, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    OP_22(0x7C, 0x0, 0x64)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_62E end

    def Function_6_6A2(): pass

    label("Function_6_6A2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B9")
    Call(0, 11)
    Call(0, 12)

    label("loc_6B9")

    OP_6D(-21660, -2500, -66230, 0)
    OP_67(0, 4770, -10000, 0)
    OP_6B(1150, 0)
    OP_6C(33000, 0)
    OP_6E(602, 0)
    SetChrPos(0x101, 1320, -500, -56520, 180)
    SetChrPos(0x102, 150, -500, -56440, 180)
    SetChrPos(0xF8, 1220, -500, -55050, 180)
    SetChrPos(0xF9, -170, -500, -55050, 180)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_74A():
        OP_6D(9270, -8000, -86360, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_74A)

    def lambda_762():
        OP_67(0, 8039, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_762)

    def lambda_77A():
        OP_6B(9070, 12000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_77A)

    def lambda_78A():
        OP_6C(336000, 12000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_78A)

    def lambda_79A():
        OP_6E(600, 12000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_79A)
    OP_C8(0x200, 0x46, "C_PLAC26._CH", 0x0, 0xFA0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    Fade(500)
    OP_6D(1870, -500, -56280, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4030, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82F")

    ChrTalk(    #9
        0x107,
        "#560F#5P哇……！\x02",
    )

    CloseMessageWindow()

    label("loc_82F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_856")

    ChrTalk(    #10
        0x105,
        "#1168F#5P好漂亮……\x02",
    )

    CloseMessageWindow()

    label("loc_856")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_882")

    ChrTalk(    #11
        0x103,
        "#027F#5P好棒的风景呢……\x02",
    )

    CloseMessageWindow()

    label("loc_882")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AD")

    ChrTalk(    #12
        0x109,
        "#1064F#5P哇～了不起啊。\x02",
    )

    CloseMessageWindow()

    label("loc_8AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E2")

    ChrTalk(    #13
        0x104,
        (
            "#031F#5P哟……\x01",
            "很不错的视觉享受。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90A")

    ChrTalk(    #14
        0x106,
        "#052F#5P这还真是……\x02",
    )

    CloseMessageWindow()

    label("loc_90A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93B")

    ChrTalk(    #15
        0x108,
        (
            "#070F#5P嗯……\x01",
            "好清爽的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93B")


    ChrTalk(    #16
        0x101,
        (
            "#1016F#5P怎、怎么说呢……\x02\x03",

            "#1008F实在让人想不到\x01",
            "这是在天上……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        (
            "#1035F#6P古代塞姆里亚文明……\x02\x03",

            "#1040F看来不仅仅是一个\x01",
            "技术发达的社会呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2202)
    EventEnd(0x0)
    Return()

    # Function_6_6A2 end

    def Function_7_9D3(): pass

    label("Function_7_9D3")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(140, -6000, -104620, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_6F(0x0, 500)
    FadeToBright(1000, 0)

    def lambda_A3C():
        OP_6D(27920, -7650, -71810, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A3C)
    OP_6C(327000, 7000)
    Fade(500)
    OP_6D(26130, -8000, -68590, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(327000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)
    OP_71(0x4, 0x4)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_9D3 end

    def Function_8_AC6(): pass

    label("Function_8_AC6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #18
        "\x07\x05门牢牢地锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_AC6 end

    def Function_9_AFC(): pass

    label("Function_9_AFC")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(0, -6000, -105000, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x101, 0, -6000, -104000, 0)
    OP_89(0x102, -1000, -6000, -105000, 0)
    OP_89(0xF8, 1000, -6000, -105000, 0)
    OP_89(0xF9, 0, -6000, -106000, 0)
    OP_0D()
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x258)

    def lambda_BA8():
        OP_6D(0, 45000, -105000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA8)

    def lambda_BC0():
        OP_67(0, 10500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BC0)

    def lambda_BD8():
        OP_6C(320000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BD8)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1CA, 0x5A)
    Sleep(100)
    OP_24(0x1CA, 0x50)
    Sleep(100)
    OP_24(0x1CA, 0x46)
    Sleep(100)
    OP_24(0x1CA, 0x3C)
    Sleep(100)
    OP_24(0x1CA, 0x32)
    Sleep(100)
    OP_24(0x1CA, 0x28)
    Sleep(100)
    OP_24(0x1CA, 0x1E)
    Sleep(100)
    OP_24(0x1CA, 0x14)
    Sleep(100)
    OP_24(0x1CA, 0xA)
    Sleep(100)
    OP_23(0x1CA)
    Sleep(500)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C6000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_AFC end

    def Function_10_C58(): pass

    label("Function_10_C58")

    EventBegin(0x0)
    OP_6D(0, 40000, -105000, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(319000, 0)
    OP_6E(262, 0)
    OP_6F(0x0, 500)
    OP_48()
    OP_89(0x101, 0, 100000, -104000, 0)
    OP_89(0x102, -1000, 100000, -105000, 0)
    OP_89(0xF8, 1000, 100000, -105000, 0)
    OP_89(0xF9, 0, 100000, -106000, 0)
    OP_22(0xEB, 0x0, 0x64)
    FadeToBright(1000, 0)

    def lambda_CF7():
        OP_6D(0, -6000, -105000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CF7)

    def lambda_D0F():
        OP_67(0, 6500, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D0F)

    def lambda_D27():
        OP_6C(315000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D27)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    Sleep(200)
    Fade(500)
    OP_6D(0, -5990, -102670, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, -6000, -102670, 0)
    SetChrPos(0x1, 0, -6000, -102670, 0)
    SetChrPos(0x2, 0, -6000, -102670, 0)
    SetChrPos(0x3, 0, -6000, -102670, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_10_C58 end

    def Function_11_DD2(): pass

    label("Function_11_DD2")

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
        (0, "loc_E4C"),
        (1, "loc_E52"),
        (SWITCH_DEFAULT, "loc_E58"),
    )


    label("loc_E4C")

    OP_A2(0x1200)
    Jump("loc_E58")

    label("loc_E52")

    OP_A2(0x1201)
    Jump("loc_E58")

    label("loc_E58")

    Return()

    # Function_11_DD2 end

    def Function_12_E59(): pass

    label("Function_12_E59")

    FadeToDark(0, 0, -1)
    OP_6D(-545830, 30000, 755590, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_12_E59 end

    SaveToFile()

Try(main)
