from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C6001   ._SN',
        MapName             = 'Other',
        Location            = 'C6001.x',
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
    )

    AddCharChipPat(
        'ED6_DT26/CH20353P._CP',             # 00
        'ED6_DT26/CH20425P._CP',             # 01
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
        "Function_0_182",          # 00, 0
        "Function_1_1B3",          # 01, 1
        "Function_2_20E",          # 02, 2
        "Function_3_119B",         # 03, 3
        "Function_4_11D2",         # 04, 4
        "Function_5_1209",         # 05, 5
        "Function_6_1240",         # 06, 6
        "Function_7_1277",         # 07, 7
        "Function_8_1974",         # 08, 8
        "Function_9_1A6C",         # 09, 9
        "Function_10_1AC0",        # 0A, 10
        "Function_11_2305",        # 0B, 11
        "Function_12_235C",        # 0C, 12
        "Function_13_23AE",        # 0D, 13
        "Function_14_2400",        # 0E, 14
        "Function_15_2452",        # 0F, 15
        "Function_16_2DD8",        # 10, 16
        "Function_17_2FD3",        # 11, 17
        "Function_18_315F",        # 12, 18
        "Function_19_326A",        # 13, 19
        "Function_20_3425",        # 14, 20
        "Function_21_34AC",        # 15, 21
        "Function_22_353F",        # 16, 22
    )


    def Function_0_182(): pass

    label("Function_0_182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_193")
    OP_A3(0x10F0)
    Event(0, 10)
    Jump("loc_1B2")

    label("loc_193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1A4")
    OP_A3(0x10F1)
    Event(0, 17)
    Jump("loc_1B2")

    label("loc_1A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_1B2")
    OP_A3(0x10F2)
    Event(0, 19)

    label("loc_1B2")

    Return()

    # Function_0_182 end

    def Function_1_1B3(): pass

    label("Function_1_1B3")

    OP_22(0x1C3, 0x1, 0x64)
    StopSound(0x124F8, 0x493E0, 0x0)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 500)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_END)), "loc_1FC")
    OP_6F(0x1, 950)
    OP_6F(0x3, 240)

    label("loc_1FC")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    Return()

    # Function_1_1B3 end

    def Function_2_20E(): pass

    label("Function_2_20E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8D")
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

    def lambda_285():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_285)
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

    def lambda_37D():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_37D)

    def lambda_395():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_395)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_3C0():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3C0)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B3")

    ChrTalk(    #3
        0x105,
        (
            "#1165F#6P看来这就是\x01",
            "『光环轨道』了。\x02\x03",

            "是通过什么样的原理呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4")

    label("loc_4B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50F")

    ChrTalk(    #4
        0x103,
        (
            "#026F#6P呼呼……\x01",
            "看来这就是『光环轨道』了。\x02\x03",

            "是通过什么样的原理呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4")

    label("loc_50F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_570")

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
    Jump("loc_6D4")

    label("loc_570")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CE")

    ChrTalk(    #6
        0x108,
        (
            "#074F#6P呼呼。\x01",
            "看来这就是『光环轨道』了。\x02\x03",

            "什么样的原理倒是无从得知……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4")

    label("loc_5CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_638")

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
    Jump("loc_6D4")

    label("loc_638")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_690")

    ChrTalk(    #8
        0x104,
        (
            "#035F#6P呼，看来这就是\x01",
            "『光环轨道』了。\x02\x03",

            "虽然不了解是什么原理……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4")

    label("loc_690")


    ChrTalk(    #9
        0x102,
        (
            "#1040F#2P看来\x01",
            "这就是『光环轨道』了。\x02\x03",

            "是通过什么样的原理呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_744")

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
    Jump("loc_9A9")

    label("loc_744")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AE")

    ChrTalk(    #11
        0x104,
        (
            "#030F#6P呼，好像是帝国\x01",
            "铁路的进化版一样。\x02\x03",

            "#031F不过，透明的轨道\x01",
            "还是相当惊险的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A9")

    label("loc_7AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_818")

    ChrTalk(    #12
        0x109,
        (
            "#1064F#6P好像是一些国家使用的\x01",
            "铁路的进化版。\x02\x03",

            "#1068F透明的轨道\x01",
            "很让人感到不安啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A9")

    label("loc_818")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_880")

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
    Jump("loc_9A9")

    label("loc_880")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E6")

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
    Jump("loc_9A9")

    label("loc_8E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_94A")

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
    Jump("loc_9A9")

    label("loc_94A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A9")

    ChrTalk(    #16
        0x105,
        (
            "#1164F#6P好像是帝国铁路的\x01",
            "进化版一样。\x02\x03",

            "这透明的轨道\x01",
            "是用什么做出来的呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A14")

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

    label("loc_A14")


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
    Jump("loc_10F5")

    label("loc_A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE6")
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

    def lambda_AFD():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AFD)
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

    def lambda_BCB():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BCB)

    def lambda_BE3():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BE3)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_C0E():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C0E)
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
            "马上试试吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x220A)
    Jump("loc_10F5")

    label("loc_CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDF")
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

    def lambda_D5B():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D5B)
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

    def lambda_DC8():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DC8)

    def lambda_DE0():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DE0)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_E0B():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E0B)
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
    Jump("loc_10F5")

    label("loc_EDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F5")
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

    def lambda_F54():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F54)
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

    def lambda_FC1():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FC1)

    def lambda_FD9():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FD9)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_1004():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1004)
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

    label("loc_10F5")

    OP_A2(0x2207)
    OP_28(0x9D, 0x1, 0x200)
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

    # Function_2_20E end

    def Function_3_119B(): pass

    label("Function_3_119B")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xA3C, 0x1388, 0x47B8, 0x1388, 0x0)

    def lambda_11C6():

        label("loc_11C6")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_11C6")

    QueueWorkItem2(0xFE, 2, lambda_11C6)
    Return()

    # Function_3_119B end

    def Function_4_11D2(): pass

    label("Function_4_11D2")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xE2E, 0x1388, 0x47CC, 0x1388, 0x0)

    def lambda_11FD():

        label("loc_11FD")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_11FD")

    QueueWorkItem2(0xFE, 2, lambda_11FD)
    Return()

    # Function_4_11D2 end

    def Function_5_1209(): pass

    label("Function_5_1209")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0x8C0, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_1234():

        label("loc_1234")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1234")

    QueueWorkItem2(0xFE, 2, lambda_1234)
    Return()

    # Function_5_1209 end

    def Function_6_1240(): pass

    label("Function_6_1240")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xFE6, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_126B():

        label("loc_126B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_126B")

    QueueWorkItem2(0xFE, 2, lambda_126B)
    Return()

    # Function_6_1240 end

    def Function_7_1277(): pass

    label("Function_7_1277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1280")
    Return()

    label("loc_1280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_169C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160F")
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
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E0")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1414")

    label("loc_13E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1402")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1414")

    label("loc_1402")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_1414")

    Sleep(50)
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

    Sleep(1500)
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
    Sleep(200)
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
    Jump("loc_1699")

    label("loc_160F")

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

    label("loc_1699")

    Jump("loc_1973")

    label("loc_169C")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_END)), "loc_1779")
    OP_CC(0x1, 0x0, "【西卡尔玛丽站】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_END)), "loc_17A2")
    OP_CC(0x1, 0x0, "【第７法克特里亚站】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_17A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_END)), "loc_17C5")
    OP_CC(0x1, 0x0, "【中枢塔前站】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_17C5")

    OP_CC(0x1, 0x0, "【放弃使用】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1808")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_188A")

    label("loc_1808")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1812")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_188A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182C")
    Jump("loc_188A")

    label("loc_182C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_187D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1866")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1863")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1863")

    Jump("loc_187D")

    label("loc_1866")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_182C")

    label("loc_187D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1812")

    label("loc_188A")

    SetMapFlags(0x100000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_18A8"),
        (1, "loc_18E6"),
        (2, "loc_1924"),
        (3, "loc_1962"),
        (SWITCH_DEFAULT, "loc_1965"),
    )


    label("loc_18A8")

    OP_A2(0x2211)
    OP_A2(0x2214)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_18BB():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18BB)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1965")

    label("loc_18E6")

    OP_A2(0x2211)
    OP_A2(0x2216)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_18F9():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18F9)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1965")

    label("loc_1924")

    OP_A2(0x2211)
    OP_A2(0x2217)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_1937():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1937)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1965")

    label("loc_1962")

    Jump("loc_1965")

    label("loc_1965")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    EventEnd(0x0)

    label("loc_1973")

    Return()

    # Function_7_1277 end

    def Function_8_1974(): pass

    label("Function_8_1974")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 4)), scpexpr(EXPR_END)), "loc_1A10")
    OP_6F(0x1, 300)
    OP_70(0x1, 0x1F4)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_19EB():
        OP_6D(-2860, 5000, 21710, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19EB)

    def lambda_1A03():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A03)
    Jump("loc_1A5B")

    label("loc_1A10")

    OP_6F(0x1, 1100)
    OP_70(0x1, 0x514)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_1A29():
        OP_6D(8300, 5000, 21350, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A29)

    def lambda_1A41():
        OP_6C(12000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A41)

    def lambda_1A51():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1A51)

    label("loc_1A5B")

    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_8_1974 end

    def Function_9_1A6C(): pass

    label("Function_9_1A6C")

    OP_8E(0xFE, 0xC08, 0x1388, 0x4A56, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC2, 0x13F6, 0x4F6A, 0x7D0, 0x0)

    def lambda_1A9A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1A9A)
    OP_8E(0xFE, 0xC1C, 0x13F6, 0x5E9C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_1A6C end

    def Function_10_1AC0(): pass

    label("Function_10_1AC0")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 2)), scpexpr(EXPR_END)), "loc_1BD9")
    OP_6D(12690, 5000, 20450, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 1300)
    OP_70(0x1, 0x640)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_1BB4():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BB4)

    def lambda_1BCC():
        OP_6C(0, 5500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BCC)
    Jump("loc_1C41")

    label("loc_1BD9")

    OP_6D(-9950, 5000, 20680, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_1C2F():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C2F)

    label("loc_1C41")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FB")
    OP_43(0x101, 0x1, 0x0, 0xB)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0xC)
    Sleep(800)

    def lambda_1C9D():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C9D)

    def lambda_1CB5():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CB5)
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
            "真想它能跑得慢一点，\x01",
            "让我好好欣赏一下……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E0E")

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
    Jump("loc_1F33")

    label("loc_1E0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E48")

    ChrTalk(    #37
        0x107,
        (
            "#067F#5P嘿嘿……\x01",
            "的确可以这么说呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1E48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E7D")

    ChrTalk(    #38
        0x105,
        (
            "#1168F#5P呵呵……\x01",
            "确实是这样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1E7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EAC")

    ChrTalk(    #39
        0x103,
        "#021F#5P呵呵……有道理。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ED8")

    ChrTalk(    #40
        0x109,
        "#1061F#5P哈哈，没错～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1ED8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F09")

    ChrTalk(    #41
        0x104,
        "#031F#5P呵呵……我有同感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1F09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F33")

    ChrTalk(    #42
        0x108,
        "#071F#5P哈哈……没错。\x02",
    )

    CloseMessageWindow()

    label("loc_1F33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F9A")

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
    Jump("loc_21F5")

    label("loc_1F9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFB")

    ChrTalk(    #44
        0x108,
        (
            "#070F#5P不过，有了这个，\x01",
            "探索就轻松许多了。\x02\x03",

            "发现了新的车站\x01",
            "就赶快启用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F5")

    label("loc_1FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2065")

    ChrTalk(    #45
        0x104,
        (
            "#035F#5P呵呵，有了这个\x01",
            "探索就方便得多了。\x02\x03",

            "#030F发现新的车站之后\x01",
            "要赶快将它启动哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F5")

    label("loc_2065")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C5")

    ChrTalk(    #46
        0x109,
        (
            "#1060F#5P不过，有了这个\x01",
            "探索就方便得多了。\x02\x03",

            "发现了新的车站\x01",
            "就赶紧启用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F5")

    label("loc_20C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2124")

    ChrTalk(    #47
        0x103,
        (
            "#027F#5P不过，有了这个\x01",
            "探索就方便得多了。\x02\x03",

            "发现了新的车站\x01",
            "就赶紧启用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F5")

    label("loc_2124")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_218E")

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
    Jump("loc_21F5")

    label("loc_218E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21F5")

    ChrTalk(    #49
        0x107,
        (
            "#061F#5P嘿嘿，不过有了这个\x01",
            "探索就方便得多了阿⊙\x02\x03",

            "#560F发现了新的车站\x01",
            "就赶快启用吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F5")

    OP_A2(0x220F)
    Jump("loc_2253")

    label("loc_21FB")

    OP_43(0x101, 0x1, 0x0, 0xB)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0xC)
    Sleep(800)

    def lambda_2219():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2219)

    def lambda_2231():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2231)
    OP_43(0xF8, 0x1, 0x0, 0xD)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0xE)
    Sleep(500)

    label("loc_2253")

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

    # Function_10_1AC0 end

    def Function_11_2305(): pass

    label("Function_11_2305")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_231B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_231B)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xECE, 0x1388, 0x4376, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    ClearChrFlags(0xFE, 0x80)
    Return()

    # Function_11_2305 end

    def Function_12_235C(): pass

    label("Function_12_235C")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2372():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2372)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9F6, 0x1388, 0x4362, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_235C end

    def Function_13_23AE(): pass

    label("Function_13_23AE")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_23C4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23C4)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1086, 0x1388, 0x4808, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_13_23AE end

    def Function_14_2400(): pass

    label("Function_14_2400")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2416():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2416)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7B2, 0x1388, 0x47A4, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_14_2400 end

    def Function_15_2452(): pass

    label("Function_15_2452")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2477")
    Call(0, 20)
    Call(0, 21)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_2477")

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
            "\x07\x05#1S『光环轨道』第３５克雷德尔站\x01\x01\x01",
            "※现在『光环轨道』的运行受到了\x01",
            "  大幅度的限制。麻烦请您在本终端\x01",
            "  手动输入我们可以为您提供的服务。\x01\x01\x01",
            "『利贝尔·方舟』市·交通管理中心\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D2A")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        20,
        100,
        0,
        (
            "【克雷德尔向导】\x01",      # 0
            "【使用光环轨道】\x01",      # 1
            "【网络商城】\x01",          # 2
            "【解除门锁】\x01",          # 3
            "【停止服务】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2650"),
        (1, "loc_274B"),
        (2, "loc_286F"),
        (3, "loc_288C"),
        (4, "loc_2D0D"),
        (SWITCH_DEFAULT, "loc_2D1A"),
    )


    label("loc_2650")


    AnonymousTalk(    #51
        (
            "\x07\x05#1S『克雷德尔』是\x01",
            "位于利贝尔·方舟市南区的\x01",
            "普通市民居住区。\x01\x01",
            "现在其中虽然有１２８个区域，\x01",
            "但由于最近几十年出生率的低下，\x01",
            "有三分之一的区域已经被关闭。\x01",
            "此外，『克雷德尔』的各个区域\x01",
            "都设有车站、市政厅、社交场所等公共设施，\x01",
            "为市民提供丰富的服务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D27")

    label("loc_274B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2809")

    AnonymousTalk(    #52
        (
            "\x07\x05#1S现在『光环轨道』的运行受到了\x01",
            "大幅度的限制。\x01\x01",
            "要启动『第３５克雷德尔站』的\x01",
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
        (0, "loc_27E7"),
        (1, "loc_2800"),
        (SWITCH_DEFAULT, "loc_2806"),
    )


    label("loc_27E7")

    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Call(0, 2)
    Return()

    label("loc_2800")

    OP_5F(0x1)
    Jump("loc_2806")

    label("loc_2806")

    Jump("loc_286C")

    label("loc_2809")


    AnonymousTalk(    #53
        (
            "\x07\x05#1S现在『光环轨道』的运行受到了\x01",
            "大幅度的限制。\x01\x01",
            "『第３５克雷德尔站』的紧急运行\x01",
            "模式已经启动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_286C")

    Jump("loc_2D27")

    label("loc_286F")

    FadeToBright(300, 0)

    AnonymousTalk(    #54
        "\x07\x05\x02",
    )

    OP_A9(0xF1)
    FadeToDark(300, 0, 100)
    Jump("loc_2D27")

    label("loc_288C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD2")

    AnonymousTalk(    #55
        (
            "\x07\x05#1S当『光环轨道』\x01",
            "由于各种原因而无法使用时，\x01",
            "可以解除车站周边大门的锁定\x01",
            "并进入地下通道之中。\x01\x01",
            "【警告】\x01",
            "根据来自『中枢塔』的指示，\x01",
            "解除锁定必须先进行身份认证。\x01\x01",
            "请在此终端前使用\x01",
            "您携带的『福音』。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_56(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAB")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇第一次看到（未持有福音）的情况下】\x01",              # 0
            "【◇第一次看到（持有福音）的情况下】\x01",                # 1
            "【◇第二次（以上）看到（未持有福音）的情况下】\x01",      # 2
            "【◇第二次（以上）看到（持有福音）的情况下】\x01",        # 3
            "【◇什么也没有变更】\x01",                                # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A7F"),
        (1, "loc_2A8A"),
        (2, "loc_2A95"),
        (3, "loc_2AA0"),
        (SWITCH_DEFAULT, "loc_2AAB"),
    )


    label("loc_2A7F")

    OP_A3(0x221A)
    OP_3F(0x40F, 1)
    Jump("loc_2AAB")

    label("loc_2A8A")

    OP_A3(0x221A)
    OP_3E(0x40F, 1)
    Jump("loc_2AAB")

    label("loc_2A95")

    OP_A2(0x221A)
    OP_3F(0x40F, 1)
    Jump("loc_2AAB")

    label("loc_2AA0")

    OP_A2(0x221A)
    OP_3E(0x40F, 1)
    Jump("loc_2AAB")

    label("loc_2AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x40F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B40")

    ChrTalk(    #56
        0x101,
        "#1004F#6P这是什么意思……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        (
            "#1035F#6P看来这次和以前\x01",
            "不一样了。\x02\x03",

            "#1043F『福音』啊……\x01",
            "有没有办法拿到呢？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #58
        "\x07\x05\x02",
    )

    Jump("loc_2CBC")

    label("loc_2B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x40F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BE5")

    ChrTalk(    #59
        0x101,
        "#1004F#6P这是什么意思……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        (
            "#1035F#6P看来这次和以前\x01",
            "不一样了。\x02\x03",

            "#1043F如果把刚才拿到的『福音』\x01",
            "在这个终端前使用的话……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #61
        "\x07\x05\x02",
    )

    Jump("loc_2CBC")

    label("loc_2BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 2)), scpexpr(EXPR_EXEC_OP, "OP_40(0x40F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C55")

    ChrTalk(    #62
        0x102,
        (
            "#1035F#6P看来要解除锁定\x01",
            "就需要『福音』。\x02\x03",

            "#1043F有没有办法拿到呢……？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #63
        "\x07\x05\x02",
    )

    Jump("loc_2CBC")

    label("loc_2C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 2)), scpexpr(EXPR_EXEC_OP, "OP_40(0x40F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CBC")

    ChrTalk(    #64
        0x102,
        (
            "#1040F#6P如果把刚才拿到的『福音』\x01",
            "在这个终端前使用好像就行了……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #65
        "\x07\x05\x02",
    )


    label("loc_2CBC")

    OP_A2(0x221A)
    OP_28(0x9D, 0x1, 0x400)
    FadeToDark(300, 0, 100)
    Jump("loc_2D0A")

    label("loc_2CD2")


    AnonymousTalk(    #66
        (
            "\x07\x05#1S现在，第３５克雷德尔站附近的\x01",
            "大门锁定已经解除。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D0A")

    Jump("loc_2D27")

    label("loc_2D0D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D27")

    label("loc_2D1A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D27")

    label("loc_2D27")

    Jump("loc_25C8")

    label("loc_2D2A")

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

    # Function_15_2452 end

    def Function_16_2DD8(): pass

    label("Function_16_2DD8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x40F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DE5")
    Return()

    label("loc_2DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15E0), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F82")
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
    PlayEffect(0x1, 0xFF, 0x9, 0, 150, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5801   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_2FD2")

    label("loc_2F82")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_48()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #67
        "\x07\x05什么也没发生……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    ClearMapFlags(0x80)
    Return()

    label("loc_2FD2")

    Return()

    # Function_16_2DD8 end

    def Function_17_2FD3(): pass

    label("Function_17_2FD3")

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
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #68
        (
            "\x07\x05本站附近的大门锁定\x01",
            "已经解除。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #69
        "\x07\x05地下通道１２５号已经可以使用了。\x02",
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
    OP_A2(0x221C)
    OP_28(0x9D, 0x1, 0x1000)
    EventEnd(0x0)
    Return()

    # Function_17_2FD3 end

    def Function_18_315F(): pass

    label("Function_18_315F")

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

    def lambda_320B():
        OP_6D(-13000, -25000, 490, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_320B)

    def lambda_3223():
        OP_67(0, 3890, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3223)

    def lambda_323B():
        OP_6B(5200, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_323B)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x1C3)
    Sleep(500)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5801   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_18_315F end

    def Function_19_326A(): pass

    label("Function_19_326A")

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

    def lambda_3310():
        OP_6D(-13000, 0, 2000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3310)

    def lambda_3328():
        OP_67(0, 3880, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3328)
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
    EventEnd(0x0)
    Return()

    # Function_19_326A end

    def Function_20_3425(): pass

    label("Function_20_3425")

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
        (0, "loc_349F"),
        (1, "loc_34A5"),
        (SWITCH_DEFAULT, "loc_34AB"),
    )


    label("loc_349F")

    OP_A2(0x1200)
    Jump("loc_34AB")

    label("loc_34A5")

    OP_A2(0x1201)
    Jump("loc_34AB")

    label("loc_34AB")

    Return()

    # Function_20_3425 end

    def Function_21_34AC(): pass

    label("Function_21_34AC")

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

    # Function_21_34AC end

    def Function_22_353F(): pass

    label("Function_22_353F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #70
        (
            "\x07\x05≡ 前面的月台\x01",
            "　　　第３５克雷德尔站\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_353F end

    SaveToFile()

Try(main)
