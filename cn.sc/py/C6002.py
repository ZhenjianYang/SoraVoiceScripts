from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C6002   ._SN',
        MapName             = 'Other',
        Location            = 'C6002.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
        Flags               = 0,
        EntryFunctionIndex  = 16,
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
        '目标',                                 # 9
        '原福音',                               # 10
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
        'ED6_DT26/CH20353 ._CH',             # 00
        'ED6_DT26/CH20425 ._CH',             # 01
        'ED6_DT27/CH03000 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT26/CH20353P._CP',             # 00
        'ED6_DT26/CH20425P._CP',             # 01
        'ED6_DT27/CH03000P._CP',             # 02
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65537,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 2000,
        Y                   = 4500,
        Z                   = 19500,
        Range               = 4000,
        Unknown_10          = 0x1964,
        Unknown_14          = 0x4E20,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -12900,
        Y                   = 0,
        Z                   = 2140,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 18,
    )


    DeclActor(
        TriggerX            = 2000,
        TriggerZ            = 2000,
        TriggerY            = 1560,
        TriggerRange        = 1000,
        ActorX              = 2000,
        ActorZ              = 2000,
        ActorY              = 1560,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5200,
        TriggerZ            = 0,
        TriggerY            = 12110,
        TriggerRange        = 1000,
        ActorX              = 5200,
        ActorZ              = 1200,
        ActorY              = 13110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_18A",          # 00, 0
        "Function_1_1BB",          # 01, 1
        "Function_2_216",          # 02, 2
        "Function_3_11A5",         # 03, 3
        "Function_4_11DC",         # 04, 4
        "Function_5_1213",         # 05, 5
        "Function_6_124A",         # 06, 6
        "Function_7_1281",         # 07, 7
        "Function_8_196F",         # 08, 8
        "Function_9_1A67",         # 09, 9
        "Function_10_1ABB",        # 0A, 10
        "Function_11_22FE",        # 0B, 11
        "Function_12_2355",        # 0C, 12
        "Function_13_23A7",        # 0D, 13
        "Function_14_23F9",        # 0E, 14
        "Function_15_244B",        # 0F, 15
        "Function_16_2DCC",        # 10, 16
        "Function_17_35D2",        # 11, 17
        "Function_18_376B",        # 12, 18
        "Function_19_3876",        # 13, 19
        "Function_20_3A34",        # 14, 20
        "Function_21_3AB9",        # 15, 21
        "Function_22_3B4C",        # 16, 22
    )


    def Function_0_18A(): pass

    label("Function_0_18A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_19B")
    OP_A3(0x10F0)
    Event(0, 10)
    Jump("loc_1BA")

    label("loc_19B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1AC")
    OP_A3(0x10F1)
    Event(0, 17)
    Jump("loc_1BA")

    label("loc_1AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_1BA")
    OP_A3(0x10F2)
    Event(0, 19)

    label("loc_1BA")

    Return()

    # Function_0_18A end

    def Function_1_1BB(): pass

    label("Function_1_1BB")

    OP_22(0x1C3, 0x1, 0x64)
    StopSound(0x124F8, 0x493E0, 0x0)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 500)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_END)), "loc_204")
    OP_6F(0x1, 950)
    OP_6F(0x3, 240)

    label("loc_204")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    Return()

    # Function_1_1BB end

    def Function_2_216(): pass

    label("Function_2_216")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A95")
    Fade(500)
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x8, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    Sleep(500)

    def lambda_28D():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28D)
    OP_22(0x13D, 0x0, 0x64)
    OP_73(0x3)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    OP_6D(1980, 2000, 1300, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(205, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x101,
        "#1004F#6P这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#1044F#6P……有东西过来了……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_385():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_385)

    def lambda_39D():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39D)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_3C8():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3C8)
    Sleep(2000)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x6)
    OP_73(0x1)
    OP_23(0x13E)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(500)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)

    ChrTalk(    #2
        0x101,
        "#1004F#6P那、那是什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BB")

    ChrTalk(    #3
        0x105,
        (
            "#1165F#6P看来这就是\x01",
            "『光环轨道』了。\x02\x03",

            "是通过什么样的原理呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC")

    label("loc_4BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_517")

    ChrTalk(    #4
        0x103,
        (
            "#026F#6P呼呼……\x01",
            "看来这就是『光环轨道』了。\x02\x03",

            "是通过什么样的原理呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC")

    label("loc_517")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_578")

    ChrTalk(    #5
        0x106,
        (
            "#053F#6P哟，\x01",
            "看来这就是『光环轨道』了。\x02\x03",

            "虽然不知道是\x01",
            "通过什么样的原理……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC")

    label("loc_578")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D6")

    ChrTalk(    #6
        0x108,
        (
            "#074F#6P呼呼。\x01",
            "看来这就是『光环轨道』了。\x02\x03",

            "什么样的原理倒是无从得知……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC")

    label("loc_5D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_640")

    ChrTalk(    #7
        0x109,
        (
            "#1064F#6P哈……\x01",
            "看来这就是『光环轨道』了。\x02\x03",

            "虽然完全搞不清楚\x01",
            "是通过什么样的原理……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC")

    label("loc_640")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_698")

    ChrTalk(    #8
        0x104,
        (
            "#035F#6P呼，看来这就是\x01",
            "『光环轨道』了。\x02\x03",

            "虽然不了解是什么原理……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC")

    label("loc_698")


    ChrTalk(    #9
        0x102,
        (
            "#1040F#2P看来\x01",
            "这就是『光环轨道』了。\x02\x03",

            "是通过什么样的原理呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74C")

    ChrTalk(    #10
        0x10B,
        (
            "#213F#6P……但感觉和帝国的\x01",
            "铁路有点相似。\x02\x03",

            "#413F不过，透明的轨道\x01",
            "还是令人有点胆战心惊啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B1")

    label("loc_74C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B4")

    ChrTalk(    #11
        0x104,
        (
            "#030F#6P呼，好像是帝国\x01",
            "铁路的进化版一样。\x02\x03",

            "#031F不过透明的轨道\x01",
            "还是相当惊险的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B1")

    label("loc_7B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_822")

    ChrTalk(    #12
        0x109,
        (
            "#1064F#6P好像是一些国家使用的\x01",
            "铁路的进化版。\x02\x03",

            "#1068F不过透明的轨道\x01",
            "很让人感到不安啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B1")

    label("loc_822")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88A")

    ChrTalk(    #13
        0x108,
        (
            "#073F#6P像矿车一样\x01",
            "在轨道上跑的交通工具啊。\x02\x03",

            "#075F透明的轨道还真\x01",
            "让人不放心啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B1")

    label("loc_88A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F0")

    ChrTalk(    #14
        0x106,
        (
            "#555F#6P像矿车一样\x01",
            "在轨道上跑的交通工具啊。\x02\x03",

            "#551F透明的轨道实在\x01",
            "感觉怪怪的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B1")

    label("loc_8F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_954")

    ChrTalk(    #15
        0x103,
        (
            "#020F#6P像矿车一样\x01",
            "在轨道上跑的交通工具。\x02\x03",

            "#524F透明的轨道\x01",
            "总让人有点不安……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B1")

    label("loc_954")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B1")

    ChrTalk(    #16
        0x105,
        (
            "#1164F#6P好像是帝国铁路的\x01",
            "进化版一样。\x02\x03",

            "这透明的轨道\x01",
            "是用什么做出来呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A1C")

    ChrTalk(    #17
        0x107,
        (
            "#064F#6P说、说不定是\x01",
            "在空中展开了某种力场\x01",
            "所形成的轨道……\x02\x03",

            "#067F了、了不起的技术啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1C")


    ChrTalk(    #18
        0x101,
        (
            "#1006F#6P嗯，虽然没什么头绪，\x01",
            "不过既然是一种移动的手段，\x01",
            "就没有不尝试的道理。\x02\x03",

            "#1018F快点坐上去看看吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2205)
    OP_28(0x9D, 0x1, 0x20)
    Jump("loc_10FF")

    label("loc_A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF0")
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x8, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    Sleep(500)

    def lambda_B05():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B05)
    OP_22(0x13D, 0x0, 0x64)
    OP_73(0x3)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(1980, 2000, 1300, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(205, 0)
    OP_0D()

    ChrTalk(    #19
        0x101,
        "#1006F#6P来了……！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_BD3():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BD3)

    def lambda_BEB():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BEB)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_C16():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C16)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x6)
    OP_73(0x1)
    OP_23(0x13E)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)

    ChrTalk(    #20
        0x101,
        (
            "#1006F#6P好了，这样一来总算\x01",
            "可以使用这个东西了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#1040F#6P是啊……\x01",
            "马上试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x220A)
    Jump("loc_10FF")

    label("loc_CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE9")
    Fade(500)
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x8, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    Sleep(500)

    def lambda_D65():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D65)
    OP_22(0x13D, 0x0, 0x64)
    OP_73(0x3)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_DD2():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DD2)

    def lambda_DEA():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DEA)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_E15():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E15)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x6)
    OP_73(0x1)
    OP_23(0x13E)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)

    ChrTalk(    #22
        0x101,
        (
            "#1015F#6P嗯，现在可以来往于\x01",
            "３个车站了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1040F#6P嗯……\x01",
            "变得相当方便了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x220B)
    Jump("loc_10FF")

    label("loc_EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FF")
    Fade(500)
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x8, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    Sleep(500)

    def lambda_F5E():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F5E)
    OP_22(0x13D, 0x0, 0x64)
    OP_73(0x3)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_FCB():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FCB)

    def lambda_FE3():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FE3)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_100E():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_100E)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x6)
    OP_73(0x1)
    OP_23(0x13E)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)

    ChrTalk(    #24
        0x102,
        (
            "#1035F#6P好……\x02\x03",

            "#1040F现在从『卡尔玛丽』\x01",
            "到『中枢塔』都能\x01",
            "方便地来回了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1007F#6P呼……好长的距离啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x220C)
    OP_28(0x9F, 0x1, 0x2)

    label("loc_10FF")

    OP_A2(0x2208)
    OP_28(0x9E, 0x1, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3060, 5000, 18520, 0)
    SetChrPos(0x1, 3060, 5000, 18520, 0)
    SetChrPos(0x2, 3060, 5000, 18520, 0)
    SetChrPos(0x3, 3060, 5000, 18520, 0)
    OP_6D(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_2_216 end

    def Function_3_11A5(): pass

    label("Function_3_11A5")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xA3C, 0x1388, 0x47B8, 0x1388, 0x0)

    def lambda_11D0():

        label("loc_11D0")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_11D0")

    QueueWorkItem2(0xFE, 2, lambda_11D0)
    Return()

    # Function_3_11A5 end

    def Function_4_11DC(): pass

    label("Function_4_11DC")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xE2E, 0x1388, 0x47CC, 0x1388, 0x0)

    def lambda_1207():

        label("loc_1207")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1207")

    QueueWorkItem2(0xFE, 2, lambda_1207)
    Return()

    # Function_4_11DC end

    def Function_5_1213(): pass

    label("Function_5_1213")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0x8C0, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_123E():

        label("loc_123E")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_123E")

    QueueWorkItem2(0xFE, 2, lambda_123E)
    Return()

    # Function_5_1213 end

    def Function_6_124A(): pass

    label("Function_6_124A")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xFE6, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_1275():

        label("loc_1275")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1275")

    QueueWorkItem2(0xFE, 2, lambda_1275)
    Return()

    # Function_6_124A end

    def Function_7_1281(): pass

    label("Function_7_1281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128A")
    Return()

    label("loc_128A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1697")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160A")
    EventBegin(0x0)
    Fade(500)
    OP_6D(3080, 5110, 21340, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2620, 5000, 18360, 0)
    SetChrPos(0x102, 3630, 5000, 18380, 0)
    SetChrPos(0xF8, 2240, 5000, 17190, 0)
    SetChrPos(0xF9, 4070, 5000, 17190, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #26
        (
            "\x07\x05现在其它车站的紧急运行\x01",
            "模式尚未启动。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("合成音")

    AnonymousTalk(    #27
        "\x07\x05『光环轨道』无法使用。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E5")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1419")

    label("loc_13E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1407")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1419")

    label("loc_1407")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_1419")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143B")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_146F")

    label("loc_143B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145D")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_146F")

    label("loc_145D")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_146F")

    Sleep(1000)
    OP_63(0x101)
    OP_63(0x102)
    OP_63(0xF8)
    OP_63(0xF9)
    Sleep(500)

    ChrTalk(    #28
        0x101,
        "#1019F#6P……怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1035F#6P……看来不启动其它\x01",
            "车站的『紧急运行模式』的话\x01",
            "就不能使用这个来移动了。\x02\x03",

            "#1040F很遗憾，\x01",
            "现在只能放弃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1007F#6P唔～……\x01",
            "害我空欢喜了一场。\x02\x03",

            "#1015F没办法，先找其他路线吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x220E)
    OP_28(0x9D, 0x1, 0x40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3060, 5000, 18520, 0)
    SetChrPos(0x1, 3060, 5000, 18520, 0)
    SetChrPos(0x2, 3060, 5000, 18520, 0)
    SetChrPos(0x3, 3060, 5000, 18520, 0)
    OP_6D(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_1694")

    label("loc_160A")

    EventBegin(0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #31
        (
            "\x07\x05现在其它车站的紧急运行\x01",
            "模式尚未启动。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("合成音")

    AnonymousTalk(    #32
        "\x07\x05『光环轨道』无法使用。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_1694")

    Jump("loc_196E")

    label("loc_1697")

    EventBegin(0x0)
    Fade(500)
    OP_6D(3080, 5110, 21340, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2620, 5000, 18360, 0)
    SetChrPos(0x102, 3630, 5000, 18380, 0)
    SetChrPos(0xF8, 2240, 5000, 17190, 0)
    SetChrPos(0xF9, 4070, 5000, 17190, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_END)), "loc_1774")
    OP_CC(0x1, 0x0, "【西卡尔玛丽站】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_END)), "loc_179D")
    OP_CC(0x1, 0x0, "【第３５克雷德尔站】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_179D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_END)), "loc_17C0")
    OP_CC(0x1, 0x0, "【中枢塔前站】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_17C0")

    OP_CC(0x1, 0x0, "【放弃使用】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1803")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1885")

    label("loc_1803")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_180D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1885")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1827")
    Jump("loc_1885")

    label("loc_1827")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1878")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1861")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_185E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_185E")

    Jump("loc_1878")

    label("loc_1861")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1827")

    label("loc_1878")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_180D")

    label("loc_1885")

    SetMapFlags(0x100000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_18A3"),
        (1, "loc_18E1"),
        (2, "loc_191F"),
        (3, "loc_195D"),
        (SWITCH_DEFAULT, "loc_1960"),
    )


    label("loc_18A3")

    OP_A2(0x2212)
    OP_A2(0x2214)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_18B6():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18B6)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1960")

    label("loc_18E1")

    OP_A2(0x2212)
    OP_A2(0x2215)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_18F4():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18F4)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1960")

    label("loc_191F")

    OP_A2(0x2212)
    OP_A2(0x2217)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_1932():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1932)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1960")

    label("loc_195D")

    Jump("loc_1960")

    label("loc_1960")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    EventEnd(0x0)

    label("loc_196E")

    Return()

    # Function_7_1281 end

    def Function_8_196F(): pass

    label("Function_8_196F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_43(0x101, 0x2, 0x0, 0x9)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x9)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x9)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x9)
    Sleep(1500)
    OP_6F(0x1, 950)
    OP_70(0x1, 0x44C)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 5)), scpexpr(EXPR_END)), "loc_1A1B")
    OP_6F(0x1, 1100)
    OP_70(0x1, 0x514)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_19E6():
        OP_6D(8300, 5000, 21350, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19E6)

    def lambda_19FE():
        OP_6C(12000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19FE)

    def lambda_1A0E():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1A0E)
    Jump("loc_1A56")

    label("loc_1A1B")

    OP_6F(0x1, 300)
    OP_70(0x1, 0x1F4)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_1A34():
        OP_6D(-2860, 5000, 21710, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A34)

    def lambda_1A4C():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A4C)

    label("loc_1A56")

    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_8_196F end

    def Function_9_1A67(): pass

    label("Function_9_1A67")

    OP_8E(0xFE, 0xC08, 0x1388, 0x4A56, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC2, 0x13F6, 0x4F6A, 0x7D0, 0x0)

    def lambda_1A95():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1A95)
    OP_8E(0xFE, 0xC1C, 0x13F6, 0x5E9C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_1A67 end

    def Function_10_1ABB(): pass

    label("Function_10_1ABB")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(3100, 5110, 23900, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 3050, 5110, 21510, 180)
    SetChrPos(0x102, 3050, 5110, 21510, 180)
    SetChrPos(0xF8, 3050, 5110, 21510, 180)
    SetChrPos(0xF9, 3050, 5110, 21510, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 3)), scpexpr(EXPR_END)), "loc_1BC4")
    OP_6D(-9950, 5000, 20680, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_1BAF():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BAF)
    Jump("loc_1C3C")

    label("loc_1BC4")

    OP_6D(12690, 5000, 20450, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 1300)
    OP_70(0x1, 0x640)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_1C1A():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C1A)

    def lambda_1C32():
        OP_6C(0, 5500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C32)

    label("loc_1C3C")

    OP_A3(0x2210)
    OP_A3(0x2211)
    OP_A3(0x2212)
    OP_A3(0x2213)
    FadeToBright(1000, 0)
    OP_73(0x1)
    OP_23(0x13E)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F4")
    OP_43(0x101, 0x1, 0x0, 0xB)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0xC)
    Sleep(800)

    def lambda_1C98():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C98)

    def lambda_1CB0():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CB0)
    OP_43(0xF8, 0x1, 0x0, 0xD)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0xE)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #33
        0x101,
        (
            "#1004F#4P好、好像一转眼\x01",
            "就到了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#1035F#6P速度很快，\x01",
            "却几乎没有摇晃……\x02\x03",

            "#1040F真是了不起的技术。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1015F#4P确实如此……\x02\x03",

            "#1016F不过难得有那么棒的景色，\x01",
            "真希望它能跑得慢一点\x01",
            "让我好好欣赏一下……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E09")

    ChrTalk(    #36
        0x10B,
        (
            "#413F#5P真是的……\x01",
            "你还真是悠哉啊。\x02\x03",

            "#210F……不过确实也\x01",
            "有点可惜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2E")

    label("loc_1E09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E43")

    ChrTalk(    #37
        0x107,
        (
            "#067F#5P嘿嘿……\x01",
            "的确可以这么说呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2E")

    label("loc_1E43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E78")

    ChrTalk(    #38
        0x105,
        (
            "#1168F#5P呵呵……\x01",
            "确实是这样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2E")

    label("loc_1E78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EA7")

    ChrTalk(    #39
        0x103,
        "#021F#5P呵呵……有道理。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F2E")

    label("loc_1EA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ED3")

    ChrTalk(    #40
        0x109,
        "#1061F#5P哈哈，没错～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F2E")

    label("loc_1ED3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F04")

    ChrTalk(    #41
        0x104,
        "#031F#5P呵呵……我有同感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F2E")

    label("loc_1F04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F2E")

    ChrTalk(    #42
        0x108,
        "#071F#5P哈哈……没错。\x02",
    )

    CloseMessageWindow()

    label("loc_1F2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F95")

    ChrTalk(    #43
        0x106,
        (
            "#051F#5P不过，多亏有这东西，\x01",
            "探索变得轻松许多了。\x02\x03",

            "发现了新的车站\x01",
            "就赶快启用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EE")

    label("loc_1F95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF6")

    ChrTalk(    #44
        0x108,
        (
            "#070F#5P不过，有了这东西\x01",
            "探索就方便得多了。\x02\x03",

            "发现了新的车站\x01",
            "就赶快启用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EE")

    label("loc_1FF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_205E")

    ChrTalk(    #45
        0x104,
        (
            "#035F#5P呵呵，有了这个\x01",
            "探索就方便得多了。\x02\x03",

            "#030F发现了新的车站\x01",
            "还真想赶快启用啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EE")

    label("loc_205E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20BE")

    ChrTalk(    #46
        0x109,
        (
            "#1060F#5P不过，有了这个\x01",
            "探索就方便得多了。\x02\x03",

            "发现了新的车站\x01",
            "就赶快启用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EE")

    label("loc_20BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_211D")

    ChrTalk(    #47
        0x103,
        (
            "#027F#5P不过，有了这个\x01",
            "探索就方便得多了。\x02\x03",

            "发现了新的车站\x01",
            "就赶快启用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EE")

    label("loc_211D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2187")

    ChrTalk(    #48
        0x105,
        (
            "#1167F#5P不过，有了这个\x01",
            "探索就方便得多了。\x02\x03",

            "#1168F发现了新的车站\x01",
            "还真想赶快启用呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EE")

    label("loc_2187")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21EE")

    ChrTalk(    #49
        0x107,
        (
            "#061F#5P嘿嘿，不过有了这个\x01",
            "探索就轻松许多了阿⊙\x02\x03",

            "#560F发现了新的车站\x01",
            "就赶快启用吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21EE")

    OP_A2(0x220F)
    Jump("loc_224C")

    label("loc_21F4")

    OP_43(0x101, 0x1, 0x0, 0xB)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0xC)
    Sleep(800)

    def lambda_2212():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2212)

    def lambda_222A():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_222A)
    OP_43(0xF8, 0x1, 0x0, 0xD)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0xE)
    Sleep(500)

    label("loc_224C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)
    SetChrPos(0x0, 3060, 5000, 18520, 180)
    SetChrPos(0x1, 3060, 5000, 18520, 180)
    SetChrPos(0x2, 3060, 5000, 18520, 180)
    SetChrPos(0x3, 3060, 5000, 18520, 180)
    OP_6D(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    ClearMapFlags(0x100000)
    Return()

    # Function_10_1ABB end

    def Function_11_22FE(): pass

    label("Function_11_22FE")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2314():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2314)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xECE, 0x1388, 0x4376, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    ClearChrFlags(0xFE, 0x80)
    Return()

    # Function_11_22FE end

    def Function_12_2355(): pass

    label("Function_12_2355")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_236B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_236B)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9F6, 0x1388, 0x4362, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_2355 end

    def Function_13_23A7(): pass

    label("Function_13_23A7")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_23BD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23BD)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1086, 0x1388, 0x4808, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_13_23A7 end

    def Function_14_23F9(): pass

    label("Function_14_23F9")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_240F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_240F)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7B2, 0x1388, 0x47A4, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_14_23F9 end

    def Function_15_244B(): pass

    label("Function_15_244B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2470")
    Call(0, 20)
    Call(0, 21)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_2470")

    Fade(500)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2480, 2000, 500, 0)
    SetChrPos(0x102, 1480, 2000, 500, 0)
    SetChrPos(0xF8, 2450, 1600, -1400, 0)
    SetChrPos(0xF9, 1560, 1600, -1220, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 78, 34, 12)

    AnonymousTalk(    #50
        (
            "\x07\x05#1S『光环轨道』第７法克特里亚站\x01\x01\x01",
            "※现在『光环轨道』的运行受到了\x01",
            "  大幅度的限制。麻烦请您在本终端\x01",
            "  手动输入我们可以为您提供的服务。\x01\x01\x01",
            "『利贝尔·方舟』市·交通管理中心\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D1E")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        20,
        100,
        0,
        (
            "【法克特里亚向导】\x01",      # 0
            "【使用光环轨道】\x01",        # 1
            "【网络商城】\x01",            # 2
            "【解除门锁】\x01",            # 3
            "【停止服务】\x01",            # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_264B"),
        (1, "loc_2735"),
        (2, "loc_2859"),
        (3, "loc_2876"),
        (4, "loc_2D01"),
        (SWITCH_DEFAULT, "loc_2D0E"),
    )


    label("loc_264B")


    AnonymousTalk(    #51
        (
            "\x07\x05#1S『法克特里亚』是\x01",
            "位于利贝尔·方舟市东区的\x01",
            "工业计划区域。\x01\x01",
            "食品、服装、医疗、机械、住宅等\x01",
            "城市生活所需的各类工业产品\x01",
            "都由区内的工厂负责制造。\x01\x01",
            "此外，在６４个区域当中，\x01",
            "第１到第８区内设有港湾设施，\x01",
            "成为了都市之间贸易的窗口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D1B")

    label("loc_2735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F3")

    AnonymousTalk(    #52
        (
            "\x07\x05#1S现在『光环轨道』的运行受到了\x01",
            "大幅度的限制。\x01\x01",
            "要启动『第７法克特里亚站』的\x01",
            "紧急运行模式吗？\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        1,
        130,
        240,
        0,
        (
            "【启动】\x01",        # 0
            "【不启动】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27D1"),
        (1, "loc_27EA"),
        (SWITCH_DEFAULT, "loc_27F0"),
    )


    label("loc_27D1")

    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Call(0, 2)
    Return()

    label("loc_27EA")

    OP_5F(0x1)
    Jump("loc_27F0")

    label("loc_27F0")

    Jump("loc_2856")

    label("loc_27F3")


    AnonymousTalk(    #53
        (
            "\x07\x05#1S现在『光环轨道』的运行受到了\x01",
            "大幅度的限制。\x01\x01",
            "『第７法克特里亚站』的紧急运行\x01",
            "模式已经启动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2856")

    Jump("loc_2D1B")

    label("loc_2859")

    FadeToBright(300, 0)

    AnonymousTalk(    #54
        "\x07\x05\x02",
    )

    OP_A9(0xF2)
    FadeToDark(300, 0, 100)
    Jump("loc_2D1B")

    label("loc_2876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC8")

    AnonymousTalk(    #55
        (
            "\x07\x05#1S当『光环轨道』\x01",
            "由于各种原因而无法使用时，\x01",
            "可以解除车站周边大门的锁定\x01",
            "并进入地下通道之中。\x01\x01",
            "【警告】\x01",
            "根据来自『中枢塔』的指示，\x01",
            "安全等级提高了。\x01\x01",
            "请在此终端前使用\x01",
            "您携带的『福音』之后\x01",
            "输入密码。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_56(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AC1")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇第一次调查的情况下】\x01",                                           # 0
            "【◇第二次（以上）调查的情况下（没向吉尔打听&空贼团救出前）】\x01",      # 1
            "【◇第二次（以上）调查的情况下（没向吉尔打听&空贼团救出后）】\x01",      # 2
            "【◇第二次（以上）调查的情况下（已向吉尔打听）】\x01",                   # 3
            "【◇什么也没有变更】\x01",                                               # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A91"),
        (1, "loc_2A9D"),
        (2, "loc_2AA9"),
        (3, "loc_2AB5"),
        (SWITCH_DEFAULT, "loc_2AC1"),
    )


    label("loc_2A91")

    OP_A3(0x221F)
    OP_A3(0x222D)
    OP_A3(0x222C)
    Jump("loc_2AC1")

    label("loc_2A9D")

    OP_A2(0x221F)
    OP_A3(0x222D)
    OP_A3(0x222C)
    Jump("loc_2AC1")

    label("loc_2AA9")

    OP_A2(0x221F)
    OP_A3(0x222D)
    OP_A2(0x222C)
    Jump("loc_2AC1")

    label("loc_2AB5")

    OP_A2(0x221F)
    OP_A2(0x222D)
    OP_A2(0x222C)
    Jump("loc_2AC1")

    label("loc_2AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B5A")

    ChrTalk(    #56
        0x101,
        "#1004F#6P密、密码是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        (
            "#1035F#6P受到网络管理中枢的\x01",
            "操作了吗……\x02\x03",

            "#1042F看来『结社』对这座城市的\x01",
            "功能掌握得相当透彻。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #58
        "\x07\x05\x02",
    )

    Jump("loc_2CB2")

    label("loc_2B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC4")

    ChrTalk(    #59
        0x102,
        (
            "#1035F#6P……现在只能\x01",
            "不管这个终端了。\x02\x03",

            "#1040F等发现了什么线索\x01",
            "再来这里吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #60
        "\x07\x05\x02",
    )

    Jump("loc_2CB2")

    label("loc_2BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C44")

    ChrTalk(    #61
        0x102,
        (
            "#1035F#6P如果『结社』\x01",
            "最近设置了密码的话\x01",
            "仅凭我们手头的情报恐怕不够。\x02\x03",

            "#1040F如果有人知道的话……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #62
        "\x07\x05\x02",
    )

    Jump("loc_2CB2")

    label("loc_2C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 5)), scpexpr(EXPR_END)), "loc_2CB2")

    ChrTalk(    #63
        0x102,
        (
            "#1040F#6P我想应该试试\x01",
            "吉尔先生提供的情报。\x02\x03",

            "在终端前使用『福音』之后\x01",
            "说出那个词吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #64
        "\x07\x05\x02",
    )


    label("loc_2CB2")

    OP_A2(0x221F)
    OP_28(0x9E, 0x1, 0x2)
    FadeToDark(300, 0, 100)
    Jump("loc_2CFE")

    label("loc_2CC8")


    AnonymousTalk(    #65
        (
            "\x07\x05#1S现在第７法克特里亚站附近的\x01",
            "大门锁定已经解除。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CFE")

    Jump("loc_2D1B")

    label("loc_2D01")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1B")

    label("loc_2D0E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1B")

    label("loc_2D1B")

    Jump("loc_25C1")

    label("loc_2D1E")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(100, 0)
    Sleep(100)
    Fade(500)
    OP_6D(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, 2020, 2000, 40, 180)
    SetChrPos(0x1, 2020, 2000, 40, 180)
    SetChrPos(0x2, 2020, 2000, 40, 180)
    SetChrPos(0x3, 2020, 2000, 40, 180)
    EventEnd(0x0)
    Return()

    # Function_15_244B end

    def Function_16_2DCC(): pass

    label("Function_16_2DCC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x40F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DD9")
    Return()

    label("loc_2DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15E0), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3134")
    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_48()
    EventBegin(0x0)
    Fade(1000)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2480, 2000, 500, 0)
    SetChrPos(0x102, 1480, 2000, 500, 0)
    SetChrPos(0xF8, 2450, 1600, -1400, 0)
    SetChrPos(0xF9, 1560, 1600, -1220, 0)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #66
        (
            "\x07\x05【警告】\x01",
            "根据来自『中枢塔』的指示，\x01",
            "安全等级提高了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #67
        (
            "\x07\x05麻烦请在此终端前\x01",
            "输入密码。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD9")

    ChrTalk(    #68
        0x101,
        "#1004F#6P密、密码是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        (
            "#1035F#6P受到网络管理中枢的\x01",
            "操作了吗……\x02\x03",

            "#1042F看来『结社』对这座城市的\x01",
            "功能掌握得相当透彻。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x221F)
    Jump("loc_30A4")

    label("loc_2FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3035")

    ChrTalk(    #70
        0x102,
        (
            "#1035F#6P……现在只能\x01",
            "不管这个终端了。\x02\x03",

            "#1040F等发现了什么线索\x01",
            "再来这里吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A4")

    label("loc_3035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A4")

    ChrTalk(    #71
        0x102,
        (
            "#1035F#6P如果『结社』\x01",
            "最近设置了密码的话\x01",
            "仅凭我们手头的情报恐怕不够。\x02\x03",

            "#1040F如果有人知道的话……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A4")

    Sleep(100)
    Fade(500)
    OP_6D(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, 2020, 2000, 40, 180)
    SetChrPos(0x1, 2020, 2000, 40, 180)
    SetChrPos(0x2, 2020, 2000, 40, 180)
    SetChrPos(0x3, 2020, 2000, 40, 180)
    EventEnd(0x0)
    Jump("loc_35D1")

    label("loc_3134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15E0), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3581")
    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_48()
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31B7")
    Call(0, 20)
    Call(0, 21)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_31B7")

    Fade(1000)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2730, 2000, 270, 315)
    SetChrPos(0x102, 1150, 2000, 310, 45)
    SetChrPos(0xF8, 2430, 1600, -1200, 0)
    SetChrPos(0xF9, 1550, 1600, -1200, 0)
    OP_0D()
    Sleep(1000)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 9)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 1)
    SetChrPos(0x9, 2400, 2650, 500, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x1, "map\\\\mp007_00.eff")
    OP_22(0x90, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x9, 0, 150, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_82(0x0, 0x2)
    OP_23(0x90)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #72
        "\x07\x05福音已经确认。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #73
        (
            "\x07\x05请您于控制台\x01",
            "输入密码。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x9, 0x80)
    OP_0D()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #74
        "\x18\x07\x05输入密码\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【Ｏ．Ｒ．Ｆ．Ｅ．Ｕ．Ｈ．Ｓ】\x01",      # 0
            "【Ｏ．Ｒ．Ｐ．Ｈ．Ｅ．Ｕ．Ｓ】\x01",      # 1
            "【Ｏ．Ｌ．Ｐ．Ｈ．Ｅ．Ｕ．Ｓ】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_342F"),
        (2, "loc_342F"),
        (1, "loc_3541"),
        (SWITCH_DEFAULT, "loc_357E"),
    )


    label("loc_342F")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #75
        "\x07\x05密码错误。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("合成音")

    AnonymousTalk(    #76
        (
            "\x07\x05请再次使用『福音』并输入\x01",
            "正确的密码。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    Fade(500)
    OP_6D(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrPos(0x0, 2020, 2000, 40, 180)
    SetChrPos(0x1, 2020, 2000, 40, 180)
    SetChrPos(0x2, 2020, 2000, 40, 180)
    SetChrPos(0x3, 2020, 2000, 40, 180)
    EventEnd(0x0)
    EventEnd(0x0)
    Jump("loc_357E")

    label("loc_3541")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #77
        "\x07\x05密码确认。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5701   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_357E")

    label("loc_357E")

    Jump("loc_35D1")

    label("loc_3581")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_48()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #78
        "\x07\x05什么也没发生……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    ClearMapFlags(0x80)
    Return()

    label("loc_35D1")

    Return()

    # Function_16_2DCC end

    def Function_17_35D2(): pass

    label("Function_17_35D2")

    EventBegin(0x0)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2480, 2000, 500, 0)
    SetChrPos(0x102, 1480, 2000, 500, 0)
    SetChrPos(0xF8, 2450, 1600, -1400, 0)
    SetChrPos(0xF9, 1560, 1600, -1220, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #79
        (
            "\x07\x05本站附近的大门锁定\x01",
            "已经解除。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("合成音")

    AnonymousTalk(    #80
        "\x07\x05地下通道２４６号已经可以使用了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    Fade(500)
    OP_6D(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, 2020, 2000, 40, 180)
    SetChrPos(0x1, 2020, 2000, 40, 180)
    SetChrPos(0x2, 2020, 2000, 40, 180)
    SetChrPos(0x3, 2020, 2000, 40, 180)
    OP_0D()
    OP_A2(0x222E)
    OP_28(0x9E, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_17_35D2 end

    def Function_18_376B(): pass

    label("Function_18_376B")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-13000, 0, 2000, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_89(0x101, -12000, 0, 2000, 90)
    OP_89(0x102, -13000, 0, 3000, 90)
    OP_89(0xF8, -13000, 0, 1000, 90)
    OP_89(0xF9, -14000, 0, 2000, 90)
    OP_0D()
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x4B0)

    def lambda_3817():
        OP_6D(-13000, -25000, 490, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3817)

    def lambda_382F():
        OP_67(0, 3890, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_382F)

    def lambda_3847():
        OP_6B(5200, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3847)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x1C3)
    Sleep(500)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5701   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_18_376B end

    def Function_19_3876(): pass

    label("Function_19_3876")

    EventBegin(0x0)
    OP_6D(-13000, -12750, 490, 0)
    OP_67(0, 3890, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    OP_6F(0x0, 300)
    OP_48()
    OP_89(0x101, -12000, -23000, 2000, 90)
    OP_89(0x102, -13000, -23000, 3000, 90)
    OP_89(0xF8, -13000, -23000, 1000, 90)
    OP_89(0xF9, -14000, -23000, 2000, 90)
    OP_22(0xEB, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_70(0x0, 0x0)

    def lambda_391C():
        OP_6D(-13000, 0, 2000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_391C)

    def lambda_3934():
        OP_67(0, 3880, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3934)
    Sleep(4000)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    OP_73(0x0)
    Sleep(200)
    Fade(500)
    OP_6D(-7000, 0, 2000, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, -7000, 0, 2000, 90)
    SetChrPos(0x1, -7000, 0, 2000, 90)
    SetChrPos(0x2, -7000, 0, 2000, 90)
    SetChrPos(0x3, -7000, 0, 2000, 90)
    OP_0D()
    OP_A2(0x222F)
    EventEnd(0x0)
    Return()

    # Function_19_3876 end

    def Function_20_3A34(): pass

    label("Function_20_3A34")

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
            "【◇阿加特在队伍中】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3AAC"),
        (1, "loc_3AB2"),
        (SWITCH_DEFAULT, "loc_3AB8"),
    )


    label("loc_3AAC")

    OP_A2(0x1200)
    Jump("loc_3AB8")

    label("loc_3AB2")

    OP_A2(0x1201)
    Jump("loc_3AB8")

    label("loc_3AB8")

    Return()

    # Function_20_3A34 end

    def Function_21_3AB9(): pass

    label("Function_21_3AB9")

    FadeToDark(0, 0, -1)
    OP_6D(-545830, 30000, 755590, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_21_3AB9 end

    def Function_22_3B4C(): pass

    label("Function_22_3B4C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #81
        (
            "\x07\x05≡ 前面的月台\x01",
            "　　　第７法克特里亚站\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_3B4C end

    SaveToFile()

Try(main)
