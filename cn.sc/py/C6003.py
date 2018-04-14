from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C6003   ._SN',
        MapName             = 'Other',
        Location            = 'C6003.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '目标',                                 # 9
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
        Unknown_1C          = 16,
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
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_152",          # 00, 0
        "Function_1_172",          # 01, 1
        "Function_2_1CD",          # 02, 2
        "Function_3_1160",         # 03, 3
        "Function_4_1197",         # 04, 4
        "Function_5_11CE",         # 05, 5
        "Function_6_1205",         # 06, 6
        "Function_7_123C",         # 07, 7
        "Function_8_1930",         # 08, 8
        "Function_9_1A28",         # 09, 9
        "Function_10_1A7C",        # 0A, 10
        "Function_11_22BF",        # 0B, 11
        "Function_12_2316",        # 0C, 12
        "Function_13_2368",        # 0D, 13
        "Function_14_23BA",        # 0E, 14
        "Function_15_240C",        # 0F, 15
        "Function_16_2F0A",        # 10, 16
        "Function_17_3015",        # 11, 17
        "Function_18_31D0",        # 12, 18
        "Function_19_3253",        # 13, 19
        "Function_20_32E6",        # 14, 20
    )


    def Function_0_152(): pass

    label("Function_0_152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_163")
    OP_A3(0x10F0)
    Event(0, 10)
    Jump("loc_171")

    label("loc_163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_171")
    OP_A3(0x10F1)
    Event(0, 17)

    label("loc_171")

    Return()

    # Function_0_152 end

    def Function_1_172(): pass

    label("Function_1_172")

    OP_22(0x1C3, 0x1, 0x64)
    StopSound(0x124F8, 0x493E0, 0x0)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 500)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_END)), "loc_1BB")
    OP_6F(0x1, 950)
    OP_6F(0x3, 240)

    label("loc_1BB")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    Return()

    # Function_1_172 end

    def Function_2_1CD(): pass

    label("Function_2_1CD")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A50")
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

    def lambda_244():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_244)
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

    def lambda_33C():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_33C)

    def lambda_354():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_354)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_37F():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_37F)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_472")

    ChrTalk(    #3
        0x105,
        (
            "#1165F#6P看来这就是\x01",
            "『光环轨道』了。\x02\x03",

            "是通过什么样的原理呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_697")

    label("loc_472")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CE")

    ChrTalk(    #4
        0x103,
        (
            "#026F#6P呼呼……\x01",
            "看来这就是『光环轨道』了。\x02\x03",

            "是通过什么样的原理呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_697")

    label("loc_4CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52F")

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
    Jump("loc_697")

    label("loc_52F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58D")

    ChrTalk(    #6
        0x108,
        (
            "#074F#6P呼呼。\x01",
            "看来这就是『光环轨道』了。\x02\x03",

            "什么样的原理倒是无从得知……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_697")

    label("loc_58D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F7")

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
    Jump("loc_697")

    label("loc_5F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_653")

    ChrTalk(    #8
        0x104,
        (
            "#035F#6P呼，看来这就是\x01",
            "『光环轨道』了。\x02\x03",

            "什么样的原理倒是无从得知……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_697")

    label("loc_653")


    ChrTalk(    #9
        0x102,
        (
            "#1040F#2P看来\x01",
            "这就是『光环轨道』了。\x02\x03",

            "是通过什么样的原理呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_697")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_707")

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
    Jump("loc_96C")

    label("loc_707")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76F")

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
    Jump("loc_96C")

    label("loc_76F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DD")

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
    Jump("loc_96C")

    label("loc_7DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_845")

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
    Jump("loc_96C")

    label("loc_845")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AB")

    ChrTalk(    #14
        0x106,
        (
            "#555F#6P像矿车一样\x01",
            "在轨道上跑的交通工具啊。\x02\x03",

            "#551F透明的轨道真是\x01",
            "感觉怪怪的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96C")

    label("loc_8AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90F")

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
    Jump("loc_96C")

    label("loc_90F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_96C")

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

    label("loc_96C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D7")

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

    label("loc_9D7")


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
    Jump("loc_10BA")

    label("loc_A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAB")
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

    def lambda_AC0():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AC0)
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

    def lambda_B8E():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B8E)

    def lambda_BA6():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BA6)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_BD1():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BD1)
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
    Jump("loc_10BA")

    label("loc_CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA4")
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

    def lambda_D20():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D20)
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

    def lambda_D8D():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D8D)

    def lambda_DA5():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DA5)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_DD0():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DD0)
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
    Jump("loc_10BA")

    label("loc_EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BA")
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

    def lambda_F19():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F19)
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

    def lambda_F86():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F86)

    def lambda_F9E():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F9E)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_FC9():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FC9)
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

    label("loc_10BA")

    OP_A2(0x2209)
    OP_28(0x9F, 0x1, 0x1)
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

    # Function_2_1CD end

    def Function_3_1160(): pass

    label("Function_3_1160")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xA3C, 0x1388, 0x47B8, 0x1388, 0x0)

    def lambda_118B():

        label("loc_118B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_118B")

    QueueWorkItem2(0xFE, 2, lambda_118B)
    Return()

    # Function_3_1160 end

    def Function_4_1197(): pass

    label("Function_4_1197")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xE2E, 0x1388, 0x47CC, 0x1388, 0x0)

    def lambda_11C2():

        label("loc_11C2")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_11C2")

    QueueWorkItem2(0xFE, 2, lambda_11C2)
    Return()

    # Function_4_1197 end

    def Function_5_11CE(): pass

    label("Function_5_11CE")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0x8C0, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_11F9():

        label("loc_11F9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_11F9")

    QueueWorkItem2(0xFE, 2, lambda_11F9)
    Return()

    # Function_5_11CE end

    def Function_6_1205(): pass

    label("Function_6_1205")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xFE6, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_1230():

        label("loc_1230")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1230")

    QueueWorkItem2(0xFE, 2, lambda_1230)
    Return()

    # Function_6_1205 end

    def Function_7_123C(): pass

    label("Function_7_123C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1245")
    Return()

    label("loc_1245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1652")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C5")
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A0")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_13D4")

    label("loc_13A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C2")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_13D4")

    label("loc_13C2")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_13D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F6")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_142A")

    label("loc_13F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1418")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_142A")

    label("loc_1418")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_142A")

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
    Jump("loc_164F")

    label("loc_15C5")

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

    label("loc_164F")

    Jump("loc_192F")

    label("loc_1652")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_END)), "loc_172F")
    OP_CC(0x1, 0x0, "【西卡尔玛丽站】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_172F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_END)), "loc_1758")
    OP_CC(0x1, 0x0, "【第３５克雷德尔站】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_END)), "loc_1781")
    OP_CC(0x1, 0x0, "【第７法克特里亚站】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1781")

    OP_CC(0x1, 0x0, "【放弃使用】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_17C4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1846")

    label("loc_17C4")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1846")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E8")
    Jump("loc_1846")

    label("loc_17E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1839")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1822")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_181F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_181F")

    Jump("loc_1839")

    label("loc_1822")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_17E8")

    label("loc_1839")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_17CE")

    label("loc_1846")

    SetMapFlags(0x100000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1864"),
        (1, "loc_18A2"),
        (2, "loc_18E0"),
        (3, "loc_191E"),
        (SWITCH_DEFAULT, "loc_1921"),
    )


    label("loc_1864")

    OP_A2(0x2213)
    OP_A2(0x2214)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_1877():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1877)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1921")

    label("loc_18A2")

    OP_A2(0x2213)
    OP_A2(0x2215)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_18B5():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18B5)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1921")

    label("loc_18E0")

    OP_A2(0x2213)
    OP_A2(0x2216)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_18F3():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18F3)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1921")

    label("loc_191E")

    Jump("loc_1921")

    label("loc_1921")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    EventEnd(0x0)

    label("loc_192F")

    Return()

    # Function_7_123C end

    def Function_8_1930(): pass

    label("Function_8_1930")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 6)), scpexpr(EXPR_END)), "loc_19DC")
    OP_6F(0x1, 1100)
    OP_70(0x1, 0x514)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_19A7():
        OP_6D(8300, 5000, 21350, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19A7)

    def lambda_19BF():
        OP_6C(12000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19BF)

    def lambda_19CF():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_19CF)
    Jump("loc_1A17")

    label("loc_19DC")

    OP_6F(0x1, 300)
    OP_70(0x1, 0x1F4)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_19F5():
        OP_6D(-2860, 5000, 21710, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19F5)

    def lambda_1A0D():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A0D)

    label("loc_1A17")

    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_8_1930 end

    def Function_9_1A28(): pass

    label("Function_9_1A28")

    OP_8E(0xFE, 0xC08, 0x1388, 0x4A56, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC2, 0x13F6, 0x4F6A, 0x7D0, 0x0)

    def lambda_1A56():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1A56)
    OP_8E(0xFE, 0xC1C, 0x13F6, 0x5E9C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_1A28 end

    def Function_10_1A7C(): pass

    label("Function_10_1A7C")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 0)), scpexpr(EXPR_END)), "loc_1B85")
    OP_6D(-9950, 5000, 20680, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_1B70():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B70)
    Jump("loc_1BFD")

    label("loc_1B85")

    OP_6D(12690, 5000, 20450, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 1300)
    OP_70(0x1, 0x640)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_1BDB():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BDB)

    def lambda_1BF3():
        OP_6C(0, 5500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BF3)

    label("loc_1BFD")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B5")
    OP_43(0x101, 0x1, 0x0, 0xB)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0xC)
    Sleep(800)

    def lambda_1C59():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C59)

    def lambda_1C71():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C71)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DCA")

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
    Jump("loc_1EEF")

    label("loc_1DCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E04")

    ChrTalk(    #37
        0x107,
        (
            "#067F#5P嘿嘿……\x01",
            "的确可以这么说呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEF")

    label("loc_1E04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E39")

    ChrTalk(    #38
        0x105,
        (
            "#1168F#5P呵呵……\x01",
            "确实是这样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEF")

    label("loc_1E39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E68")

    ChrTalk(    #39
        0x103,
        "#021F#5P呵呵……有道理。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EEF")

    label("loc_1E68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E94")

    ChrTalk(    #40
        0x109,
        "#1061F#5P哈哈，没错～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EEF")

    label("loc_1E94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EC5")

    ChrTalk(    #41
        0x104,
        "#031F#5P呵呵……我有同感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EEF")

    label("loc_1EC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EEF")

    ChrTalk(    #42
        0x108,
        "#071F#5P哈哈……没错。\x02",
    )

    CloseMessageWindow()

    label("loc_1EEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F56")

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
    Jump("loc_21AF")

    label("loc_1F56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB7")

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
    Jump("loc_21AF")

    label("loc_1FB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_201F")

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
    Jump("loc_21AF")

    label("loc_201F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207F")

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
    Jump("loc_21AF")

    label("loc_207F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20DE")

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
    Jump("loc_21AF")

    label("loc_20DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2148")

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
    Jump("loc_21AF")

    label("loc_2148")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21AF")

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

    label("loc_21AF")

    OP_A2(0x220F)
    Jump("loc_220D")

    label("loc_21B5")

    OP_43(0x101, 0x1, 0x0, 0xB)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0xC)
    Sleep(800)

    def lambda_21D3():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_21D3)

    def lambda_21EB():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_21EB)
    OP_43(0xF8, 0x1, 0x0, 0xD)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0xE)
    Sleep(500)

    label("loc_220D")

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

    # Function_10_1A7C end

    def Function_11_22BF(): pass

    label("Function_11_22BF")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_22D5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22D5)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xECE, 0x1388, 0x4376, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    ClearChrFlags(0xFE, 0x80)
    Return()

    # Function_11_22BF end

    def Function_12_2316(): pass

    label("Function_12_2316")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_232C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_232C)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9F6, 0x1388, 0x4362, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_2316 end

    def Function_13_2368(): pass

    label("Function_13_2368")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_237E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_237E)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1086, 0x1388, 0x4808, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_13_2368 end

    def Function_14_23BA(): pass

    label("Function_14_23BA")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_23D0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23D0)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7B2, 0x1388, 0x47A4, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_14_23BA end

    def Function_15_240C(): pass

    label("Function_15_240C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2431")
    Call(0, 18)
    Call(0, 19)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_2431")

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
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #50
        (
            "\x07\x05#1S『光环轨道』中枢塔前站\x01\x01\x01",
            "※现在『光环轨道』的运行受到了\x01",
            "  大幅度的限制，麻烦请您在本终端\x01",
            "  手动输入我们可以为您提供的服务。\x01\x01\x01",
            "『利贝尔·方舟』市·交通管理中心\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_257C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E5C")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        20,
        100,
        0,
        (
            "【中枢塔向导】\x01",        # 0
            "【使用光环轨道】\x01",      # 1
            "【网络商城】\x01",          # 2
            "【解除门锁】\x01",          # 3
            "【停止服务】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2602"),
        (1, "loc_2C9C"),
        (2, "loc_2DB4"),
        (3, "loc_2DD1"),
        (4, "loc_2E3F"),
        (SWITCH_DEFAULT, "loc_2E4C"),
    )


    label("loc_2602")


    AnonymousTalk(    #51
        (
            "\x07\x02#1S诸位游击士，欢迎你们。\x01\x01",
            "我猜想诸位能够来到这里，\x01",
            "于是就在此留言了。\x01\x01",
            "『福音计划』已经进入最后一部分，\x01",
            "『辉之环』也接近真正的觉醒了。\x01\x01",
            "我希望你们也能\x01",
            "亲临现场做个见证，\x01",
            "不过光是为你们带路的话也颇为无趣。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #52
        (
            "\x07\x02#1S因此我们来玩个游戏吧。\x01\x01",
            "在中枢塔的各处，\x01",
            "都有我的协助者们在把守着。\x01\x01",
            "如果能突破他们的防线，来到塔顶的话\x01",
            "我就向诸位展示『环』的复活过程。\x01\x01",
            "接下来就让我期待你们的表现吧。\x01\x01\x01",
            "『蛇之使徒』第三柱——盖鲁格·怀斯曼\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #53
        (
            "\x07\x02#1SP.S.致约修亚。\x01",
            "我很高兴你能和\x01",
            "重要的家人以及同伴再会。\x01\x01",
            "不过，你可别小看了\x01",
            "莱维和玲哦。\x01\x01",
            "我特地给你们准备了机会，\x01",
            "你们就尽情地聊聊吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C99")
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #54
        0x102,
        "#1042F#5P………………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28B8")

    ChrTalk(    #55
        0x107,
        "#065F#6P这、这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_29AD")

    label("loc_28B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28E0")

    ChrTalk(    #56
        0x105,
        "#1163F#6P这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_29AD")

    label("loc_28E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2908")

    ChrTalk(    #57
        0x109,
        "#1063F#6P这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_29AD")

    label("loc_2908")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2933")

    ChrTalk(    #58
        0x103,
        "#022F#6P……这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_29AD")

    label("loc_2933")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_295E")

    ChrTalk(    #59
        0x104,
        "#032F#6P哟，这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_29AD")

    label("loc_295E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2985")

    ChrTalk(    #60
        0x106,
        "#057F#6P这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_29AD")

    label("loc_2985")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29AD")

    ChrTalk(    #61
        0x108,
        "#072F#6P……这是……\x02",
    )

    CloseMessageWindow()

    label("loc_29AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A04")

    ChrTalk(    #62
        0x10B,
        (
            "#212F#6P我不大了解\x01",
            "这个教授……\x02\x03",

            "不过感觉他真是个\x01",
            "趣味低级的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B6C")

    label("loc_2A04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A35")

    ChrTalk(    #63
        0x108,
        "#072F#6P趣味低级的男人……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B6C")

    label("loc_2A35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A6A")

    ChrTalk(    #64
        0x106,
        "#057F#6P哼……趣味低级的白痴。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B6C")

    label("loc_2A6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AC9")

    ChrTalk(    #65
        0x104,
        (
            "#035F#6P呼，不得了不得了。\x02\x03",

            "#030F看来是个令人心服口服的\x01",
            "趣味低级人物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B6C")

    label("loc_2AC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AFC")

    ChrTalk(    #66
        0x103,
        "#022F#6P……趣味低级的男人。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B6C")

    label("loc_2AFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B41")

    ChrTalk(    #67
        0x109,
        (
            "#1063F#6P怎么说呢……\x01",
            "还真是个趣味低级的男人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B6C")

    label("loc_2B41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B6C")

    ChrTalk(    #68
        0x105,
        "#1162F#6P……趣味低级。\x02",
    )

    CloseMessageWindow()

    label("loc_2B6C")


    ChrTalk(    #69
        0x101,
        (
            "#1007F#6P嗯……是一个性格\x01",
            "完全扭曲的人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #70
        0x101,
        (
            "#1025F#2P我说，约修亚。\x01",
            "你不必介意那种人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #71
        0x102,
        (
            "#1035F#5P……没关系，我不介意。\x02\x03",

            "#1040F不过，莱维他们\x01",
            "看来似乎真的在那里面呢。\x02\x03",

            "我们必须打起精神来才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1006F#2P……嗯！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2231)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)
    SetMessageWindowPos(330, 78, 34, 12)

    AnonymousTalk(    #73
        "\x07\x05\x02",
    )


    label("loc_2C99")

    Jump("loc_2E59")

    label("loc_2C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D54")

    AnonymousTalk(    #74
        (
            "\x07\x05#1S现在『光环轨道』的运行受到了\x01",
            "大幅度的限制。\x01\x01",
            "要启动『中枢塔前站』的\x01",
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
        (0, "loc_2D32"),
        (1, "loc_2D4B"),
        (SWITCH_DEFAULT, "loc_2D51"),
    )


    label("loc_2D32")

    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Call(0, 2)
    Return()

    label("loc_2D4B")

    OP_5F(0x1)
    Jump("loc_2D51")

    label("loc_2D51")

    Jump("loc_2DB1")

    label("loc_2D54")


    AnonymousTalk(    #75
        (
            "\x07\x05#1S现在『光环轨道』的运行受到了\x01",
            "大幅度的限制。\x01\x01",
            "『中枢塔前站』的紧急运行\x01",
            "模式已经启动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DB1")

    Jump("loc_2E59")

    label("loc_2DB4")

    FadeToBright(300, 0)

    AnonymousTalk(    #76
        "\x07\x05\x02",
    )

    OP_A9(0xF3)
    FadeToDark(300, 0, 100)
    Jump("loc_2E59")

    label("loc_2DD1")


    AnonymousTalk(    #77
        (
            "\x07\x05#1S地下通道２４６号\x01",
            "已经可以使用了。\x01\x01",
            "对面的地下大门\x01",
            "是通向公园区域的避难通道。\x01\x01",
            "只能在紧急时刻使用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E59")

    label("loc_2E3F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E59")

    label("loc_2E4C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E59")

    label("loc_2E59")

    Jump("loc_257C")

    label("loc_2E5C")

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

    # Function_15_240C end

    def Function_16_2F0A(): pass

    label("Function_16_2F0A")

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

    def lambda_2FB6():
        OP_6D(-13000, -25000, 490, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FB6)

    def lambda_2FCE():
        OP_67(0, 3890, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2FCE)

    def lambda_2FE6():
        OP_6B(5200, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2FE6)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x1C3)
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2F0A end

    def Function_17_3015(): pass

    label("Function_17_3015")

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

    def lambda_30BB():
        OP_6D(-13000, 0, 2000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_30BB)

    def lambda_30D3():
        OP_67(0, 3880, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30D3)
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

    # Function_17_3015 end

    def Function_18_31D0(): pass

    label("Function_18_31D0")

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
            "【◇雪拉扎德在队伍内】\x01",      # 0
            "【◇阿加特在队伍内】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3246"),
        (1, "loc_324C"),
        (SWITCH_DEFAULT, "loc_3252"),
    )


    label("loc_3246")

    OP_A2(0x1200)
    Jump("loc_3252")

    label("loc_324C")

    OP_A2(0x1201)
    Jump("loc_3252")

    label("loc_3252")

    Return()

    # Function_18_31D0 end

    def Function_19_3253(): pass

    label("Function_19_3253")

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

    # Function_19_3253 end

    def Function_20_32E6(): pass

    label("Function_20_32E6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #78
        (
            "\x07\x05≡ 前面的月台\x01",
            "　　　中枢塔前站\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_32E6 end

    SaveToFile()

Try(main)
