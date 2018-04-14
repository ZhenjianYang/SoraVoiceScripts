from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C6000   ._SN',
        MapName             = 'Other',
        Location            = 'C6000.x',
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
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -12900,
        Y                   = 0,
        Z                   = 2140,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 26,
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
        TalkFunctionIndex   = 11,
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
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_152",          # 00, 0
        "Function_1_197",          # 01, 1
        "Function_2_1F7",          # 02, 2
        "Function_3_DDA",          # 03, 3
        "Function_4_E6C",          # 04, 4
        "Function_5_E88",          # 05, 5
        "Function_6_EB8",          # 06, 6
        "Function_7_ED4",          # 07, 7
        "Function_8_F04",          # 08, 8
        "Function_9_F34",          # 09, 9
        "Function_10_F64",         # 0A, 10
        "Function_11_F94",         # 0B, 11
        "Function_12_1BA0",        # 0C, 12
        "Function_13_2B55",        # 0D, 13
        "Function_14_2B8C",        # 0E, 14
        "Function_15_2BC3",        # 0F, 15
        "Function_16_2BFA",        # 10, 16
        "Function_17_2C31",        # 11, 17
        "Function_18_2DBB",        # 12, 18
        "Function_19_34B9",        # 13, 19
        "Function_20_35B1",        # 14, 20
        "Function_21_3605",        # 15, 21
        "Function_22_3E48",        # 16, 22
        "Function_23_3E9F",        # 17, 23
        "Function_24_3EF1",        # 18, 24
        "Function_25_3F43",        # 19, 25
        "Function_26_3F95",        # 1A, 26
        "Function_27_40A0",        # 1B, 27
        "Function_28_425B",        # 1C, 28
        "Function_29_42E2",        # 1D, 29
        "Function_30_4373",        # 1E, 30
    )


    def Function_0_152(): pass

    label("Function_0_152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_168")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_196")

    label("loc_168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_179")
    OP_A3(0x10F1)
    Event(0, 21)
    Jump("loc_196")

    label("loc_179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_196")
    OP_A3(0x10F2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192")
    Event(0, 2)
    Jump("loc_196")

    label("loc_192")

    Event(0, 27)

    label("loc_196")

    Return()

    # Function_0_152 end

    def Function_1_197(): pass

    label("Function_1_197")

    OP_22(0x1C3, 0x1, 0x64)
    StopSound(0x124F8, 0x493E0, 0x0)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 500)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_END)), "loc_1E5")
    OP_72(0x1, 0x4)
    OP_6F(0x1, 950)
    OP_6F(0x3, 240)

    label("loc_1E5")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    Return()

    # Function_1_197 end

    def Function_2_1F7(): pass

    label("Function_2_1F7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20E")
    Call(0, 28)
    Call(0, 29)

    label("loc_20E")

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
    OP_70(0x0, 0x0)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_2A9():
        OP_6D(-13000, 0, 2000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A9)

    def lambda_2C1():
        OP_67(0, 3880, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C1)
    FadeToBright(1000, 0)
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
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(100)
    OP_43(0x102, 0x1, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x7)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x9)
    WaitChrThread(0xF9, 0x1)

    def lambda_373():
        OP_6D(-3930, 0, 11550, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_373)

    def lambda_38B():
        OP_67(0, 7500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38B)

    def lambda_3A3():
        OP_6B(3650, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3A3)

    def lambda_3B3():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3B3)
    Sleep(3000)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x6)
    Sleep(300)
    OP_43(0xF8, 0x1, 0x0, 0x8)
    Sleep(300)
    OP_43(0xF9, 0x1, 0x0, 0xA)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_425")

    ChrTalk(    #0
        0x107,
        "#064F哇……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E0")

    label("loc_425")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44E")

    ChrTalk(    #1
        0x105,
        "#1164F好厉害……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E0")

    label("loc_44E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_474")

    ChrTalk(    #2
        0x103,
        "#023F这真是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E0")

    label("loc_474")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49B")

    ChrTalk(    #3
        0x109,
        "#1064F这真是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E0")

    label("loc_49B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BD")

    ChrTalk(    #4
        0x104,
        "#033F这……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E0")

    label("loc_4BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E0")

    ChrTalk(    #5
        0x106,
        "#052F这家伙……\x02",
    )

    CloseMessageWindow()

    label("loc_4E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50C")

    ChrTalk(    #6
        0x108,
        "#072F这还真是精彩……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EE")

    label("loc_50C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_538")

    ChrTalk(    #7
        0x106,
        "#555F果然令人吃惊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EE")

    label("loc_538")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56D")

    ChrTalk(    #8
        0x104,
        (
            "#035F呼……\x01",
            "真是压倒性的景象。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EE")

    label("loc_56D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A0")

    ChrTalk(    #9
        0x109,
        "#1060F一句话，真是太棒了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EE")

    label("loc_5A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CA")

    ChrTalk(    #10
        0x103,
        "#020F……了不起啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EE")

    label("loc_5CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EE")

    ChrTalk(    #11
        0x105,
        "#1382F了不起……\x02",
    )

    CloseMessageWindow()

    label("loc_5EE")


    ChrTalk(    #12
        0x101,
        (
            "#1004F#6P想、想不到\x01",
            "是这么大的都市……\x02\x03",

            "#1015F果然真的……\x01",
            "没人住在这里吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#1035F#6P嗯……大概。\x02\x03",

            "#1040F看来在被封入异次元时\x01",
            "大多数的居民好像都离开了。\x02\x03",

            "利贝尔国民的始祖\x01",
            "大概就是那些人吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    def lambda_6DF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6DF)

    ChrTalk(    #14
        0x101,
        (
            "#1020F#2P那、那就是说……\x02\x03",

            "我们的祖先曾经\x01",
            "住在这座都市里！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A9")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #15
        0x105,
        (
            "#1167F……我觉得很有可能。\x02\x03",

            "#1162F不光是在利贝尔，\x01",
            "大崩坏之前文明的痕迹据说\x01",
            "在各地都惊人地稀少……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A01")

    label("loc_7A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81F")
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #16
        0x108,
        (
            "#074F很有可能吧。\x02\x03",

            "#072F在卡尔瓦德也一样，\x01",
            "大崩坏之前文明的痕迹据说\x01",
            "在各地都惊人地稀少。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A01")

    label("loc_81F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89B")
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #17
        0x104,
        (
            "#035F我觉得很有可能。\x02\x03",

            "#030F在埃雷波尼亚也一样，\x01",
            "大崩坏之前文明的痕迹据说\x01",
            "在各地都惊人地稀少。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A01")

    label("loc_89B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91B")
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #18
        0x109,
        (
            "#1065F……可能性应该很高。\x02\x03",

            "#1063F大陆全境都是一样，\x01",
            "大崩坏之前文明的痕迹据说\x01",
            "在各地都惊人地稀少。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A01")

    label("loc_91B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_997")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #19
        0x103,
        (
            "#026F应该很有可能呢……\x02\x03",

            "#022F不光是在利贝尔，\x01",
            "大崩坏之前文明的痕迹据说\x01",
            "在各地都惊人地稀少哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A01")

    label("loc_997")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A01")
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #20
        0x107,
        (
            "#063F说、说起来以前\x01",
            "爷爷说过……\x02\x03",

            "大崩坏之前文明的痕迹据说\x01",
            "在各地都惊人地稀少。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A5F")

    ChrTalk(    #21
        0x106,
        (
            "#053F原来如此啊……\x02\x03",

            "#050F在地面上没留下痕迹\x01",
            "原来是因为以前住在天上啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C35")

    label("loc_A5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ABC")

    ChrTalk(    #22
        0x107,
        (
            "#065F这、这样啊……\x02\x03",

            "在地面上没留下痕迹\x01",
            "原来是因为以前都住在天上啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C35")

    label("loc_ABC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B18")

    ChrTalk(    #23
        0x103,
        (
            "#026F原来如此……\x02\x03",

            "#022F在地面上没留下痕迹\x01",
            "原来是因为以前住在天上啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C35")

    label("loc_B18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7A")

    ChrTalk(    #24
        0x109,
        (
            "#1068F哈，原来如此……\x02\x03",

            "#1060F在地面上没留下痕迹\x01",
            "原来是因为以前住在天上啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C35")

    label("loc_B7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDA")

    ChrTalk(    #25
        0x104,
        (
            "#035F呵，原来如此……\x02\x03",

            "#030F在地面上没留下痕迹\x01",
            "原来是因为以前住在天上啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C35")

    label("loc_BDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C35")

    ChrTalk(    #26
        0x108,
        (
            "#074F呼，原来如此。\x02\x03",

            "#070F在地面上没留下痕迹\x01",
            "原来是因为以前住在天上啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C35")


    ChrTalk(    #27
        0x101,
        (
            "#1007F#2P好、好像越说越\x01",
            "觉得离奇了……\x02\x03",

            "#1017F话说回来……\x01",
            "景色看上去这么棒，\x01",
            "这里到底是什么地方？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        "#1043F#6P可能只是普通的了望台……\x02",
    )

    CloseMessageWindow()

    def lambda_CCA():
        OP_6D(-2200, 0, 8670, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CCA)

    def lambda_CE2():
        OP_67(0, 6140, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CE2)
    OP_8C(0x102, 135, 400)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #29
        0x102,
        (
            "#1040F#5P前面有像终端一样的东西，\x01",
            "我们去调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-3950, 0, 6730, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, -3950, 0, 6730, 225)
    SetChrPos(0x1, -3950, 0, 6730, 225)
    SetChrPos(0x2, -3950, 0, 6730, 225)
    SetChrPos(0x3, -3950, 0, 6730, 225)
    Sleep(500)
    OP_A2(0x2203)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_2_1F7 end

    def Function_3_DDA(): pass

    label("Function_3_DDA")


    def lambda_DE0():
        OP_6D(-7380, 0, 2100, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DE0)
    OP_8E(0xFE, 0xFFFFE958, 0x0, 0x884, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(18150, 5000, 23940, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4990, 0)
    OP_6C(0, 0)
    OP_6E(267, 0)
    Return()

    # Function_3_DDA end

    def Function_4_E6C(): pass

    label("Function_4_E6C")

    OP_8E(0xFE, 0xFFFFF1AA, 0x0, 0x2486, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_E6C end

    def Function_5_E88(): pass

    label("Function_5_E88")

    OP_8E(0xFE, 0xFFFFD5F8, 0xA, 0x708, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE44E, 0x0, 0x802, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_5_E88 end

    def Function_6_EB8(): pass

    label("Function_6_EB8")

    OP_8E(0xFE, 0xFFFFED90, 0x0, 0x210C, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_EB8 end

    def Function_7_ED4(): pass

    label("Function_7_ED4")

    OP_8E(0xFE, 0xFFFFD5F8, 0xA, 0x708, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE0C0, 0xAA, 0x780, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_7_ED4 end

    def Function_8_F04(): pass

    label("Function_8_F04")

    OP_8E(0xFE, 0xFFFFE520, 0x0, 0x816, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF498, 0x0, 0x1EA0, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_8_F04 end

    def Function_9_F34(): pass

    label("Function_9_F34")

    OP_8E(0xFE, 0xFFFFD5F8, 0xA, 0x708, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFDBA2, 0xC8, 0x762, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_9_F34 end

    def Function_10_F64(): pass

    label("Function_10_F64")

    OP_8E(0xFE, 0xFFFFE520, 0x0, 0x816, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFEFFC, 0x0, 0x1AE0, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_F64 end

    def Function_11_F94(): pass

    label("Function_11_F94")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FB9")
    Call(0, 28)
    Call(0, 29)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_FB9")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1560")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #30
        (
            "\x07\x05#1S『光环轨道』西卡尔玛丽站\x01\x01\x01",
            "※现在『光环轨道』的运行受到了\x01",
            "  大幅度的限制。麻烦请您在本终端\x01",
            "  手动输入我们可以为您提供的服务。\x01\x01",
            "※因现在是紧急时期，无需用『福音』\x01",
            "  进行市民ID的认证。\x01\x01\x01",
            "『利贝尔·方舟』市·交通管理中心\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #31
        0x101,
        (
            "#1020F这、这是什么……\x02\x03",

            "出现了好几个令人\x01",
            "在意的词汇呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        (
            "#1035F#6P『光环轨道』……\x01",
            "好像是某种交通工具呢。\x02\x03",

            "#1040F而且，这座浮游都市的\x01",
            "名字看来叫做『利贝尔·方舟』。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #33
        0x101,
        "#1004F『利贝尔·方舟』……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1275")

    ChrTalk(    #34
        0x105,
        (
            "#1382F从发音来判断的话……\x01",
            "应该是『利贝尔』的语源吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E0")

    label("loc_1275")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C0")

    ChrTalk(    #35
        0x104,
        (
            "#035F嗯，从发音来判断的话\x01",
            "好像是『利贝尔』的语源吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E0")

    label("loc_12C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1309")

    ChrTalk(    #36
        0x103,
        (
            "#027F从发音来判断的话……\x01",
            "就是『利贝尔』的语源吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E0")

    label("loc_1309")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1350")

    ChrTalk(    #37
        0x108,
        (
            "#070F从发音来判断的话\x01",
            "好像是『利贝尔』的语源吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E0")

    label("loc_1350")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1398")

    ChrTalk(    #38
        0x109,
        (
            "#1060F从发音来判断的话\x01",
            "好像是『利贝尔』的语源吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E0")

    label("loc_1398")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E0")

    ChrTalk(    #39
        0x106,
        (
            "#051F从发音来判断的话……\x01",
            "好像是『利贝尔』的语源吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E0")


    ChrTalk(    #40
        0x101,
        "#1015F#5P原，原来如此……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(300)

    ChrTalk(    #41
        0x102,
        (
            "#1042F#6P还有『福音』……\x02\x03",

            "看来对这里的市民来说\x01",
            "是个很普通的东西呢。\x02\x03",

            "#1043F大概是享受公共服务时\x01",
            "所需要的个人身份证明兼认证终端……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1007F啊，我感到头脑混乱了……\x02\x03",

            "#1006F总之没有『福音』也可以\x01",
            "做一些事吧？\x02\x03",

            "快点进行各项调查吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        (
            "#1040F#6P明白──\x01",
            "呼叫出可以提供的服务一览吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_A2(0x2204)
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #44
        "\x07\x05\x02",
    )

    Jump("loc_1655")

    label("loc_1560")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 78, 34, 12)

    AnonymousTalk(    #45
        (
            "\x07\x05#1S『光环轨道』西卡尔玛丽站\x01\x01\x01",
            "※现在『光环轨道』的运行受到了\x01",
            "  大幅度的限制，麻烦请您在本终端\x01",
            "  手动输入我们可以为您提供的服务。\x01\x01",
            "※因现在是紧急时期，无需用『福音』\x01",
            "  进行市民ID的认证。\x01\x01\x01",
            "『利贝尔·方舟』市·交通管理中心\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1655")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_165F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AF2")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        20,
        100,
        0,
        (
            "【卡尔玛丽向导】\x01",      # 0
            "【使用光环轨道】\x01",      # 1
            "【网络商城】\x01",          # 2
            "【解除门锁】\x01",          # 3
            "【停止服务】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16E7"),
        (1, "loc_1863"),
        (2, "loc_197F"),
        (3, "loc_199C"),
        (4, "loc_1AD5"),
        (SWITCH_DEFAULT, "loc_1AE2"),
    )


    label("loc_16E7")


    AnonymousTalk(    #46
        (
            "\x07\x05#1S『卡尔玛丽』是\x01",
            "建造在利贝尔·方舟市西区的大型公园区域，\x01",
            "是供市民们休闲的场所。\x01\x01",
            "由数十个单边３００亚矩的\x01",
            "正六边形组成，\x01",
            "是一次主题为『自然与文明的和谐』的\x01",
            "大规模造园行动。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #47
        (
            "\x07\x05#1S四个入口分别为『光环轨道』的\x01",
            "『北卡尔玛丽站』、『东卡尔玛丽站』、\x01",
            "『西卡尔玛丽站』、『南卡尔玛丽站』。\x01\x01",
            "从各站开始的巡回路线，\x01",
            "各自通向风格迥异的地区，\x01",
            "可以享受到不同的四季景观和植被风貌。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AEF")

    label("loc_1863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191D")

    AnonymousTalk(    #48
        (
            "\x07\x05#1S现在『光环轨道』的运行受到了\x01",
            "大幅度的限制。\x01\x01",
            "要启动『西卡尔玛丽站』的\x01",
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
        (0, "loc_18FB"),
        (1, "loc_1914"),
        (SWITCH_DEFAULT, "loc_191A"),
    )


    label("loc_18FB")

    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Call(0, 12)
    Return()

    label("loc_1914")

    OP_5F(0x1)
    Jump("loc_191A")

    label("loc_191A")

    Jump("loc_197C")

    label("loc_191D")


    AnonymousTalk(    #49
        (
            "\x07\x05#1S现在『光环轨道』的运行受到了\x01",
            "大幅度的限制。\x01\x01",
            "『西卡尔玛丽站』的紧急运行\x01",
            "模式已经启动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197C")

    Jump("loc_1AEF")

    label("loc_197F")

    FadeToBright(300, 0)

    AnonymousTalk(    #50
        "\x07\x05\x02",
    )

    OP_A9(0xF0)
    FadeToDark(300, 0, 100)
    Jump("loc_1AEF")

    label("loc_199C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA2")

    AnonymousTalk(    #51
        (
            "\x07\x05#1S当『光环轨道』\x01",
            "由于各种原因而无法使用时，\x01",
            "可以解除车站周边大门的锁定\x01",
            "并进入地下通道之中。\x01\x01",
            "因现在处于紧急时期，\x01",
            "可以解除大门的锁定。\x01\x01",
            "要解除吗？\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        1,
        130,
        240,
        0,
        (
            "【解除】\x01",        # 0
            "【不解除】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A6E"),
        (1, "loc_1A99"),
        (SWITCH_DEFAULT, "loc_1A9F"),
    )


    label("loc_1A6E")

    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5901   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_1A9F")

    label("loc_1A99")

    OP_5F(0x1)
    Jump("loc_1A9F")

    label("loc_1A9F")

    Jump("loc_1AD2")

    label("loc_1AA2")


    AnonymousTalk(    #52
        (
            "\x07\x05#1S现在，西卡尔玛丽站的\x01",
            "大门锁定已经解除。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AD2")

    Jump("loc_1AEF")

    label("loc_1AD5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AEF")

    label("loc_1AE2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AEF")

    label("loc_1AEF")

    Jump("loc_165F")

    label("loc_1AF2")

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

    # Function_11_F94 end

    def Function_12_1BA0(): pass

    label("Function_12_1BA0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2443")
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

    def lambda_1C17():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C17)
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

    ChrTalk(    #53
        0x101,
        "#1004F#6P那、那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
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

    def lambda_1D0F():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D0F)

    def lambda_1D27():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D27)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_1D52():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1D52)
    Sleep(2000)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x10)
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

    ChrTalk(    #55
        0x101,
        "#1004F#6P那、那是什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E45")

    ChrTalk(    #56
        0x102,
        (
            "#1040F#6P看来这就是\x01",
            "『光环轨道』了。\x02\x03",

            "是通过什么样的原理呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208C")

    label("loc_1E45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EA0")

    ChrTalk(    #57
        0x105,
        (
            "#1165F#6P看来这就是\x01",
            "『光环轨道』了。\x02\x03",

            "#1382F是通过什么样的原理呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208C")

    label("loc_1EA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EFF")

    ChrTalk(    #58
        0x103,
        (
            "#026F#6P嗯……\x01",
            "看来这就是『光环轨道』了。\x02\x03",

            "#020F是通过什么样的原理呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208C")

    label("loc_1EFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F65")

    ChrTalk(    #59
        0x106,
        (
            "#053F#6P呼，\x01",
            "看来这就是『光环轨道』了。\x02\x03",

            "#555F虽然不知道是\x01",
            "通过什么样的原理……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208C")

    label("loc_1F65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FC6")

    ChrTalk(    #60
        0x108,
        (
            "#074F#6P呼呼。\x01",
            "看来这就是『光环轨道』了。\x02\x03",

            "#070F虽然完全不懂是什么原理……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208C")

    label("loc_1FC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2036")

    ChrTalk(    #61
        0x109,
        (
            "#1064F#6P哈……\x01",
            "看来这就是『光环轨道』了。\x02\x03",

            "#1068F虽然完全搞不清楚\x01",
            "是通过什么样的原理……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208C")

    label("loc_2036")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_208C")

    ChrTalk(    #62
        0x104,
        (
            "#035F#6P呼，看来这就是\x01",
            "『光环轨道』了。\x02\x03",

            "#030F虽然不了解其原理……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_208C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20FC")

    ChrTalk(    #63
        0x10B,
        (
            "#213F#6P……但感觉和帝国的\x01",
            "铁路有点相似。\x02\x03",

            "#413F不过，透明的轨道\x01",
            "还真令人有点胆战心惊啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235F")

    label("loc_20FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2166")

    ChrTalk(    #64
        0x104,
        (
            "#030F#6P呼，好像是帝国\x01",
            "铁路的进化版一样。\x02\x03",

            "#031F不过，透明的轨道\x01",
            "还是相当惊险的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235F")

    label("loc_2166")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21D0")

    ChrTalk(    #65
        0x109,
        (
            "#1064F#6P好像是一些国家使用的\x01",
            "铁路的进化版。\x02\x03",

            "#1068F透明的轨道\x01",
            "很让人感到不安啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235F")

    label("loc_21D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2238")

    ChrTalk(    #66
        0x108,
        (
            "#073F#6P像矿车一样\x01",
            "在轨道上跑的交通工具啊。\x02\x03",

            "#075F透明的轨道还真\x01",
            "让人不放心啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235F")

    label("loc_2238")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_229E")

    ChrTalk(    #67
        0x106,
        (
            "#555F#6P像矿车一样\x01",
            "在轨道上跑的交通工具啊。\x02\x03",

            "#551F透明的轨道真是\x01",
            "感觉怪怪的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235F")

    label("loc_229E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2302")

    ChrTalk(    #68
        0x103,
        (
            "#020F#6P像矿车一样\x01",
            "在轨道上跑的交通工具。\x02\x03",

            "#524F透明的轨道\x01",
            "总让人有点不安……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235F")

    label("loc_2302")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_235F")

    ChrTalk(    #69
        0x105,
        (
            "#1164F#6P好像是帝国铁路的\x01",
            "进化版一样。\x02\x03",

            "这透明的轨道\x01",
            "是用什么做出来呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23CA")

    ChrTalk(    #70
        0x107,
        (
            "#064F#6P说、说不定是\x01",
            "在空中展开了某种力场\x01",
            "所形成的轨道……\x02\x03",

            "#067F了、了不起的技术啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23CA")


    ChrTalk(    #71
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
    Jump("loc_2AAF")

    label("loc_2443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A0")
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

    def lambda_24B3():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_24B3)
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

    ChrTalk(    #72
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

    def lambda_2581():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2581)

    def lambda_2599():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2599)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_25C4():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_25C4)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x10)
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

    ChrTalk(    #73
        0x101,
        (
            "#1006F#6P好了，这样一来总算\x01",
            "可以使用这个东西了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#1040F#6P说得也是……\x01",
            "马上试试吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x220A)
    Jump("loc_2AAF")

    label("loc_26A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2899")
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

    def lambda_2715():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2715)
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

    def lambda_2782():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2782)

    def lambda_279A():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_279A)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_27C5():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27C5)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x10)
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

    ChrTalk(    #75
        0x101,
        (
            "#1015F#6P嗯，现在可以来往于\x01",
            "３个车站了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        (
            "#1040F#6P嗯……\x01",
            "变得相当方便了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x220B)
    Jump("loc_2AAF")

    label("loc_2899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAF")
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

    def lambda_290E():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_290E)
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

    def lambda_297B():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_297B)

    def lambda_2993():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2993)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_29BE():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29BE)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x10)
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

    ChrTalk(    #77
        0x102,
        (
            "#1035F#6P好……\x02\x03",

            "#1040F现在从『卡尔玛丽』\x01",
            "到『中枢塔』都能\x01",
            "方便地来回了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#1007F#6P呼……好长的距离啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x220C)
    OP_28(0x9F, 0x1, 0x2)

    label("loc_2AAF")

    OP_A2(0x2206)
    OP_28(0x9D, 0x1, 0x10)
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

    # Function_12_1BA0 end

    def Function_13_2B55(): pass

    label("Function_13_2B55")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xA3C, 0x1388, 0x47B8, 0x1388, 0x0)

    def lambda_2B80():

        label("loc_2B80")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2B80")

    QueueWorkItem2(0xFE, 2, lambda_2B80)
    Return()

    # Function_13_2B55 end

    def Function_14_2B8C(): pass

    label("Function_14_2B8C")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xE2E, 0x1388, 0x47CC, 0x1388, 0x0)

    def lambda_2BB7():

        label("loc_2BB7")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2BB7")

    QueueWorkItem2(0xFE, 2, lambda_2BB7)
    Return()

    # Function_14_2B8C end

    def Function_15_2BC3(): pass

    label("Function_15_2BC3")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0x8C0, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_2BEE():

        label("loc_2BEE")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2BEE")

    QueueWorkItem2(0xFE, 2, lambda_2BEE)
    Return()

    # Function_15_2BC3 end

    def Function_16_2BFA(): pass

    label("Function_16_2BFA")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xFE6, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_2C25():

        label("loc_2C25")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2C25")

    QueueWorkItem2(0xFE, 2, lambda_2C25)
    Return()

    # Function_16_2BFA end

    def Function_17_2C31(): pass

    label("Function_17_2C31")

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

    AnonymousTalk(    #79
        (
            "\x07\x05本站附近的大门锁定\x01",
            "已经解除。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #80
        "\x07\x05地下通道７８号已经可以使用了。\x02",
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
    OP_A2(0x220D)
    OP_28(0x9D, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_17_2C31 end

    def Function_18_2DBB(): pass

    label("Function_18_2DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC4")
    Return()

    label("loc_2DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3150")
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

    AnonymousTalk(    #81
        (
            "\x07\x05现在其它车站的紧急运行\x01",
            "模式尚未启动。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("合成音")

    AnonymousTalk(    #82
        "\x07\x05『光环轨道』无法使用。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F24")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2F58")

    label("loc_2F24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F46")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2F58")

    label("loc_2F46")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_2F58")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F7F")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2FB3")

    label("loc_2F7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FA1")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2FB3")

    label("loc_2FA1")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_2FB3")

    Sleep(1500)
    OP_63(0x101)
    OP_63(0x102)
    OP_63(0xF8)
    OP_63(0xF9)
    Sleep(500)

    ChrTalk(    #83
        0x101,
        "#1019F#6P……怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x102,
        (
            "#1035F#6P……看来不启动其他\x01",
            "车站的『紧急运行模式』的话，\x01",
            "就不能使用这个来移动了。\x02\x03",

            "#1040F很遗憾，\x01",
            "现在只能放弃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
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
    Jump("loc_31DA")

    label("loc_3150")

    EventBegin(0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #86
        (
            "\x07\x05现在其它车站的紧急运行\x01",
            "模式尚未启动。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("合成音")

    AnonymousTalk(    #87
        "\x07\x05『光环轨道』无法使用。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_31DA")

    Jump("loc_34B8")

    label("loc_31DD")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_END)), "loc_32BE")
    OP_CC(0x1, 0x0, "【第３５克雷德尔站】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_32BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_END)), "loc_32E7")
    OP_CC(0x1, 0x0, "【第７法克特里亚站】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_32E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_END)), "loc_330A")
    OP_CC(0x1, 0x0, "【中枢塔前站】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_330A")

    OP_CC(0x1, 0x0, "【放弃使用】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_334D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33CF")

    label("loc_334D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3357")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33CF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3371")
    Jump("loc_33CF")

    label("loc_3371")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33C2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_33AB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33A8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_33A8")

    Jump("loc_33C2")

    label("loc_33AB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3371")

    label("loc_33C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3357")

    label("loc_33CF")

    SetMapFlags(0x100000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_33ED"),
        (1, "loc_342B"),
        (2, "loc_3469"),
        (3, "loc_34A7"),
        (SWITCH_DEFAULT, "loc_34AA"),
    )


    label("loc_33ED")

    OP_A2(0x2210)
    OP_A2(0x2215)
    OP_43(0x101, 0x1, 0x0, 0x13)

    def lambda_3400():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_34AA")

    label("loc_342B")

    OP_A2(0x2210)
    OP_A2(0x2216)
    OP_43(0x101, 0x1, 0x0, 0x13)

    def lambda_343E():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_343E)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_34AA")

    label("loc_3469")

    OP_A2(0x2210)
    OP_A2(0x2217)
    OP_43(0x101, 0x1, 0x0, 0x13)

    def lambda_347C():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_347C)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_34AA")

    label("loc_34A7")

    Jump("loc_34AA")

    label("loc_34AA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    EventEnd(0x0)

    label("loc_34B8")

    Return()

    # Function_18_2DBB end

    def Function_19_34B9(): pass

    label("Function_19_34B9")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_43(0x101, 0x2, 0x0, 0x14)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x14)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x14)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x14)
    Sleep(1500)
    OP_6F(0x1, 950)
    OP_70(0x1, 0x44C)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 7)), scpexpr(EXPR_END)), "loc_3565")
    OP_6F(0x1, 1100)
    OP_70(0x1, 0x514)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_3530():
        OP_6D(8300, 5000, 21350, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3530)

    def lambda_3548():
        OP_6C(12000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3548)

    def lambda_3558():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3558)
    Jump("loc_35A0")

    label("loc_3565")

    OP_6F(0x1, 300)
    OP_70(0x1, 0x1F4)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_357E():
        OP_6D(-2860, 5000, 21710, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_357E)

    def lambda_3596():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3596)

    label("loc_35A0")

    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_19_34B9 end

    def Function_20_35B1(): pass

    label("Function_20_35B1")

    OP_8E(0xFE, 0xC08, 0x1388, 0x4A56, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC2, 0x13F6, 0x4F6A, 0x7D0, 0x0)

    def lambda_35DF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_35DF)
    OP_8E(0xFE, 0xC1C, 0x13F6, 0x5E9C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_35B1 end

    def Function_21_3605(): pass

    label("Function_21_3605")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 1)), scpexpr(EXPR_END)), "loc_370E")
    OP_6D(-9950, 5000, 20680, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_36F9():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_36F9)
    Jump("loc_3786")

    label("loc_370E")

    OP_6D(12690, 5000, 20450, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 1300)
    OP_70(0x1, 0x640)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_3764():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3764)

    def lambda_377C():
        OP_6C(0, 5500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_377C)

    label("loc_3786")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D3E")
    OP_43(0x101, 0x1, 0x0, 0x16)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x17)
    Sleep(800)

    def lambda_37E2():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37E2)

    def lambda_37FA():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_37FA)
    OP_43(0xF8, 0x1, 0x0, 0x18)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x19)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #88
        0x101,
        (
            "#1004F#4P好、好像一转眼\x01",
            "就到了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        (
            "#1035F#6P速度很快，\x01",
            "却几乎没有摇晃……\x02\x03",

            "#1040F真是了不起的技术。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1015F#4P确实如此……\x02\x03",

            "#1016F不过难得有那么棒的景色，\x01",
            "真想它能跑得慢一点，\x01",
            "让我好好欣赏一下……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3953")

    ChrTalk(    #91
        0x10B,
        (
            "#413F#5P真是的……\x01",
            "你还真是悠哉啊。\x02\x03",

            "#210F……不过确实也\x01",
            "有点可惜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A78")

    label("loc_3953")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_398D")

    ChrTalk(    #92
        0x107,
        (
            "#067F#5P嘿嘿……\x01",
            "的确可以这么说呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A78")

    label("loc_398D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39C2")

    ChrTalk(    #93
        0x105,
        (
            "#1168F#5P呵呵……\x01",
            "确实是这样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A78")

    label("loc_39C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39F1")

    ChrTalk(    #94
        0x103,
        "#021F#5P呵呵……有道理。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A78")

    label("loc_39F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A1D")

    ChrTalk(    #95
        0x109,
        "#1061F#5P哈哈，没错～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A78")

    label("loc_3A1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A4E")

    ChrTalk(    #96
        0x104,
        "#031F#5P呵呵……我有同感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A78")

    label("loc_3A4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A78")

    ChrTalk(    #97
        0x108,
        "#071F#5P哈哈……没错。\x02",
    )

    CloseMessageWindow()

    label("loc_3A78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ADF")

    ChrTalk(    #98
        0x106,
        (
            "#051F#5P不过，多亏有这东西，\x01",
            "探索变得轻松许多了。\x02\x03",

            "发现了新的车站\x01",
            "就赶紧启用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D38")

    label("loc_3ADF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B40")

    ChrTalk(    #99
        0x108,
        (
            "#070F#5P不过，有了这个，\x01",
            "探索就方便得多了。\x02\x03",

            "发现了新的车站\x01",
            "就赶紧启用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D38")

    label("loc_3B40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BA8")

    ChrTalk(    #100
        0x104,
        (
            "#035F#5P呵呵，有了这个\x01",
            "探索就方便得多了。\x02\x03",

            "#030F发现了新的车站\x01",
            "还真想赶紧启用啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D38")

    label("loc_3BA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C08")

    ChrTalk(    #101
        0x109,
        (
            "#1060F#5P不过，有了这个\x01",
            "探索就方便得多了。\x02\x03",

            "发现了新的车站\x01",
            "就赶紧启用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D38")

    label("loc_3C08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C67")

    ChrTalk(    #102
        0x103,
        (
            "#027F#5P不过，有了这个\x01",
            "探索就方便得多了。\x02\x03",

            "发现了新的车站\x01",
            "就赶紧启用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D38")

    label("loc_3C67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CD1")

    ChrTalk(    #103
        0x105,
        (
            "#1167F#5P不过，有了这个\x01",
            "探索就方便得多了。\x02\x03",

            "#1168F发现了新的车站\x01",
            "还真想赶紧启用呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D38")

    label("loc_3CD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D38")

    ChrTalk(    #104
        0x107,
        (
            "#061F#5P嘿嘿，不过有了这个\x01",
            "探索就轻松许多了阿⊙\x02\x03",

            "#560F发现了新的车站\x01",
            "就赶快启用吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D38")

    OP_A2(0x220F)
    Jump("loc_3D96")

    label("loc_3D3E")

    OP_43(0x101, 0x1, 0x0, 0x16)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x17)
    Sleep(800)

    def lambda_3D5C():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D5C)

    def lambda_3D74():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3D74)
    OP_43(0xF8, 0x1, 0x0, 0x18)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x19)
    Sleep(500)

    label("loc_3D96")

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

    # Function_21_3605 end

    def Function_22_3E48(): pass

    label("Function_22_3E48")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3E5E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E5E)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xECE, 0x1388, 0x4376, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    ClearChrFlags(0xFE, 0x80)
    Return()

    # Function_22_3E48 end

    def Function_23_3E9F(): pass

    label("Function_23_3E9F")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3EB5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3EB5)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9F6, 0x1388, 0x4362, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_23_3E9F end

    def Function_24_3EF1(): pass

    label("Function_24_3EF1")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3F07():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F07)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1086, 0x1388, 0x4808, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_24_3EF1 end

    def Function_25_3F43(): pass

    label("Function_25_3F43")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3F59():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F59)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7B2, 0x1388, 0x47A4, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_25_3F43 end

    def Function_26_3F95(): pass

    label("Function_26_3F95")

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

    def lambda_4041():
        OP_6D(-13000, -25000, 490, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4041)

    def lambda_4059():
        OP_67(0, 3890, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4059)

    def lambda_4071():
        OP_6B(5200, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4071)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x1C3)
    Sleep(500)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C5901   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_26_3F95 end

    def Function_27_40A0(): pass

    label("Function_27_40A0")

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

    def lambda_4146():
        OP_6D(-13000, 0, 2000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4146)

    def lambda_415E():
        OP_67(0, 3880, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_415E)
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

    # Function_27_40A0 end

    def Function_28_425B(): pass

    label("Function_28_425B")

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
        (0, "loc_42D5"),
        (1, "loc_42DB"),
        (SWITCH_DEFAULT, "loc_42E1"),
    )


    label("loc_42D5")

    OP_A2(0x1200)
    Jump("loc_42E1")

    label("loc_42DB")

    OP_A2(0x1201)
    Jump("loc_42E1")

    label("loc_42E1")

    Return()

    # Function_28_425B end

    def Function_29_42E2(): pass

    label("Function_29_42E2")

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

    # Function_29_42E2 end

    def Function_30_4373(): pass

    label("Function_30_4373")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #105
        (
            "\x07\x05≡ 前面的月台\x01",
            "　　　西卡尔玛丽站\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_30_4373 end

    SaveToFile()

Try(main)
