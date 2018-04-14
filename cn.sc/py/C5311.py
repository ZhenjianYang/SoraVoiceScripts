from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5311   ._SN',
        MapName             = 'Other',
        Location            = 'C5311.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60064",
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
        '歼灭天使玲',                           # 9
        '帕蒂尔·玛蒂尔',                       # 10
        '目标用照相机',                         # 11
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
        TriggerX            = -32500,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = -32500,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_12E",          # 00, 0
        "Function_1_177",          # 01, 1
        "Function_2_1B8",          # 02, 2
        "Function_3_3FD",          # 03, 3
        "Function_4_406",          # 04, 4
        "Function_5_182D",         # 05, 5
        "Function_6_3310",         # 06, 6
        "Function_7_3391",         # 07, 7
        "Function_8_3406",         # 08, 8
        "Function_9_342C",         # 09, 9
        "Function_10_3452",        # 0A, 10
        "Function_11_3478",        # 0B, 11
        "Function_12_39A4",        # 0C, 12
        "Function_13_3A0E",        # 0D, 13
        "Function_14_3B23",        # 0E, 14
        "Function_15_3BAA",        # 0F, 15
    )


    def Function_0_12E(): pass

    label("Function_0_12E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_148")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 11)
    Jump("loc_176")

    label("loc_148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_159")
    OP_A3(0x10F1)
    Event(0, 13)
    Jump("loc_176")

    label("loc_159")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_176")

    Return()

    # Function_0_12E end

    def Function_1_177(): pass

    label("Function_1_177")

    OP_22(0x1C3, 0x1, 0x64)
    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 3)), scpexpr(EXPR_END)), "loc_191")
    OP_64(0x0, 0x1)
    OP_71(0x2, 0x4)

    label("loc_191")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x463), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AE")

    Call(0, 2)
    OP_72(0x0, 0x4)

    label("loc_1B7")

    Return()

    # Function_1_177 end

    def Function_2_1B8(): pass

    label("Function_2_1B8")

    OP_D2(0x2701C7, 0x2701CC, 0x0)
    OP_D2(0x270110, 0x270120, 0x1)
    OP_D2(0x270111, 0x270121, 0x2)
    OP_D2(0x270130, 0x270140, 0x3)
    OP_D2(0x270131, 0x270141, 0x4)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_213"),
        (5, "loc_22A"),
        (3, "loc_241"),
        (4, "loc_258"),
        (6, "loc_26F"),
        (7, "loc_286"),
        (8, "loc_29D"),
        (10, "loc_2B4"),
        (SWITCH_DEFAULT, "loc_2CB"),
    )


    label("loc_213")

    OP_D2(0x701D0, 0x701DC, 0x5)
    OP_D2(0x701D1, 0x701DD, 0x6)
    Jump("loc_2CB")

    label("loc_22A")

    OP_D2(0x70218, 0x70224, 0x5)
    OP_D2(0x70219, 0x70225, 0x6)
    Jump("loc_2CB")

    label("loc_241")

    OP_D2(0x701E8, 0x701F4, 0x5)
    OP_D2(0x701E9, 0x701F5, 0x6)
    Jump("loc_2CB")

    label("loc_258")

    OP_D2(0x27036E, 0x27037B, 0x5)
    OP_D2(0x27036F, 0x27037C, 0x6)
    Jump("loc_2CB")

    label("loc_26F")

    OP_D2(0x70230, 0x7023C, 0x5)
    OP_D2(0x70231, 0x7023D, 0x6)
    Jump("loc_2CB")

    label("loc_286")

    OP_D2(0x70248, 0x70254, 0x5)
    OP_D2(0x70249, 0x70255, 0x6)
    Jump("loc_2CB")

    label("loc_29D")

    OP_D2(0x270176, 0x270183, 0x5)
    OP_D2(0x270177, 0x270184, 0x6)
    Jump("loc_2CB")

    label("loc_2B4")

    OP_D2(0x702B4, 0x702BB, 0x5)
    OP_D2(0x702B5, 0x702BC, 0x6)
    Jump("loc_2CB")

    label("loc_2CB")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_2F4"),
        (5, "loc_30B"),
        (3, "loc_322"),
        (4, "loc_339"),
        (6, "loc_350"),
        (7, "loc_367"),
        (8, "loc_37E"),
        (10, "loc_395"),
        (SWITCH_DEFAULT, "loc_3AC"),
    )


    label("loc_2F4")

    OP_D2(0x701D0, 0x701DC, 0x7)
    OP_D2(0x701D1, 0x701DD, 0x8)
    Jump("loc_3AC")

    label("loc_30B")

    OP_D2(0x70218, 0x70224, 0x7)
    OP_D2(0x70219, 0x70225, 0x8)
    Jump("loc_3AC")

    label("loc_322")

    OP_D2(0x701E8, 0x701F4, 0x7)
    OP_D2(0x701E9, 0x701F5, 0x8)
    Jump("loc_3AC")

    label("loc_339")

    OP_D2(0x27036E, 0x27037B, 0x7)
    OP_D2(0x27036F, 0x27037C, 0x8)
    Jump("loc_3AC")

    label("loc_350")

    OP_D2(0x70230, 0x7023C, 0x7)
    OP_D2(0x70231, 0x7023D, 0x8)
    Jump("loc_3AC")

    label("loc_367")

    OP_D2(0x70248, 0x70254, 0x7)
    OP_D2(0x70249, 0x70255, 0x8)
    Jump("loc_3AC")

    label("loc_37E")

    OP_D2(0x270176, 0x270183, 0x7)
    OP_D2(0x270177, 0x270184, 0x8)
    Jump("loc_3AC")

    label("loc_395")

    OP_D2(0x702B4, 0x702BB, 0x7)
    OP_D2(0x702B5, 0x702BC, 0x8)
    Jump("loc_3AC")

    label("loc_3AC")

    OP_D2(0x27023E, 0x270248, 0x9)
    OP_D2(0x270244, 0x27024E, 0xA)
    OP_D2(0x2601CF, 0x2601D4, 0xB)
    OP_D2(0x2601D0, 0x2601D5, 0xC)
    OP_D2(0x270246, 0x270250, 0xD)
    OP_D2(0x2600D3, 0x2600D8, 0xE)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    Return()

    # Function_2_1B8 end

    def Function_3_3FD(): pass

    label("Function_3_3FD")

    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_3FD end

    def Function_4_406(): pass

    label("Function_4_406")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_427")
    Call(0, 14)
    Call(0, 15)

    label("loc_427")

    Call(0, 2)
    LoadEffect(0x0, "battle\\\\mgaria0.eff")
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    OP_A1(0x9, 0x0)
    SetChrPos(0x9, -23640, 20000, 120, 90)
    OP_72(0x0, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x1)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(18160, 0, 1020, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 23580, 0, -420, 270)
    SetChrPos(0x102, 23550, 0, 850, 270)
    SetChrPos(0xF8, 24710, 0, -660, 270)
    SetChrPos(0xF9, 24630, 0, 720, 270)

    def lambda_534():
        OP_6B(3960, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_534)

    def lambda_544():
        OP_8E(0xFE, 0x4556, 0x0, 0xFFFFFE5C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_544)
    Sleep(80)

    def lambda_564():
        OP_8E(0xFE, 0x44AC, 0x0, 0x352, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_564)
    Sleep(100)

    def lambda_584():
        OP_8E(0xFE, 0x4A6A, 0x0, 0xFFFFFD6C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_584)
    Sleep(150)

    def lambda_5A4():
        OP_8E(0xFE, 0x49C0, 0x0, 0x2D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5A4)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, -18090, 0, 240, 90)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #0
        0x8,
        "少女的声音",
        (
            "嘻嘻……\x01",
            "你们果然还是来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x1F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_677")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6B5")

    label("loc_677")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69E")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6B5")

    label("loc_69E")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6B5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E1")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_71F")

    label("loc_6E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_708")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_71F")

    label("loc_708")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_71F")

    Sleep(500)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_731():
        OP_6D(-18810, 0, 1110, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_731)

    def lambda_749():
        OP_67(0, 5310, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_749)

    def lambda_761():
        OP_6B(3430, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_761)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_794")

    ChrTalk(    #1
        0x107,
        "#065F啊……\x02",
    )

    CloseMessageWindow()

    label("loc_794")


    ChrTalk(    #2
        0x101,
        "#1002F……玲！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        "#1042F果然是你……\x02",
    )

    CloseMessageWindow()

    def lambda_7C6():
        OP_8E(0xFE, 0xFFFFDCEC, 0x0, 0xFFFFFE3E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C6)

    def lambda_7E1():
        OP_6D(-14650, 0, 2440, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E1)

    def lambda_7F9():
        OP_67(0, 3910, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7F9)

    def lambda_811():
        OP_6B(3680, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_811)

    def lambda_821():
        OP_6E(311, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_821)
    Sleep(300)

    def lambda_836():
        OP_8E(0xFE, 0xFFFFDD82, 0x0, 0x316, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_836)
    Sleep(100)

    def lambda_856():
        OP_8E(0xFE, 0xFFFFE46C, 0x0, 0xFFFFFBB4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_856)
    Sleep(300)
    OP_8E(0xF9, 0xFFFFE444, 0x0, 0x172, 0x1770, 0x0)
    WaitChrThread(0x102, 0x2)
    Sleep(500)

    ChrTalk(    #4
        0x8,
        (
            "#1306F#5P要打倒那三个人\x01",
            "是很难的……\x02\x03",

            "#261F但艾丝蒂尔和约修亚\x02\x03",

            "是一定会来找玲的。\x01",
            "玲一直都坚信不移呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1002F#6P玲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1043F#6P如此说来……\x01",
            "你还是准备同我们一战吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#263F#5P嘿嘿嘿，该怎么办好呢。\x02\x03",

            "以前都约定好了，\x01",
            "再次见面时要把你们都杀死，\x01",
            "但上次在城里相遇时又错过了好机会……\x02\x03",

            "#1306F算啦，只要艾丝蒂尔的态度正确，\x01",
            "玲饶了你们也是可以的哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1015F#6P我的……态度？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#261F#5P呵呵……很简单啦。\x02\x03",

            "#265F你只要收回上次\x01",
            "对玲说过的话就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1020F#6P哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#265F#5P上次你说过，玲待在\x01",
            "『结社』是错误的，对吧？\x02\x03",

            "只要你将这句话收回，\x01",
            "玲就马上离开。\x02\x03",

            "#261F怎么样，这交易不坏吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1026F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B3E")

    ChrTalk(    #13
        0x107,
        "#063F#4P小玲……\x02",
    )

    CloseMessageWindow()

    label("loc_B3E")


    ChrTalk(    #14
        0x102,
        (
            "#1042F#6P玲……\x01",
            "这样的交易有什么价值呢？\x02\x03",

            "即使你听到了想听的话，\x01",
            "但如果不是发自真心，也是没有意义的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1010F#6P约修亚……没关系。\x02\x03",

            "#1025F接下来……\x01",
            "就交给我可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1044F#2P艾丝蒂尔……\x02\x03",

            "#1035F明白了……拜托你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#1025F#6P……谢谢。\x02",
    )

    CloseMessageWindow()

    def lambda_C43():
        OP_6D(-16000, 0, 2180, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C43)

    def lambda_C5B():
        OP_67(0, 3400, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C5B)

    def lambda_C73():
        OP_6B(3440, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C73)
    OP_8F(0x101, 0xFFFFD72E, 0x0, 0x1E, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #18
        0x8,
        (
            "#261F#5P呵呵，你终于肯\x01",
            "答应了吗？\x02\x03",

            "#265F好～快点说吧！\x02\x03",

            "说玲待在『结社』\x01",
            "并没有任何错误。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1007F#6P玲……\x02\x03",

            "#1019F……撒娇也要\x01",
            "有个限度。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0x8,
        "#264F#5P…………咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1002F#6P世界不是以玲\x01",
            "为中心运转的。\x02\x03",

            "不会因为玲的任性\x01",
            "要求而改变。\x02\x03",

            "#1003F虽然玲拥有着\x01",
            "如此强大的力量……\x02\x03",

            "又有那位巨大的爸爸妈妈\x01",
            "来帮助你……\x02\x03",

            "#1010F但即便如此……\x01",
            "也无法改变别人的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "#262F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1007F#6P不希望玲呆在结社，\x01",
            "可能只是我一厢情愿的想法。\x02\x03",

            "所以我并没打算勉强你……\x02\x03",

            "#1025F但如果可能的话，\x01",
            "我希望玲能明白一点。\x02\x03",

            "无论什么时候，你都可以\x01",
            "像约修亚一样回头的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1040F#2P………艾丝蒂尔…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#1300F…………………………………\x02\x03",

            "#266F…………是吗…………………\x02\x03",

            "好心好意给你们一个机会，\x01",
            "你却枉费了我的苦心……\x02\x03",

            "#1306F你真是个无可救药的大傻瓜。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 14)

    def lambda_FCF():
        OP_99(0x8, 0xE, 0x8, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FCF)
    WaitChrThread(0x8, 0x1)
    Sleep(200)

    def lambda_FE9():
        OP_99(0x8, 0x8, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FE9)
    Sleep(200)
    Fade(500)

    def lambda_1003():
        OP_6B(3300, 0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1003)
    OP_22(0x1F9, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_1022():
        OP_99(0x8, 0x2, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1022)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 0)
    OP_0D()

    def lambda_103D():
        OP_6D(-13120, 0, 1130, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_103D)

    def lambda_1055():
        OP_6B(3510, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1055)

    def lambda_1065():
        OP_6C(302000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1065)
    Sleep(500)
    SetChrChipByIndex(0x8, 10)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x113, 0x0, 0x50)

    def lambda_10E3():

        label("loc_10E3")

        OP_7C(0xA, 0xA, 0x3E8, 0x3E8)
        OP_48()
        Jump("loc_10E3")

    QueueWorkItem2(0x101, 2, lambda_10E3)
    Sleep(500)
    OP_43(0x102, 0x0, 0x0, 0x6)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x102, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0xF8, 5)
    SetChrChipByIndex(0xF9, 7)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #26
        0x101,
        (
            "#1003F#5P……各位，对不起。\x02\x03",

            "这场战斗或许\x01",
            "原本可以避免的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#1035F#2P……你没有必要道歉啊。\x02\x03",

            "#1040F你……已经把我想对那孩子\x01",
            "说的话全部传达给她了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1256")

    ChrTalk(    #28
        0x107,
        (
            "#562F#4P我、我也\x01",
            "觉得姐姐说得对。\x02\x03",

            "#062F玲一直这样下去的话…\x01",
            "……我会好难过的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_1256")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A7")

    ChrTalk(    #29
        0x109,
        (
            "#1061F#4P哈哈，指引迷途的羊羔\x01",
            "回到正途，我也是双手赞成的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_12A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F9")

    ChrTalk(    #30
        0x104,
        (
            "#031F#4P呼……\x02\x03",

            "小猫咪不乖的时候，\x01",
            "偶尔也要好好调教一下哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_12F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_133B")

    ChrTalk(    #31
        0x106,
        (
            "#051F#4P算啦，反正教育小鬼\x01",
            "也是大人的职责。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_133B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1375")

    ChrTalk(    #32
        0x108,
        (
            "#070F#4P反正这也确实是\x01",
            "大人的义务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_1375")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B0")

    ChrTalk(    #33
        0x105,
        (
            "#1162F#4P我也……\x01",
            "不会在这里退缩的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_13B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13ED")

    ChrTalk(    #34
        0x103,
        (
            "#027F#4P而且，这种事也算是\x01",
            "大人的义务吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1421")

    ChrTalk(    #35
        0x10B,
        (
            "#210F#4P哼哼……\x01",
            "拿出气势来！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157E")

    label("loc_1421")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_145D")

    ChrTalk(    #36
        0x103,
        (
            "#027F#4P呵呵……\x01",
            "大家都拿出气势来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157E")

    label("loc_145D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1492")

    ChrTalk(    #37
        0x105,
        (
            "#1162F#4P要拿出……\x01",
            "气势来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157E")

    label("loc_1492")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D0")

    ChrTalk(    #38
        0x108,
        (
            "#074F#4P很好……\x01",
            "各位，都拿出干劲来吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157E")

    label("loc_14D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1504")

    ChrTalk(    #39
        0x106,
        (
            "#051F#4P嘿……\x01",
            "拿出气势来吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157E")

    label("loc_1504")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1546")

    ChrTalk(    #40
        0x104,
        (
            "#031F#4P呼呼……\x01",
            "我会用满腔的爱来温暖玲的～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157E")

    label("loc_1546")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157E")

    ChrTalk(    #41
        0x109,
        (
            "#1060F#4P嘿嘿……\x01",
            "拿出气势来战斗吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157E")


    ChrTalk(    #42
        0x101,
        "#1025F#5P大家……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 201)
    OP_70(0x0, 0xDC)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_71(0x1, 0x4)
    OP_6D(-14790, 8500, 0, 0)
    OP_67(0, -1000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(352, 0)
    SetChrPos(0x8, -20420, 0, 80, 90)
    SetChrPos(0x9, -23900, 20000, 120, 90)

    def lambda_162E():

        label("loc_162E")

        OP_7C(0x32, 0x32, 0x3E8, 0x3E8)
        OP_48()
        Jump("loc_162E")

    QueueWorkItem2(0x101, 2, lambda_162E)
    OP_24(0x113, 0x55)
    Sleep(100)
    OP_24(0x113, 0x5A)
    Sleep(100)
    OP_24(0x113, 0x5F)
    Sleep(100)
    OP_24(0x113, 0x64)
    Sleep(100)

    def lambda_166D():
        OP_8F(0xFE, 0xFFFFA3A8, 0x0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_166D)
    Sleep(500)

    def lambda_168D():
        OP_6D(-14790, 5500, 0, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_168D)

    def lambda_16A5():
        OP_67(0, 2200, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16A5)

    def lambda_16BD():
        OP_6B(1600, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16BD)
    WaitChrThread(0x9, 0x1)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 221)
    OP_70(0x0, 0xF0)
    WaitChrThread(0x9, 0x1)
    OP_23(0x113)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_44(0x101, 0x2)
    OP_7C(0x0, 0x320, 0xBB8, 0x578)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x28)
    Sleep(500)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(2000)

    def lambda_1731():
        OP_6D(-24500, 2400, 0, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1731)

    def lambda_1749():
        OP_67(0, 1980, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1749)

    def lambda_1761():
        OP_6B(2460, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1761)

    def lambda_1771():
        OP_6E(415, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1771)
    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)
    OP_0D()
    WaitChrThread(0x102, 0x0)
    Sleep(500)

    ChrTalk(    #43
        0x8,
        (
            "#1302F#5P……惹人生气……\x02\x03",

            "真是太惹人生气了……\x02\x03",

            "#1304F『帕蒂尔·玛蒂尔』！\x01",
            "解除限制吧！\x02\x03",

            "马力全开！\x01",
            "歼灭艾丝蒂尔她们！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Battle(0x463, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_4_406 end

    def Function_5_182D(): pass

    label("Function_5_182D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    Call(0, 2)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    OP_A1(0x9, 0x0)
    SetChrPos(0x9, -20000, 0, 5500, 135)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0x19)
    OP_6F(0x0, 521)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x1)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -9460, 0, -820, 270)
    SetChrPos(0x102, -9160, 0, 360, 270)
    SetChrPos(0xF8, -8020, 0, -1850, 270)
    SetChrPos(0xF9, -7600, 0, -600, 270)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0xF8, 5)
    SetChrChipByIndex(0xF9, 7)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, -18600, 0, 2700, 0)
    OP_6D(-15000, 1300, 2300, 0)
    OP_67(0, 4100, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(326000, 0)
    OP_6E(394, 0)

    def lambda_19C0():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19C0)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #44
        0x8,
        (
            "#1308F#6P为、为什么……\x02\x03",

            "为什么『帕蒂尔·玛蒂尔』会输给\x01",
            "艾丝蒂尔她们！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #45
        0x102,
        (
            "#1035F#4P极限级战略人形兵器\x01",
            "的控制系统好像还不稳定呢……\x02\x03",

            "#1043F大概是因为关节部分的负荷过重，\x01",
            "导致无法运转了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)
    Sleep(300)

    ChrTalk(    #46
        0x8,
        "#1308F#5P……怎么会………\x02",
    )

    CloseMessageWindow()

    def lambda_1AF5():
        OP_6D(-21870, 0, 8680, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1AF5)

    def lambda_1B0D():
        OP_67(0, 4720, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B0D)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x101, 0x0)
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #47
        0x8,
        (
            "#1303F#6P#3S『帕蒂尔·玛蒂尔』！！#2S\x02\x03",

            "喂！站起来啊！\x02\x03",

            "快点把艾丝蒂尔她们\x01",
            "全部杀光！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)
    Sleep(500)
    OP_22(0xF4, 0x0, 0x64)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x23)
    OP_6F(0x0, 481)
    OP_70(0x0, 0x208)
    Sleep(5200)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    Sleep(200)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(1000)

    ChrTalk(    #48
        0x8,
        "#1307F#6P……啊…………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 11)
    OP_22(0xD1, 0x0, 0x50)
    OP_99(0x8, 0x0, 0x4, 0x4B0)
    Sleep(500)
    Fade(500)
    OP_6D(-15270, 0, 3370, 0)
    OP_67(0, 3950, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(326000, 0)
    OP_6E(394, 0)
    OP_0D()

    ChrTalk(    #49
        0x8,
        "#268F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1026F#6P玲……\x02",
    )

    CloseMessageWindow()

    def lambda_1CC5():
        OP_6D(-18010, 0, 3600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1CC5)

    def lambda_1CDD():
        OP_67(0, 3800, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CDD)

    def lambda_1CF5():
        OP_6B(3050, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CF5)

    def lambda_1D05():
        OP_8F(0xFE, 0xFFFFC194, 0x0, 0x7B2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D05)
    Sleep(800)

    def lambda_1D25():
        OP_8F(0xFE, 0xFFFFC9AA, 0x0, 0x618, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D25)
    Sleep(200)

    def lambda_1D45():
        OP_8F(0xFE, 0xFFFFCBBC, 0x0, 0xFFFFFDA8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1D45)
    Sleep(200)

    def lambda_1D65():
        OP_8F(0xFE, 0xFFFFD08A, 0x0, 0x32, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1D65)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    ChrTalk(    #51
        0x8,
        (
            "#268F#5P干什么……\x02\x03",

            "是艾丝蒂尔赢了！\x01",
            "你们愿意怎样就请便……\x02\x03",

            "赶快去把终端解除，\x01",
            "继续向上层前进吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1006F#6P……那虽然也很重要，\x01",
            "但还是稍后再说吧。\x02\x03",

            "因为现在…你的事情最重要。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #53
        0x8,
        (
            "#1303F#5P什么啊…艾丝蒂尔根本就不理解玲，\x01",
            "玲的事情……你一点都不了解！\x02\x03",

            "既然这样，为什么……\x01",
            "……为什么还要管我……！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1012F#6P呵呵，那还用说吗。\x02\x03",

            "#1006F当然是因为我喜欢玲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        "#1308F#5P！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1002F#6P所以……有件事情，\x01",
            "我必须要对玲做。\x02\x03",

            "虽然很抱歉，不过我会下手轻一点的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        "#1307F#5P咦……\x02",
    )

    CloseMessageWindow()

    def lambda_1F99():
        OP_6D(-19570, 0, 4110, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F99)

    def lambda_1FB1():
        OP_6B(2630, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FB1)
    OP_8F(0x101, 0xFFFFBA78, 0x0, 0x992, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    Fade(1000)

    def lambda_1FDF():
        OP_6B(2480, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FDF)
    SetChrFlags(0x101, 0x80)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 12)

    def lambda_200D():
        OP_99(0xFE, 0x0, 0xD, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_200D)
    Sleep(500)
    OP_20(0x0)
    OP_22(0xA5, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #58
        0x8,
        (
            "#1308F#5P…………啊…………………\x02\x03",

            "#40W……………被打了…………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x76)
    Sleep(500)

    ChrTalk(    #59
        0x101,
        (
            "#1007F#6P做了坏事，\x01",
            "当然要挨打啊。\x02\x03",

            "不然的话，你就永远体会不到\x01",
            "他人的痛苦。\x02\x03",

            "#1006F我小的时候也是经常\x01",
            "被爸爸用拳头揍的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "#1309F#5P#40W艾丝蒂尔……也是一样吗……\x02\x03",

            "#40W明知道我很痛……\x01",
            "但却还是不住手……\x02\x03",

            "#40W和那些把玲……对玲做了很多坏事的人\x01",
            "……完全一样吗………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1025F#6P是不是一样，\x01",
            "玲可以自己来判断。\x02\x03",

            "怎样……你真的这么认为吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#1309F#5P#40W…………………………………\x02\x03",

            "#40W………我……不知道…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1006F#6P那么……这样又如何呢？\x02",
    )

    CloseMessageWindow()

    def lambda_2255():
        OP_6D(-19900, 0, 4500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2255)
    OP_99(0x8, 0xD, 0x13, 0x5DC)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #64
        0x8,
        "#1307F#5P………啊…………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1012F#6P什么都不用说……\x02\x03",

            "……玲只要用自己心里\x01",
            "的感觉来判断就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#1307F#5P#40W……………………………………\x02\x03",

            "#40W……脑子里乱作一团，\x01",
            "虽然搞不太清楚……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x13, 0x15, 0x3E8)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #67
        0x8,
        (
            "#1309F#5P#40W不过被这样抱着…\x01",
            "……感觉好像……也并不讨厌呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1016F#6P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#1309F#5P……………………………………\x02\x03",

            "#268F………………我要回去了………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #71
        0x8,
        (
            "#1303F#5P#3S『帕蒂尔·玛蒂尔』！#2S\x02\x03",

            "停止关节部位的制动器，\x01",
            "启动辅助引擎的控制系统！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1500)

    def lambda_249C():
        OP_6D(-22500, 500, 9860, 2500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_249C)

    def lambda_24B4():
        OP_67(0, 5300, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_24B4)

    def lambda_24CC():
        OP_6B(3600, 2500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_24CC)
    Sleep(500)
    Play3DEffect(0x3, 0x0, 0x0, "Frame86__jet_0", 0x0, 0xFFFFFE0C, 0x0, 0x3C, 0xFFA6, 0xB4, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x3, 0x1, 0x0, "Frame87__jet_1", 0x0, 0xFFFFFE0C, 0x0, 0x1E, 0x46, 0xFF4C, 0x3E8, 0x3E8, 0x3E8, 0x0)

    def lambda_254B():
        OP_8F(0xFE, 0xFFFFAFEC, 0x5DC, 0x1770, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_254B)
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 521)
    OP_70(0x0, 0x230)
    PlayEffect(0x1, 0x2, 0x9, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    OP_22(0x113, 0x0, 0x64)
    OP_22(0x114, 0x0, 0x64)
    Sleep(100)
    Fade(250)
    SetChrPos(0x101, -18000, 0, 2450, 270)
    SetChrPos(0x8, -18700, 0, 2660, 90)
    ClearChrFlags(0x101, 0x80)
    SetChrFlags(0x8, 0x1)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x40)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)

    def lambda_2610():
        OP_8F(0xFE, 0xFFFFB3A2, 0x0, 0xBE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2610)
    WaitChrThread(0x8, 0x0)
    OP_0D()
    Sleep(300)
    OP_8C(0x101, 315, 400)

    def lambda_263D():
        OP_8F(0xFE, 0xFFFFBFB4, 0x0, 0x5AA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_263D)
    OP_43(0x102, 0x1, 0x0, 0x8)
    Sleep(50)
    OP_43(0xF8, 0x1, 0x0, 0x9)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0xA)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x9, 0x1)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_B0(0x0, 0x1)
    OP_6F(0x0, 30)
    Sleep(300)
    Fade(500)
    OP_71(0x1, 0x4)
    OP_6D(-20000, 1800, 3140, 0)
    OP_67(0, 3170, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(291000, 0)
    OP_6E(598, 0)

    def lambda_26E4():
        OP_8F(0xFE, 0xFFFFAFEC, 0x0, 0x1770, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_26E4)
    WaitChrThread(0x9, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x12C)
    OP_72(0x0, 0x20)
    OP_0D()
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 461)
    OP_70(0x0, 0x1E0)
    OP_22(0x115, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_D8(0x0, 0x320)
    OP_6F(0x0, 381)
    OP_70(0x0, 0x1A4)
    Sleep(1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_2768():

        label("loc_2768")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2768")

    QueueWorkItem2(0x101, 3, lambda_2768)

    def lambda_2779():
        OP_6D(-24790, 0, 4270, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2779)

    def lambda_2791():
        OP_67(0, 5140, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2791)

    def lambda_27A9():
        OP_6B(2200, 1000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_27A9)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 2)
    OP_96(0x8, 0xFFFFAE3E, 0xE10, 0x9C4, 0x1194, 0xBB8)
    SetChrSubChip(0x8, 7)
    ClearChrFlags(0x8, 0x1)
    OP_CF(0x8, 0x0, "Frame85__ren")
    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7D(0x1, 0x8, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 315, 0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #72
        0x101,
        "#1020F#5P玲……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #73
        0x8,
        (
            "#1309F#5P我的脑子里很乱，\x01",
            "所以想一个人好好想想……\x02\x03",

            "艾丝蒂尔，你们就继续\x01",
            "向塔顶前进吧……\x02\x03",

            "莱维在等着你们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1002F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#1040F#5P……是吗。\x01",
            "谢谢你告诉我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#1307F#5P没问题吗……约修亚？\x02\x03",

            "莱维看起来可是很认真的，\x01",
            "似乎决心要阻止你们呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        (
            "#1035F#5P嗯……我明白。\x02\x03",

            "#1040F但是，我也已经\x01",
            "下了决心……\x02\x03",

            "所以，不用担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "#1307F#5P是吗……\x02\x03",

            "#268F那么，玲这就要走了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_22(0x114, 0x0, 0x64)
    OP_22(0xCC, 0x0, 0x64)
    Play3DEffect(0x2, 0x0, 0x0, "Frame86__jet_0", 0x0, 0xFFFFFD44, 0x0, 0x3C, 0xFFA6, 0xB4, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x2, 0x1, 0x0, "Frame87__jet_1", 0x0, 0xFFFFFD44, 0x0, 0x1E, 0x46, 0xFF4C, 0x3E8, 0x3E8, 0x3E8, 0x0)

    def lambda_2A53():
        OP_8F(0xFE, 0xFFFFB1E0, 0x7D0, 0x157C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2A53)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AB0")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AEE")

    label("loc_2AB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD7")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AEE")

    label("loc_2AD7")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2AEE")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B1A")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B58")

    label("loc_2B1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B41")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B58")

    label("loc_2B41")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2B58")


    def lambda_2B5E():
        OP_6D(-20260, 4500, 4520, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B5E)

    def lambda_2B76():
        OP_67(0, 3530, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B76)

    def lambda_2B8E():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2B8E)

    def lambda_2B9E():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2B9E)

    def lambda_2BAE():
        OP_6E(388, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BAE)
    Sleep(800)
    OP_D8(0x0, 0x1F4)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x5)
    OP_6F(0x0, 241)
    OP_70(0x0, 0x104)

    def lambda_2BDE():

        label("loc_2BDE")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2BDE")

    QueueWorkItem2(0x101, 3, lambda_2BDE)

    def lambda_2BEF():

        label("loc_2BEF")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2BEF")

    QueueWorkItem2(0x102, 3, lambda_2BEF)

    def lambda_2C00():

        label("loc_2C00")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2C00")

    QueueWorkItem2(0xF8, 3, lambda_2C00)

    def lambda_2C11():

        label("loc_2C11")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2C11")

    QueueWorkItem2(0xF9, 3, lambda_2C11)
    Sleep(300)

    def lambda_2C27():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2C27)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x8, 0x1)
    PlayEffect(0x1, 0x2, 0x9, 0, -1500, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x101, -13180, 0, -540, 270)
    SetChrPos(0x102, -12060, 0, 230, 270)
    SetChrPos(0xF8, -11210, 0, -1500, 270)
    SetChrPos(0xF9, -11210, 0, -1500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D58")

    ChrTalk(    #79
        0x107,
        "#065F#5P小玲！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#1020F#5P玲……等等！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "#1300F#5P……再见了。\x01",
            "艾丝蒂尔，还有提妲。\x02\x03",

            "虽然玲这就要走了……#2370W #20W \x01",
            "#1301F不过我可不许你们死哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCC")

    label("loc_2D58")


    ChrTalk(    #82
        0x101,
        "#1020F#5P玲……等等！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "#1300F#5P……再见了，艾丝蒂尔。\x02\x03",

            "虽然玲这就要走了……#2370W #20W \x01",
            "#1301F不过我可不许你们死哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCC")


    def lambda_2DD2():
        OP_6D(-20220, 7330, 11320, 4500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DD2)

    def lambda_2DEA():
        OP_67(0, 2760, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2DEA)

    def lambda_2E02():
        OP_6B(4000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2E02)

    def lambda_2E12():
        OP_6C(327000, 4500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E12)

    def lambda_2E22():
        OP_6E(362, 4500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2E22)
    PlayEffect(0x2, 0x0, 0x9, 4750, 2300, 0, 0, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x9, -4750, 2300, 0, 0, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_24(0x113, 0x5F)

    def lambda_2EA0():
        OP_8C(0xFE, 0, 50)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2EA0)

    def lambda_2EAE():
        OP_8F(0xFE, 0xFFFFB1E0, 0x1388, 0x157C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2EAE)
    Sleep(100)

    def lambda_2ECE():
        OP_8F(0xFE, 0xFFFFB1E0, 0x1388, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2ECE)
    OP_82(0x2, 0x2)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x9, 0x2)
    OP_72(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 261)
    OP_70(0x0, 0x118)
    OP_22(0x116, 0x0, 0x64)
    OP_73(0x0)
    OP_D8(0x0, 0x1F4)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 281)
    OP_70(0x0, 0x12C)
    PlayEffect(0x3, 0x2, 0x9, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x9, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x9, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x9, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x9, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0x9, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x114, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x1)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    PlayEffect(0x2, 0x2, 0x9, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x9, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x9, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x9, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x9, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0x9, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_31F9():
        OP_6D(-21400, 6800, 20800, 1800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_31F9)

    def lambda_3211():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3211)
    Sleep(300)

    def lambda_3231():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3231)
    Sleep(200)

    def lambda_3251():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3251)
    Sleep(100)

    def lambda_3271():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3271)
    Sleep(100)

    def lambda_3291():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3291)
    Sleep(100)

    def lambda_32B1():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_32B1)
    Sleep(100)

    def lambda_32D1():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0x7D00, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_32D1)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_A2(0x10FF)
    OP_A2(0x10FA)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_182D end

    def Function_6_3310(): pass

    label("Function_6_3310")


    def lambda_3316():
        OP_8F(0xFE, 0xFFFFE070, 0x0, 0xFFFFFEC0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3316)
    Sleep(120)

    def lambda_3336():
        OP_8F(0xFE, 0xFFFFE76E, 0x0, 0x276, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3336)
    Sleep(80)

    def lambda_3356():
        OP_8F(0xFE, 0xFFFFE7E6, 0x0, 0xFFFFFCCC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3356)
    Sleep(100)

    def lambda_3376():
        OP_8F(0xFE, 0xFFFFE066, 0x0, 0x3B6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3376)
    WaitChrThread(0x101, 0x0)
    Return()

    # Function_6_3310 end

    def Function_7_3391(): pass

    label("Function_7_3391")


    def lambda_3397():
        OP_8E(0xFE, 0x448E, 0x0, 0xFFFFFF24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3397)
    Sleep(40)

    def lambda_33B7():
        OP_8E(0xFE, 0x44AC, 0x0, 0x352, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_33B7)
    Sleep(100)

    def lambda_33D7():
        OP_8E(0xFE, 0x49DE, 0x0, 0x4F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_33D7)
    Sleep(50)
    OP_8E(0xF9, 0x498E, 0x0, 0xFFFFFCF4, 0xBB8, 0x0)
    Return()

    # Function_7_3391 end

    def Function_8_3406(): pass

    label("Function_8_3406")

    OP_8F(0xFE, 0xFFFFC306, 0x0, 0x83E, 0x7D0, 0x0)

    def lambda_3420():

        label("loc_3420")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3420")

    QueueWorkItem2(0xFE, 3, lambda_3420)
    Return()

    # Function_8_3406 end

    def Function_9_342C(): pass

    label("Function_9_342C")

    OP_8F(0xFE, 0xFFFFC694, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_3446():

        label("loc_3446")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3446")

    QueueWorkItem2(0xFE, 3, lambda_3446)
    Return()

    # Function_9_342C end

    def Function_10_3452(): pass

    label("Function_10_3452")

    OP_8F(0xFE, 0xFFFFCB62, 0x0, 0x3B6, 0x7D0, 0x0)

    def lambda_346C():

        label("loc_346C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_346C")

    QueueWorkItem2(0xFE, 3, lambda_346C)
    Return()

    # Function_10_3452 end

    def Function_11_3478(): pass

    label("Function_11_3478")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_348F")
    Call(0, 14)
    Call(0, 15)

    label("loc_348F")

    OP_6D(-18300, 0, 10600, 0)
    OP_67(0, 4880, -10000, 0)
    OP_6B(3710, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -17750, 0, 10660, 0)
    SetChrPos(0x102, -16059, 0, 9050, 0)
    SetChrPos(0xF8, -17240, 0, 7850, 0)
    SetChrPos(0xF9, -15710, 0, 7250, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #84
        0x101,
        (
            "#1026F#5P………………………………\x02\x03",

            "#1003F这样……没关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        (
            "#1035F#6P嗯……放心吧。\x02\x03",

            "#1040F毕竟发生了太多的事情，\x01",
            "那孩子只是头脑比较混乱吧。\x02\x03",

            "虽然要花点时间……\x01",
            "不过她终究会自己找到答案的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        "#1025F#5P是吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_363E")

    ChrTalk(    #87
        0x107,
        (
            "#067F#6P嘿嘿……\x01",
            "真希望以后能再见到她啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AB")

    label("loc_363E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3679")

    ChrTalk(    #88
        0x105,
        (
            "#1168F#6P希望……\x01",
            "今后能再遇到她啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AB")

    label("loc_3679")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36B1")

    ChrTalk(    #89
        0x103,
        (
            "#027F#6P呵呵……\x01",
            "希望能再见到她。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AB")

    label("loc_36B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36EB")

    ChrTalk(    #90
        0x104,
        (
            "#035F#6P呼……\x01",
            "我很期待能再见到她。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AB")

    label("loc_36EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3726")

    ChrTalk(    #91
        0x109,
        (
            "#1062F#6P嘿嘿……\x01",
            "很期待能再见到她。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AB")

    label("loc_3726")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3776")

    ChrTalk(    #92
        0x106,
        (
            "#051F#6P嘿嘿……走了啊，\x01",
            "希望下次见面时，她能变得温顺点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AB")

    label("loc_3776")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37AB")

    ChrTalk(    #93
        0x108,
        (
            "#070F#6P哈哈……\x01",
            "期待能再见到她。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AB")


    ChrTalk(    #94
        0x101,
        (
            "#1025F#5P嗯……是啊。\x02\x03",

            "#1012F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    Sleep(300)

    ChrTalk(    #95
        0x101,
        (
            "#1006F#5P……那么……\x01",
            "得转换一下心情。\x02\x03",

            "停止掉终端，然后继续前进吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        "#1043F#6P嗯……是啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #97
        0x101,
        (
            "#1026F#5P啊，对了……\x02\x03",

            "#1002F她说莱维\x01",
            "在塔顶等着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x102,
        "#1043F#6P嗯……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(500)

    ChrTalk(    #99
        0x102,
        (
            "#1035F#6P执行者Ｎｏ．Ⅱ。\x01",
            "『剑帝』莱恩哈特。\x02\x03",

            "战斗力在『执行者』之中\x01",
            "也是数一数二的。\x02\x03",

            "#1042F做好万全的准备向塔顶前进吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1002F#5P……明白！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3982")
    OP_A2(0x2240)

    label("loc_3982")

    OP_A2(0x223A)
    OP_28(0x9F, 0x1, 0x400)
    OP_28(0x9F, 0x1, 0x800)
    OP_20(0x3E8)
    EventEnd(0x0)
    OP_1D(0x40)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_3478 end

    def Function_12_39A4(): pass

    label("Function_12_39A4")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #101
        (
            "\x07\x05解除通向上层区域的隔离壁，\x01",
            "以及传送门的锁定。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5306   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_12_39A4 end

    def Function_13_3A0E(): pass

    label("Function_13_3A0E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A25")
    Call(0, 14)
    Call(0, 15)

    label("loc_3A25")

    OP_6D(-33350, 0, 660, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(3430, 0)
    OP_6C(302000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -31400, 0, -720, 270)
    SetChrPos(0x102, -31400, 0, 210, 270)
    SetChrPos(0xF8, -29800, 0, -1260, 270)
    SetChrPos(0xF9, -29800, 0, 10, 270)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #102
        (
            "\x07\x05通往上层区域的隔离壁，\x01",
            "以及传送门的锁定已经解除了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_71(0x2, 0x4)
    OP_0D()
    Sleep(500)
    OP_64(0x0, 0x1)
    OP_A2(0x223B)
    OP_28(0x9F, 0x1, 0x1000)
    EventEnd(0x0)
    Return()

    # Function_13_3A0E end

    def Function_14_3B23(): pass

    label("Function_14_3B23")

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
        (0, "loc_3B9D"),
        (1, "loc_3BA3"),
        (SWITCH_DEFAULT, "loc_3BA9"),
    )


    label("loc_3B9D")

    OP_A2(0x1200)
    Jump("loc_3BA9")

    label("loc_3BA3")

    OP_A2(0x1201)
    Jump("loc_3BA9")

    label("loc_3BA9")

    Return()

    # Function_14_3B23 end

    def Function_15_3BAA(): pass

    label("Function_15_3BAA")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
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

    # Function_15_3BAA end

    SaveToFile()

Try(main)
