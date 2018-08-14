from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5503   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5503.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60233",
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
        '亚妮拉丝',                             # 9
        '野狼',                                 # 10
        '野狼',                                 # 11
        '封印石⑨',                             # 12
        '',                                     # 13
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
        'ED6_DT07/CH00420 ._CH',             # 00
        'ED6_DT07/CH00421 ._CH',             # 01
        'ED6_DT29/CH15070 ._CH',             # 02
        'ED6_DT29/CH15071 ._CH',             # 03
        'ED6_DT26/CH20621 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH00420P._CP',             # 00
        'ED6_DT07/CH00421P._CP',             # 01
        'ED6_DT29/CH15070P._CP',             # 02
        'ED6_DT29/CH15071P._CP',             # 03
        'ED6_DT26/CH20621P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -1750,
        Y                   = -1000,
        Z                   = 199430,
        Range               = 3280,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x31ECA,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = -14010,
        TriggerZ            = 0,
        TriggerY            = 202210,
        TriggerRange        = 1000,
        ActorX              = -14010,
        ActorZ              = 2000,
        ActorY              = 202210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 30500,
        TriggerZ            = 0,
        TriggerY            = 202010,
        TriggerRange        = 1000,
        ActorX              = 30500,
        ActorZ              = 1000,
        ActorY              = 202010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BA",          # 00, 0
        "Function_1_1CB",          # 01, 1
        "Function_2_205",          # 02, 2
        "Function_3_32B",          # 03, 3
        "Function_4_DF4",          # 04, 4
        "Function_5_E22",          # 05, 5
        "Function_6_E55",          # 06, 6
        "Function_7_E88",          # 07, 7
        "Function_8_EBB",          # 08, 8
        "Function_9_EDC",          # 09, 9
        "Function_10_EED",         # 0A, 10
        "Function_11_15EA",        # 0B, 11
        "Function_12_1A96",        # 0C, 12
        "Function_13_1ABA",        # 0D, 13
        "Function_14_1ADE",        # 0E, 14
        "Function_15_1B02",        # 0F, 15
        "Function_16_1B26",        # 10, 16
        "Function_17_1B7B",        # 11, 17
        "Function_18_1BE3",        # 12, 18
        "Function_19_1C4B",        # 13, 19
        "Function_20_1EE8",        # 14, 20
        "Function_21_1F30",        # 15, 21
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CA")
    Event(0, 3)

    label("loc_1CA")

    Return()

    # Function_0_1BA end

    def Function_1_1CB(): pass

    label("Function_1_1CB")

    OP_1B(0x0, 0x0, 0x15)
    OP_22(0x85, 0x1, 0x4B)
    SetMapFlags(0x100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB")
    OP_82(0xA9, 0x0)
    OP_82(0xAA, 0x0)
    OP_82(0xAC, 0x0)

    label("loc_1EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x532, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD")
    OP_6F(0x2, 0)
    Jump("loc_204")

    label("loc_1FD")

    OP_6F(0x2, 60)

    label("loc_204")

    Return()

    # Function_1_1CB end

    def Function_2_205(): pass

    label("Function_2_205")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x532, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18A, 1)"), scpexpr(EXPR_END)), "loc_279")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x8A\x01\x07\x00。\x02",
    )

    Jump("loc_25E")

    label("loc_25E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2994)
    Jump("loc_2E7")

    label("loc_279")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x8A\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x8A\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2C8")

    label("loc_2C8")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_2E7")

    Jump("loc_31D")

    label("loc_2EA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_31D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_205 end

    def Function_3_32B(): pass

    label("Function_3_32B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_22(0x85, 0x1, 0x46)
    OP_43(0x10, 0x0, 0x0, 0x8)
    SetChrPos(0x109, 8910, 4000, 5150, 270)
    SetChrPos(0x102, 9200, 4000, 6540, 270)
    SetChrPos(0xF0, 8910, 4000, 5150, 270)
    SetChrPos(0xF1, 9200, 4000, 6540, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(2000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #3
        (
            "\x07\x00#1063F……这还真是阴暗的楼梯啊。\x02\x03",

            "#1065F反正是处于地下的水路，\x01",
            "也是没有办法的事情。\x02",
        )
    )

    Jump("loc_438")

    label("loc_438")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 100, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #4
        (
            "\x07\x00#1500F看起来，\x01",
            "这是由古代遗迹改造而成的训练场。\x02",
        )
    )

    Jump("loc_490")

    label("loc_490")

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_532")
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #5
        (
            "\x07\x00#065F话、话说回来……\x01",
            "从刚才开始就觉得有点热呢。\x02\x03",

            "这里不是地下水路吗，\x01",
            "我觉得应该会很凉快才对啊……\x02",
        )
    )

    Jump("loc_52C")

    label("loc_52C")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_85B")

    label("loc_532")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DC")
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #6
        (
            "\x07\x00#1544F唔，姑且不说这个，\x01",
            "刚才就觉得莫名其妙地热了起来。\x02\x03",

            "#1547F我这套上等的宫廷服装\x01",
            "都被汗浸透了呢。\x02",
        )
    )

    Jump("loc_5D6")

    label("loc_5D6")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_85B")

    label("loc_5DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_675")
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("乔丝特")

    AnonymousTalk(    #7
        (
            "\x07\x00#413F话说回来……\x01",
            "不觉得开始热起来了吗？\x02\x03",

            "#210F这里是地下水路，\x01",
            "按道理应该会很凉快啊……\x02",
        )
    )

    Jump("loc_66F")

    label("loc_66F")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_85B")

    label("loc_675")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_712")
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("科洛丝")

    AnonymousTalk(    #8
        (
            "\x07\x00#1165F话说回来……\x01",
            "从刚才就觉得有点热了。\x02\x03",

            "#1382F这里不是地下水路吗，\x01",
            "应该会很凉快才对啊……\x02",
        )
    )

    Jump("loc_70C")

    label("loc_70C")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_85B")

    label("loc_712")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C1")
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("尤莉亚　　　　　　　")

    AnonymousTalk(    #9
        (
            "\x07\x00#175F话说回来……\x01",
            "觉得这儿似乎莫名其妙的热起来了。\x02\x03",

            "按道理，地下水路这地方\x01",
            "应该比地面要凉快很多才对啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_85B")

    label("loc_7C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85B")
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("穆拉")

    AnonymousTalk(    #10
        (
            "\x07\x00#276F……说起来，\x01",
            "从刚才开始就觉得有点热。\x02\x03",

            "按道理，地下水路这地方\x01",
            "应该比地面要凉快很多才对啊……\x02",
        )
    )

    Jump("loc_858")

    label("loc_858")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_85B")

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #11
        (
            "\x07\x00#1067F嗯……说的没错。\x02\x03",

            "而且从刚才开始，\x01",
            "就好像一直有一种\x01",
            "类似地震的声音……\x02",
        )
    )

    Jump("loc_8CF")

    label("loc_8CF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 100, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #12
        (
            "\x07\x00#1502F……楼梯差不多\x01",
            "该到头了吧。\x02",
        )
    )

    Jump("loc_919")

    label("loc_919")

    CloseMessageWindow()
    OP_56(0x0)
    OP_6D(3970, 1750, 6640, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_22(0x85, 0x1, 0x4B)
    OP_A2(0x0)
    OP_44(0x10, 0x0)

    def lambda_974():
        OP_6D(1500, 0, 7020, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_974)

    def lambda_98C():
        OP_67(0, 6420, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_98C)

    def lambda_9A4():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9A4)

    def lambda_9B4():
        OP_6E(280, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_9B4)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0x4)
    OP_43(0x102, 0x0, 0x0, 0x5)
    OP_43(0xF0, 0x0, 0x0, 0x6)
    OP_43(0xF1, 0x0, 0x0, 0x7)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A44")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AAB")

    label("loc_A44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AAB")

    label("loc_A6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A94")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AAB")

    label("loc_A94")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_AAB")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD8")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B3F")

    label("loc_AD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B00")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B3F")

    label("loc_B00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B28")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B3F")

    label("loc_B28")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B3F")

    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x2)

    ChrTalk(    #13
        0x102,
        "#1502F#5P这是……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCA")

    ChrTalk(    #14
        0x108,
        (
            "#075F#5P哎呀哎呀……\x01",
            "看来这里热也是理所当然的了 。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D14")

    label("loc_BCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0E")

    ChrTalk(    #15
        0x10D,
        "#272F#5P哼……这样的话这里肯定会热了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D14")

    label("loc_C0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C48")

    ChrTalk(    #16
        0x10E,
        "#176F#5P这……果然会很热啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D14")

    label("loc_C48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C89")

    ChrTalk(    #17
        0x105,
        "#1163F#5P这里这么热也可以理解了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D14")

    label("loc_C89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CCB")

    ChrTalk(    #18
        0x10B,
        "#216F#5P这、这样话这里肯定会很热啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D14")

    label("loc_CCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D14")

    ChrTalk(    #19
        0x104,
        (
            "#1544F#5P哎呀哎呀……\x01",
            "这样子热是当然的事情啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D14")


    ChrTalk(    #20
        0x109,
        (
            "#1075F#5P哼，无论怎么想\x01",
            "都觉得这儿不是平常的地方。\x02\x03",

            "#1840F会不会是敌人布下的机关呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#1505F#5P嗯嗯……\x01",
            "这么想也是很自然的。\x02\x03",

            "#1502F看来要更加小心谨慎才是。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2903)
    OP_28(0x32, 0x1, 0x100)
    OP_28(0x32, 0x1, 0x200)
    OP_1D(0xE9)
    Sleep(500)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_3_32B end

    def Function_4_DF4(): pass

    label("Function_4_DF4")


    def lambda_DFA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DFA)
    OP_8E(0xFE, 0xFFFFFE3E, 0x0, 0x14BE, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_DF4 end

    def Function_5_E22(): pass

    label("Function_5_E22")

    Sleep(300)

    def lambda_E2D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E2D)
    OP_8E(0xFE, 0xFFFFFD94, 0x0, 0x19FA, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_5_E22 end

    def Function_6_E55(): pass

    label("Function_6_E55")

    Sleep(600)

    def lambda_E60():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E60)
    OP_8E(0xFE, 0x366, 0x0, 0x148C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_E55 end

    def Function_7_E88(): pass

    label("Function_7_E88")

    Sleep(800)

    def lambda_E93():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E93)
    OP_8E(0xFE, 0x3FC, 0x0, 0x1A9A, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_7_E88 end

    def Function_8_EBB(): pass

    label("Function_8_EBB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EDB")
    OP_22(0x1B, 0x0, 0x64)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_ED8")
    Jump("loc_EDB")

    label("loc_ED8")

    Jump("Function_8_EBB")

    label("loc_EDB")

    Return()

    # Function_8_EBB end

    def Function_9_EDC(): pass

    label("Function_9_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 4)), scpexpr(EXPR_END)), "loc_EE4")
    Return()

    label("loc_EE4")

    Call(0, 10)
    Call(0, 11)
    Return()

    # Function_9_EDC end

    def Function_10_EED(): pass

    label("Function_10_EED")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    OP_E0(238, 0x45, 0x2)
    OP_E0(238, 0x46, 0x3)
    OP_E0(239, 0x47, 0x2)
    OP_E0(239, 0x48, 0x3)
    OP_E0(240, 0x49, 0x2)
    OP_E0(240, 0x4A, 0x3)
    OP_E0(241, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x3)
    OP_20(0x7D0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F98")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FFF")

    label("loc_F98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC0")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FFF")

    label("loc_FC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE8")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FFF")

    label("loc_FE8")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_FFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1027")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_108E")

    label("loc_1027")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_108E")

    label("loc_104F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1077")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_108E")

    label("loc_1077")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_108E")

    Sleep(1000)

    def lambda_1099():
        OP_6D(11980, 0, 202530, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1099)

    def lambda_10B1():
        OP_67(0, 7500, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_10B1)

    def lambda_10C9():
        OP_6B(2170, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_10C9)

    def lambda_10D9():
        OP_6E(324, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_10D9)

    def lambda_10E9():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_10E9)

    def lambda_10F7():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_10F7)

    def lambda_1105():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_1105)

    def lambda_1113():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_1113)
    WaitChrThread(0xEE, 0x2)
    SetChrPos(0xEE, -4000, 0, 201070, 90)
    SetChrPos(0xEF, -4740, 0, 202500, 90)
    SetChrPos(0xF0, -5880, 0, 201050, 90)
    SetChrPos(0xF1, -6500, 0, 202550, 90)
    Sleep(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 11420, 100, 201870, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 14000, 0, 203770, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, 14000, 0, 199870, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_122C():
        OP_6B(1900, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_122C)
    OP_22(0x85, 0x1, 0x64)

    def lambda_1241():

        label("loc_1241")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1241")

    QueueWorkItem2(0x109, 0, lambda_1241)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 11420, -3100, 201870, 270)
    SetChrSubChip(0x10, 0)
    OP_43(0x10, 0x0, 0x0, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 14000, -3100, 203770, 270)
    OP_43(0x11, 0x0, 0x0, 0x11)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 14000, -3100, 199870, 270)
    OP_43(0x12, 0x0, 0x0, 0x12)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_44(0x109, 0x0)
    OP_22(0x85, 0x1, 0x4B)
    OP_1D(0xC4)
    WaitChrThread(0x109, 0x1)
    Sleep(1000)

    ChrTalk(    #22
        0x102,
        "#1504F#2P亚妮拉丝……！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1307():
        OP_6D(8540, 0, 203300, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1307)

    def lambda_131F():
        OP_67(0, 6160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_131F)

    def lambda_1337():
        OP_6B(2050, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1337)

    def lambda_1347():
        OP_6E(412, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1347)
    OP_43(0x109, 0x0, 0x0, 0xC)
    OP_43(0x102, 0x0, 0x0, 0xD)
    OP_43(0xF0, 0x0, 0x0, 0xE)
    OP_43(0xF1, 0x0, 0x0, 0xF)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #23
        0x10,
        "#1313F#11P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1063F#6P看起来，这是和之前一样\x01",
            "被『格利摩尔』所拟态出来的。\x02\x03",

            "完全感觉不到灵魂的气息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1505F#6P也就是说……\x01",
            "我们没必要缩手缩脚的。\x02\x03",

            "#1506F全力攻击吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_148C():
        OP_6D(8840, 0, 202800, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_148C)

    def lambda_14A4():
        OP_67(0, 6580, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_14A4)

    def lambda_14BC():
        OP_6B(1700, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_14BC)

    def lambda_14CC():
        OP_6E(360, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14CC)
    SetChrChipByIndex(0x10, 1)

    def lambda_14E1():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_14E1)

    def lambda_14FC():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_14FC)
    Sleep(10)

    def lambda_151C():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_151C)
    SetChrChipByIndex(0x11, 3)

    def lambda_153C():

        label("loc_153C")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_153C")

    QueueWorkItem2(0x11, 3, lambda_153C)

    def lambda_154F():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFE0C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_154F)
    Sleep(10)

    def lambda_156F():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_156F)
    SetChrChipByIndex(0x12, 3)

    def lambda_158F():

        label("loc_158F")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_158F")

    QueueWorkItem2(0x12, 3, lambda_158F)

    def lambda_15A2():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x1F4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_15A2)
    Sleep(10)

    def lambda_15C2():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_15C2)
    WaitChrThread(0x109, 0x1)
    Battle(0x1A3, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_10_EED end

    def Function_11_15EA(): pass

    label("Function_11_15EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x109, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    OP_E0(238, 0x45, 0x2)
    OP_E0(238, 0x46, 0x3)
    OP_E0(239, 0x47, 0x2)
    OP_E0(239, 0x48, 0x3)
    OP_E0(240, 0x49, 0x2)
    OP_E0(240, 0x4A, 0x3)
    OP_E0(241, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x3)
    SetChrPos(0xEE, 6670, 0, 201380, 90)
    SetChrPos(0xEF, 6570, 0, 203010, 90)
    SetChrPos(0xF0, 4810, 0, 201060, 90)
    SetChrPos(0xF1, 4760, 0, 202870, 90)
    SetChrChipByIndex(0xEE, 5)
    SetChrSubChip(0xEE, 0)
    SetChrChipByIndex(0xEF, 7)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 9)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 11)
    SetChrSubChip(0xF1, 0)
    OP_6D(8790, 0, 202960, 0)
    OP_67(0, 6310, -10000, 0)
    OP_6B(2120, 0)
    OP_6C(45000, 0)
    OP_6E(389, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, 10500, 1200, 201870, 0)
    PlayEffect(0x7, 0x7, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)

    def lambda_1827():
        OP_6D(10000, 0, 203500, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1827)

    def lambda_183F():
        OP_67(0, 6140, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_183F)
    OP_8E(0x109, 0x251C, 0x0, 0x31498, 0x7D0, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 4)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x13, 0x2710, 0x4B0, 0x313E4, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x13, 0x80)
    OP_0D()
    Sleep(150)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x00得到了\x1F\x5A\x03\x07\x00。\x02",
    )

    Jump("loc_18E9")

    label("loc_18E9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x35A, 1)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #27
        0x102,
        (
            "#1513F#6P呼……\x01",
            "这样暂时就解决了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #28
        0x109,
        (
            "#1075F#11P嗯……\x01",
            "是谁被关在里面，\x01",
            "应该不言自明了。\x02\x03",

            "#1840F暂且先回据点吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2904)
    OP_28(0x32, 0x1, 0x400)
    OP_28(0x32, 0x1, 0x800)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(10180, 0, 201880, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 10180, 0, 201880, 270)
    SetChrPos(0x1, 10180, 0, 201880, 270)
    SetChrPos(0x2, 10180, 0, 201880, 270)
    SetChrPos(0x3, 10180, 0, 201880, 270)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_11_15EA end

    def Function_12_1A96(): pass

    label("Function_12_1A96")

    OP_8E(0xFE, 0x13E2, 0x0, 0x31286, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_1A96 end

    def Function_13_1ABA(): pass

    label("Function_13_1ABA")

    OP_8E(0xFE, 0x139C, 0x0, 0x318DA, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_13_1ABA end

    def Function_14_1ADE(): pass

    label("Function_14_1ADE")

    OP_8E(0xFE, 0xD66, 0x0, 0x31128, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_14_1ADE end

    def Function_15_1B02(): pass

    label("Function_15_1B02")

    OP_8E(0xFE, 0xDCA, 0x0, 0x31916, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_15_1B02 end

    def Function_16_1B26(): pass

    label("Function_16_1B26")

    PlayEffect(0x1, 0x3, 0xFF, 11420, 100, 201870, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x3, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_16_1B26 end

    def Function_17_1B7B(): pass

    label("Function_17_1B7B")

    PlayEffect(0x1, 0x4, 0xFF, 14000, 0, 203770, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_1BB6():

        label("loc_1BB6")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1BB6")

    QueueWorkItem2(0xFE, 3, lambda_1BB6)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_17_1B7B end

    def Function_18_1BE3(): pass

    label("Function_18_1BE3")

    PlayEffect(0x1, 0x5, 0xFF, 14000, 0, 199870, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_1C1E():

        label("loc_1C1E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1C1E")

    QueueWorkItem2(0xFE, 3, lambda_1C1E)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_18_1BE3 end

    def Function_19_1C4B(): pass

    label("Function_19_1C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D1A")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0xA9, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xAA, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xAC, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(3072)
    Sleep(500)
    Jump("loc_1D1D")

    label("loc_1D1A")

    TalkBegin(0xFF)

    label("loc_1D1D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #29
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_1D47")

    label("loc_1D47")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB2")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_1DAC")

    label("loc_1DAC")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1DC9"),
        (1, "loc_1E44"),
        (2, "loc_1E73"),
        (SWITCH_DEFAULT, "loc_1EA2"),
    )


    label("loc_1DC9")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE9)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EAF")

    label("loc_1E44")

    OP_A9(0x1E)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #30
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_1E70")

    label("loc_1E70")

    Jump("loc_1EAF")

    label("loc_1E73")

    OP_A9(0x6)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #31
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_1E9F")

    label("loc_1E9F")

    Jump("loc_1EAF")

    label("loc_1EA2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EAF")

    label("loc_1EAF")

    Jump("loc_1D5A")

    label("loc_1EB2")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDF")
    OP_A2(0x258F)
    EventEnd(0x1)
    Jump("loc_1EE2")

    label("loc_1EDF")

    TalkEnd(0xFF)

    label("loc_1EE2")

    SetMapFlags(0x100000)
    Return()

    # Function_19_1C4B end

    def Function_20_1EE8(): pass

    label("Function_20_1EE8")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #32
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_1EE8 end

    def Function_21_1F30(): pass

    label("Function_21_1F30")

    ClearMapFlags(0x2000000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_1F53")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F64")

    label("loc_1F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_1F64")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F64")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1F89"),
        (1, "loc_1FB8"),
        (2, "loc_1FE7"),
        (SWITCH_DEFAULT, "loc_2016"),
    )


    label("loc_1F89")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP001._CH")
    Jump("loc_2016")

    label("loc_1FB8")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    Jump("loc_2016")

    label("loc_1FE7")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP003._CH")
    Jump("loc_2016")

    label("loc_2016")

    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_204B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B8")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2076"),
        (1, "loc_20A2"),
        (2, "loc_20DF"),
        (SWITCH_DEFAULT, "loc_2131"),
    )


    label("loc_2076")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
        )
    )

    Jump("loc_2131")

    label("loc_20A2")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
            "【圣科洛瓦森林】\x01",      # 2
        )
    )

    Jump("loc_2131")

    label("loc_20DF")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",            # 0
            "【巴斯塔尔水道】\x01",          # 1
            "【圣科洛瓦森林】\x01",          # 2
            "【格林姆瑟尔小要塞】\x01",      # 3
        )
    )

    Jump("loc_2131")

    label("loc_2131")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_215B"),
        (1, "loc_21EF"),
        (2, "loc_2285"),
        (3, "loc_231B"),
        (SWITCH_DEFAULT, "loc_23B5"),
    )


    label("loc_215B")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #33
        "\x07\x05要移动至【训练场宿舍】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_21BA")

    label("loc_21BA")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21DC"),
        (1, "loc_21E9"),
        (SWITCH_DEFAULT, "loc_21EC"),
    )


    label("loc_21DC")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21EC")

    label("loc_21E9")

    Jump("loc_21EC")

    label("loc_21EC")

    Jump("loc_23B5")

    label("loc_21EF")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #34
        "\x07\x05要移动至【巴斯塔尔水道】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_2250")

    label("loc_2250")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2272"),
        (1, "loc_227F"),
        (SWITCH_DEFAULT, "loc_2282"),
    )


    label("loc_2272")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2282")

    label("loc_227F")

    Jump("loc_2282")

    label("loc_2282")

    Jump("loc_23B5")

    label("loc_2285")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #35
        "\x07\x05要移动至【圣科洛瓦森林】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_22E6")

    label("loc_22E6")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2308"),
        (1, "loc_2315"),
        (SWITCH_DEFAULT, "loc_2318"),
    )


    label("loc_2308")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2318")

    label("loc_2315")

    Jump("loc_2318")

    label("loc_2318")

    Jump("loc_23B5")

    label("loc_231B")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #36
        "\x07\x05要移动至【格林姆瑟尔小要塞】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_2380")

    label("loc_2380")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23A2"),
        (1, "loc_23AF"),
        (SWITCH_DEFAULT, "loc_23B2"),
    )


    label("loc_23A2")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23B2")

    label("loc_23AF")

    Jump("loc_23B2")

    label("loc_23B2")

    Jump("loc_23B5")

    label("loc_23B5")

    Jump("loc_204B")

    label("loc_23B8")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_23D1"),
        (1, "loc_2405"),
        (2, "loc_2439"),
        (3, "loc_246D"),
        (SWITCH_DEFAULT, "loc_24A1"),
    )


    label("loc_23D1")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_24A1")

    label("loc_2405")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_24A1")

    label("loc_2439")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_24A1")

    label("loc_246D")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_24A1")

    label("loc_24A1")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapFlags(0x100000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_24C8"),
        (1, "loc_24E8"),
        (2, "loc_24F4"),
        (3, "loc_2500"),
        (SWITCH_DEFAULT, "loc_250C"),
    )


    label("loc_24C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24DC")
    NewScene("ED6_DT21/U5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_24E5")

    label("loc_24DC")

    NewScene("ED6_DT21/U5102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_24E5")

    Jump("loc_250C")

    label("loc_24E8")

    NewScene("ED6_DT21/M5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_250C")

    label("loc_24F4")

    NewScene("ED6_DT21/M5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_250C")

    label("loc_2500")

    NewScene("ED6_DT21/M5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_250C")

    label("loc_250C")

    Return()

    # Function_21_1F30 end

    SaveToFile()

Try(main)
