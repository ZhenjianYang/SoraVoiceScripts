from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3132   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3132_1 ._SN',
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
        '玛尔奇娜主管',                         # 9
        '艾玛',                                 # 10
        '诺蒂亚',                               # 11
        '多杰',                                 # 12
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
        'ED6_DT07/CH01210 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01210 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01210P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01210P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
    )

    DeclNpc(
        X                   = -1700,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 192,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 36440,
        Z                   = 0,
        Y                   = 50580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 68210,
        Z                   = 0,
        Y                   = 92140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 68100,
        Z                   = 0,
        Y                   = 56310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclActor(
        TriggerX            = -1290,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = -1700,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4000,
        TriggerZ            = 0,
        TriggerY            = 4000,
        TriggerRange        = 800,
        ActorX              = -4000,
        ActorZ              = 1000,
        ActorY              = 4000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_192",          # 00, 0
        "Function_1_204",          # 01, 1
        "Function_2_205",          # 02, 2
        "Function_3_229",          # 03, 3
        "Function_4_22E",          # 04, 4
        "Function_5_A45",          # 05, 5
        "Function_6_F92",          # 06, 6
        "Function_7_1154",         # 07, 7
        "Function_8_1378",         # 08, 8
    )


    def Function_0_192(): pass

    label("Function_0_192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C3")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1B9")
    SetChrPos(0x9, 33350, 0, 55500, 0)
    Jump("loc_1C0")

    label("loc_1B9")

    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_1C0")

    Jump("loc_203")

    label("loc_1C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1DE")
    SetChrPos(0x9, 5590, 0, 134800, 348)
    Jump("loc_203")

    label("loc_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1ED")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_203")

    label("loc_1ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1F7")
    Jump("loc_203")

    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_203")
    ClearChrFlags(0xA, 0x80)

    label("loc_203")

    Return()

    # Function_0_192 end

    def Function_1_204(): pass

    label("Function_1_204")

    Return()

    # Function_1_204 end

    def Function_2_205(): pass

    label("Function_2_205")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_228")
    OP_8D(0xFE, 33380, 54030, 36670, 49190, 2000)
    Jump("Function_2_205")

    label("loc_228")

    Return()

    # Function_2_205 end

    def Function_3_229(): pass

    label("Function_3_229")

    Call(0, 4)
    Return()

    # Function_3_229 end

    def Function_4_22E(): pass

    label("Function_4_22E")

    TalkBegin(0x8)
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24B")
    OP_A9(0x99)
    TalkEnd(0x8)
    Return()

    label("loc_24B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25C")
    TalkEnd(0x8)
    Return()

    label("loc_25C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_288")
    Call(1, 1)
    Jump("loc_28C")

    label("loc_288")

    Call(1, 0)

    label("loc_28C")

    Jump("loc_A41")

    label("loc_28F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2E7")

    ChrTalk(    #0
        0x8,
        (
            "现在这种情况，\x01",
            "客人也越来越少……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "到定期船恢复之前\x01",
            "只能先忍耐了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A41")

    label("loc_2E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_424")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_376")

    ChrTalk(    #2
        0x8,
        (
            "啊，各位游击士。\x01",
            "好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "蔡恩拉德酒店\x01",
            "还像平常一样正常营业哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "虽然有些不便之处，\x01",
            "请多担待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CF")

    label("loc_376")


    ChrTalk(    #5
        0x8,
        (
            "欢迎光临。\x01",
            "蔡恩拉德酒店\x01",
            "还像平常一样正常营业哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "虽然有些不便之处，\x01",
            "请多担待。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CF")

    OP_A2(0x0)
    Jump("loc_421")

    label("loc_3D5")


    ChrTalk(    #7
        0x8,
        (
            "蔡恩拉德酒店\x01",
            "还像平常一样正常营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "虽然有些不便之处，\x01",
            "请多担待。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_421")

    Jump("loc_A41")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_775")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_708")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_692")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 3)), scpexpr(EXPR_END)), "loc_622")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_504")

    ChrTalk(    #9
        0x8,
        (
            "艾玛听到地震不会再来的消息之后\x01",
            "恢复得和以前一样活泼了，可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "像她那个样子…\x01",
            "实在是活泼过头了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "呼～不是精力过剩就是缩成一团，\x01",
            "就不能正常一点吗…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C0")

    label("loc_504")


    ChrTalk(    #12
        0x8,
        (
            "中央工房发表过安全宣言了，\x01",
            "说是地震已经不会再出现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "多亏如此，我们的艾玛也\x01",
            "恢复得和以前一样活泼了，可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "像她那个样子…\x01",
            "实在是活泼过头了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        "呼～真是担心死了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5C0")

    Jump("loc_61F")

    label("loc_5C3")


    ChrTalk(    #16
        0x8,
        (
            "大家辛苦了，\x01",
            "吉米刚才已经回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "他回来就一副急急忙忙的样子，\x01",
            "马上就退房离开了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61F")

    Jump("loc_68F")

    label("loc_622")


    ChrTalk(    #18
        0x8,
        (
            "啊，各位。\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "刚才吉米已经\x01",
            "平安回来了呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "呼～胸中的一块大石头\x01",
            "总算是落地了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1643)
    OP_A2(0x1)

    label("loc_68F")

    Jump("loc_705")

    label("loc_692")


    ChrTalk(    #21
        0x8,
        (
            "行踪不明的客人\x01",
            "好像是去了钟乳洞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "我们虽然努力\x01",
            "劝阻过他了，可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "那么，那位客人的事\x01",
            "就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_705")

    Jump("loc_772")

    label("loc_708")


    ChrTalk(    #24
        0x8,
        (
            "地震的安全宣言放出了，\x01",
            "本来是值得高兴的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "但还有一件事情\x01",
            "让我很担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "呼，怎么办呢。\x02",
    )

    CloseMessageWindow()

    label("loc_772")

    Jump("loc_A41")

    label("loc_775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_869")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7DC")

    ChrTalk(    #27
        0x8,
        (
            "店员艾玛\x01",
            "还在害怕地震会再来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "看她那种魂不守舍的模样，\x01",
            "还真是让人担心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_866")

    label("loc_7DC")


    ChrTalk(    #29
        0x8,
        (
            "店员艾玛\x01",
            "还在担心地震再来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "不过她平时活泼过头了，\x01",
            "现在这样反而更好吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "看她那种魂不守舍的模样，\x01",
            "还真是让人担心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_866")

    Jump("loc_A41")

    label("loc_869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_95A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8DC")

    ChrTalk(    #32
        0x8,
        (
            "别看艾玛现在很乖巧，\x01",
            "但平时的她可不是这个样子的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "之前总是一副大嗓门，\x01",
            "经常把客人吓到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_957")

    label("loc_8DC")


    ChrTalk(    #34
        0x8,
        (
            "这次地震\x01",
            "让店员艾玛\x01",
            "变得有些没精神了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "不过也许她现在这个样子\x01",
            "反而更好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "平时的她实在是\x01",
            "活泼得过头了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_957")

    Jump("loc_A41")

    label("loc_95A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_A41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9B5")

    ChrTalk(    #37
        0x8,
        (
            "这家酒店的抗震性\x01",
            "是没问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "中央工房也给我们\x01",
            "颁布了合格证书。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A41")

    label("loc_9B5")


    ChrTalk(    #39
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎光临蔡恩拉德酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "虽然被地震吓了一大跳，\x01",
            "不过还真是好久没遇到了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "地震并没造成什么重大影响，\x01",
            "请放心吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A41")

    TalkEnd(0x8)
    Return()

    # Function_4_22E end

    def Function_5_A45(): pass

    label("Function_5_A45")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_B17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACC")

    ChrTalk(    #42
        0xFE,
        (
            "油灯这种东西\x01",
            "还真是麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "不经常清洁的话\x01",
            "墙壁就会被弄得污黑……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "呼～果然还是导力灯\x01",
            "最便利啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_B14")

    label("loc_ACC")


    ChrTalk(    #45
        0xFE,
        (
            "这油灯才用了没几天\x01",
            "就搞得这么脏……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "果然还是导力灯\x01",
            "最便利啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B14")

    Jump("loc_F8E")

    label("loc_B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB7")

    ChrTalk(    #47
        0xFE,
        (
            "现在导力灯没法使用了，\x01",
            "只能点油灯应急……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "但还是好暗，\x01",
            "到了晚上真是好可怕呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "有时候还会和客人撞到一起，\x01",
            "都快吓出心脏病了～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_BFF")

    label("loc_BB7")


    ChrTalk(    #50
        0xFE,
        (
            "油灯的光实在是\x01",
            "太昏暗了啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "夜、夜里来到走廊时\x01",
            "真是好害怕啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFF")

    Jump("loc_F8E")

    label("loc_C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_C4B")

    ChrTalk(    #52
        0xFE,
        "好了～先来做扫除吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "今天也要鼓足干劲才行～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D00")

    label("loc_C4B")


    ChrTalk(    #54
        0xFE,
        (
            "欢迎光临！\x01",
            "欢迎光临蔡恩拉德酒店！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "嘿嘿嘿！！听说了吗！？\x01",
            "已经不会发生地震了啊！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "是客人告诉我\x01",
            "这件超级好消息的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "哈哈哈！这样的话，\x01",
            "我艾玛就彻底复活了！！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_D00")

    Jump("loc_F8E")

    label("loc_D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_DEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D66")

    ChrTalk(    #58
        0xFE,
        (
            "啊～一想起地震的事\x01",
            "就连食欲也没有了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "大概以后\x01",
            "会发展成失眠也说不定啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEB")

    label("loc_D66")


    ChrTalk(    #60
        0xFE,
        "啊，欢迎光临……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "啊～一想起地震的事\x01",
            "就连食欲也没有了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "大概以后\x01",
            "会发展成失眠也说不定啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "啊、啊哈哈哈～～……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_DEB")

    Jump("loc_F8E")

    label("loc_DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_ED6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E59")

    ChrTalk(    #64
        0xFE,
        (
            "老想着会不会再有地震，\x01",
            "都没办法投入工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "但不知为什么主管\x01",
            "就可以那么轻松……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED3")

    label("loc_E59")


    ChrTalk(    #66
        0xFE,
        (
            "啊，客人……\x01",
            "欢迎光临～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "老想着会不会再有地震，\x01",
            "都没办法投入工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "但不知为什么主管\x01",
            "就可以那么轻松……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_ED3")

    Jump("loc_F8E")

    label("loc_ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_F8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F33")

    ChrTalk(    #69
        0xFE,
        (
            "要、要是再有地震\x01",
            "的话该怎么办啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "呜呜～害怕得我\x01",
            "都没办法工作了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F8E")

    label("loc_F33")


    ChrTalk(    #71
        0xFE,
        "欢、欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "呜呜～总觉得地面\x01",
            "还在摇晃呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "好可怕啊～\x01",
            "都没办法工作了～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_F8E")

    TalkEnd(0x9)
    Return()

    # Function_5_A45 end

    def Function_6_F92(): pass

    label("Function_6_F92")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1054")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_FFE")

    ChrTalk(    #74
        0xFE,
        (
            "中央工房的报道\x01",
            "大家都很感兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "好～在坐上回航的船之前\x01",
            "先把稿子整理一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1051")

    label("loc_FFE")


    ChrTalk(    #76
        0xFE,
        (
            "中央工房的报道\x01",
            "大家都很感兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "不愧是有着王国的大脑\x01",
            "之称的地方啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1051")

    Jump("loc_1150")

    label("loc_1054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_1150")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10CD")

    ChrTalk(    #78
        0xFE,
        (
            "身为利贝尔通讯的记者，\x01",
            "绝对不能错过地震的报道啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "有关新型导力照相机\x01",
            "想听听专业人士的意见吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1150")

    label("loc_10CD")


    ChrTalk(    #80
        0xFE,
        "呼～地震还真是少见呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "身为利贝尔通讯的记者，\x01",
            "这种新闻当然不能错过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "有关新型导力照相机\x01",
            "想听听专业人士的意见吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1150")

    TalkEnd(0xA)
    Return()

    # Function_6_F92 end

    def Function_7_1154(): pass

    label("Function_7_1154")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_124E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EB")

    ChrTalk(    #83
        0xFE,
        (
            "导力器瘫痪的原因\x01",
            "好像还不清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "中央工房现在已经是那种状态了，\x01",
            "肯定不可能再进行研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "想想也知道\x01",
            "事态有多严重。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_124B")

    label("loc_11EB")


    ChrTalk(    #86
        0xFE,
        (
            "导力器瘫痪的原因\x01",
            "好像还不清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "中央工房现在已经是那种状态了，\x01",
            "肯定不可能再进行研究。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124B")

    Jump("loc_1374")

    label("loc_124E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1374")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1302")

    ChrTalk(    #88
        0xFE,
        (
            "我从共和国特意赶来，就是为了\x01",
            "购买新型导力器，可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "为、为什么城里所有的导力器\x01",
            "都瘫痪了呢！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "中央工房也是一团漆黑，\x01",
            "想进行商谈似乎很困难了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1374")

    label("loc_1302")


    ChrTalk(    #91
        0xFE,
        (
            "我从共和国特意赶来，就是为了\x01",
            "购买新型导力器，可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "照现在的形势来看的话，\x01",
            "这次的商讨算是彻底泡汤了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1374")

    TalkEnd(0xFE)
    Return()

    # Function_7_1154 end

    def Function_8_1378(): pass

    label("Function_8_1378")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #93
        (
            "\x07\x05　　　　　　　工作人员室　　　　　　　\x01",
            "        ※无关人员请勿入内\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1378 end

    SaveToFile()

Try(main)
