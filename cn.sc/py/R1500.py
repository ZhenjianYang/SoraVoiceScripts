from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R1500   ._SN',
        MapName             = 'Bose',
        Location            = 'R1500.x',
        MapIndex            = 59,
        MapDefaultBGM       = "ed60022",
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
        '拉文努村',                             # 9
        '西柏斯街道方向',                       # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
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
        'ED6_DT09/CH10030 ._CH',             # 00
        'ED6_DT09/CH10031 ._CH',             # 01
        'ED6_DT09/CH10860 ._CH',             # 02
        'ED6_DT09/CH10861 ._CH',             # 03
        'ED6_DT09/CH10310 ._CH',             # 04
        'ED6_DT09/CH10311 ._CH',             # 05
        'ED6_DT09/CH10330 ._CH',             # 06
        'ED6_DT09/CH10331 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10030P._CP',             # 00
        'ED6_DT09/CH10031P._CP',             # 01
        'ED6_DT09/CH10860P._CP',             # 02
        'ED6_DT09/CH10861P._CP',             # 03
        'ED6_DT09/CH10310P._CP',             # 04
        'ED6_DT09/CH10311P._CP',             # 05
        'ED6_DT09/CH10330P._CP',             # 06
        'ED6_DT09/CH10331P._CP',             # 07
    )

    DeclNpc(
        X                   = -170710,
        Z                   = 12010,
        Y                   = 95390,
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
        X                   = -204960,
        Z                   = -100,
        Y                   = -46530,
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
        X                   = -191470,
        Z                   = 3990,
        Y                   = 18830,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -180300,
        Z                   = 3990,
        Y                   = -3330,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -166330,
        Z                   = 11950,
        Y                   = 8590,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x130,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -206780,
        Z                   = 1860,
        Y                   = -1570,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -158080,
        Z                   = 10080,
        Y                   = -4750,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -191900,
        TriggerZ            = 3950,
        TriggerY            = 23540,
        TriggerRange        = 1000,
        ActorX              = -191900,
        ActorZ              = 3950,
        ActorY              = 24150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -146910,
        TriggerZ            = 7980,
        TriggerY            = 11710,
        TriggerRange        = 1000,
        ActorX              = -146830,
        ActorZ              = 7980,
        ActorY              = 12540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1FE",          # 00, 0
        "Function_1_228",          # 01, 1
        "Function_2_284",          # 02, 2
        "Function_3_285",          # 03, 3
        "Function_4_39C",          # 04, 4
        "Function_5_96F",          # 05, 5
    )


    def Function_0_1FE(): pass

    label("Function_0_1FE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_20A"),
        (SWITCH_DEFAULT, "loc_227"),
    )


    label("loc_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_224")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_224")

    Jump("loc_227")

    label("loc_227")

    Return()

    # Function_0_1FE end

    def Function_1_228(): pass

    label("Function_1_228")

    OP_16(0x2, 0xFA0, 0xFFFB6C20, 0xFFFE6DA8, 0x23001F)
    ClearMapFlags(0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x364, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_251")
    OP_6F(0x1, 0)
    Jump("loc_258")

    label("loc_251")

    OP_6F(0x1, 60)

    label("loc_258")

    OP_64(0x0, 0x1)
    OP_71(0x0, 0x0)
    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_276")
    OP_10(0x1, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_283")

    label("loc_276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_283")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)

    label("loc_283")

    Return()

    # Function_1_228 end

    def Function_2_284(): pass

    label("Function_2_284")

    Return()

    # Function_2_284 end

    def Function_3_285(): pass

    label("Function_3_285")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x364, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_2F4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B21)
    Jump("loc_35A")

    label("loc_2F4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x00\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_35A")

    Jump("loc_38E")

    label("loc_35D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_38E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_285 end

    def Function_4_39C(): pass

    label("Function_4_39C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B9")
    Call(0, 5)

    label("loc_3B9")

    OP_6D(-204280, -140, -31340, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -205400, -50, -35380, 0)
    SetChrPos(0xF8, -206050, -50, -36380, 0)
    SetChrPos(0xF9, -204840, -50, -36370, 0)
    SetChrPos(0x106, -205400, -50, -37370, 0)

    def lambda_440():
        OP_8E(0xFE, 0xFFFCDFE2, 0x14, 0xFFFF9278, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_440)
    Sleep(100)

    def lambda_460():
        OP_8E(0xFE, 0xFFFCDDBC, 0xFFFFFF56, 0xFFFF8B34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_460)
    Sleep(100)

    def lambda_480():
        OP_8E(0xFE, 0xFFFCE2EE, 0xFFFFFF9C, 0xFFFF8A94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_480)
    Sleep(100)

    def lambda_4A0():
        OP_8E(0xFE, 0xFFFCE0AA, 0xFFFFFF6A, 0xFFFF8076, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4A0)
    FadeToBright(2000, 0)
    WaitChrThread(0x106, 0x1)

    ChrTalk(    #3
        0x106,
        (
            "#555F#2P喂……\x01",
            "那边是拉文努村。\x02\x03",

            "我说过了，等手边的工作\x01",
            "告一段落后再过去吧。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    def lambda_520():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_520)
    Sleep(50)

    def lambda_533():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_533)
    Sleep(50)
    OP_8C(0xF9, 180, 400)

    ChrTalk(    #4
        0x101,
        (
            "#1008F啊哈哈……\x01",
            "说来也是。\x02\x03",

            "#1016F但是，既然来到这边\x01",
            "顺便绕个路也……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_771")
    OP_8C(0x107, 0, 400)

    ChrTalk(    #5
        0x107,
        (
            "#065F#2P姐、姐姐……\x01",
            "不可以勉强人家啦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1006F但是，提妲\x01",
            "也想过去看看吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x107,
        "#562F#2P虽、虽然是没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x106,
        (
            "#055F#2P啊～少说废话了。\x01",
            "赶快回去！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 180, 500)

    def lambda_652():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_652)

    def lambda_660():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_660)
    OP_8E(0x106, 0xFFFCDEDE, 0xFFFFFFCE, 0xFFFF5574, 0xBB8, 0x0)

    ChrTalk(    #9
        0x101,
        (
            "#1007F嗯……\x01",
            "好像很可疑呢～\x02\x03",

            "#1019F那么不想向我们\x01",
            "介绍你妹妹吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x107,
        (
            "#063F#5P…………………………\x02\x03",

            "难不成我……\x01",
            "误解了什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1004F咦……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #12
        0x107,
        (
            "#067F#2P不……没什么。\x02\x03",

            "#560F好了，姐姐。\x01",
            "去追阿加特哥哥吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_958")

    label("loc_771")


    ChrTalk(    #13
        0x106,
        (
            "#055F啊～少说废话了。\x01",
            "赶快回去！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 180, 500)
    OP_8E(0x106, 0xFFFCDEDE, 0xFFFFFFCE, 0xFFFF5574, 0xBB8, 0x0)

    ChrTalk(    #14
        0x101,
        (
            "#1007F嗯……\x01",
            "好像很可疑呢～\x02\x03",

            "#1019F那么不想向我们\x01",
            "介绍你妹妹吗。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84E")

    ChrTalk(    #15
        0x103,
        (
            "#524F嗯……\x01",
            "说不定有很多隐情呢。\x02\x03",

            "总之，现在还是\x01",
            "听阿加特的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_958")

    label("loc_84E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AB")

    ChrTalk(    #16
        0x104,
        (
            "#030F嗯……\x01",
            "说不定有很多隐情呢。\x02\x03",

            "#031F总之，现在还是\x01",
            "听阿加特兄的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_958")

    label("loc_8AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FD")

    ChrTalk(    #17
        0x108,
        (
            "#074F嗯……\x01",
            "总之，有很多的隐情吧。\x02\x03",

            "#070F现在还是听他的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_958")

    label("loc_8FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_958")

    ChrTalk(    #18
        0x105,
        (
            "#047F说不定是一言难尽呢。\x02\x03",

            "#040F我想现在还是先听\x01",
            "阿加特先生的话比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_958")

    FadeToBright(1500, 0)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R1201   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_4_39C end

    def Function_5_96F(): pass

    label("Function_5_96F")

    FadeToDark(0, 0, -1)
    OP_6D(97010, 0, 95840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
        (0, "loc_A26"),
        (1, "loc_A2C"),
        (SWITCH_DEFAULT, "loc_A32"),
    )


    label("loc_A26")

    OP_A2(0x1200)
    Jump("loc_A32")

    label("loc_A2C")

    OP_A2(0x1201)
    Jump("loc_A32")

    label("loc_A32")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_5_96F end

    SaveToFile()

Try(main)
