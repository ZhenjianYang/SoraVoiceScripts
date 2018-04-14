from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3401   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60125",
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
        ' ',                                    # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH12110 ._CH',             # 00
        'ED6_DT29/CH12111 ._CH',             # 01
        'ED6_DT29/CH12410 ._CH',             # 02
        'ED6_DT29/CH12411 ._CH',             # 03
        'ED6_DT29/CH12250 ._CH',             # 04
        'ED6_DT29/CH12251 ._CH',             # 05
        'ED6_DT29/CH12130 ._CH',             # 06
        'ED6_DT29/CH12131 ._CH',             # 07
        'ED6_DT09/CH10130 ._CH',             # 08
        'ED6_DT09/CH10131 ._CH',             # 09
        'ED6_DT09/CH10750 ._CH',             # 0A
        'ED6_DT09/CH10751 ._CH',             # 0B
        'ED6_DT29/CH12270 ._CH',             # 0C
        'ED6_DT29/CH12271 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12110P._CP',             # 00
        'ED6_DT29/CH12111P._CP',             # 01
        'ED6_DT29/CH12410P._CP',             # 02
        'ED6_DT29/CH12411P._CP',             # 03
        'ED6_DT29/CH12250P._CP',             # 04
        'ED6_DT29/CH12251P._CP',             # 05
        'ED6_DT29/CH12130P._CP',             # 06
        'ED6_DT29/CH12131P._CP',             # 07
        'ED6_DT09/CH10130P._CP',             # 08
        'ED6_DT09/CH10131P._CP',             # 09
        'ED6_DT09/CH10750P._CP',             # 0A
        'ED6_DT09/CH10751P._CP',             # 0B
        'ED6_DT29/CH12270P._CP',             # 0C
        'ED6_DT29/CH12271P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x49,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 860,
        Z                   = 0,
        Y                   = -80,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12680,
        Z                   = 0,
        Y                   = -5390,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7430,
        Z                   = 0,
        Y                   = 43660,
        Unknown_0C          = 225,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13610,
        Z                   = 0,
        Y                   = -45610,
        Unknown_0C          = 270,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -23680,
        Y                   = 0,
        Z                   = 5150,
        Range               = -17980,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x48A8,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 18480,
        TriggerZ            = 0,
        TriggerY            = 53330,
        TriggerRange        = 1000,
        ActorX              = 18980,
        ActorZ              = 0,
        ActorY              = 53830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12930,
        TriggerZ            = 0,
        TriggerY            = -51920,
        TriggerRange        = 1000,
        ActorX              = 12930,
        ActorZ              = 0,
        ActorY              = -52630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_212",          # 00, 0
        "Function_1_213",          # 01, 1
        "Function_2_3AF",          # 02, 2
        "Function_3_4C6",          # 03, 3
        "Function_4_5DD",          # 04, 4
        "Function_5_980",          # 05, 5
        "Function_6_A19",          # 06, 6
        "Function_7_A7F",          # 07, 7
        "Function_8_B4E",          # 08, 8
        "Function_9_BA0",          # 09, 9
    )


    def Function_0_212(): pass

    label("Function_0_212")

    Return()

    # Function_0_212 end

    def Function_1_213(): pass

    label("Function_1_213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_225")
    OP_6F(0x0, 0)
    Jump("loc_22C")

    label("loc_225")

    OP_6F(0x0, 60)

    label("loc_22C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E")
    OP_6F(0x1, 0)
    Jump("loc_245")

    label("loc_23E")

    OP_6F(0x1, 60)

    label("loc_245")

    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_384")
    LoadEffect(0x0, "map\\\\mpsteam0.eff")
    PlayEffect(0x0, 0x0, 0xFF, -12310, -650, 9080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, -5900, -650, 7400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, -7590, -650, -1210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFF, -8800, -650, -3670, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0xFF, -12860, -650, -40, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3A2")
    OP_82(0x80, 0x2)
    OP_82(0x81, 0x2)
    OP_82(0x82, 0x2)
    OP_82(0x83, 0x2)
    OP_82(0x84, 0x2)
    OP_22(0x1C7, 0x0, 0x64)
    Jump("loc_3AE")

    label("loc_3A2")

    OP_43(0x8, 0x0, 0x0, 0x7)
    OP_22(0x10B, 0x0, 0x64)

    label("loc_3AE")

    Return()

    # Function_1_213 end

    def Function_2_3AF(): pass

    label("Function_2_3AF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_487")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_41E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1560)
    Jump("loc_484")

    label("loc_41E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_484")

    Jump("loc_4B8")

    label("loc_487")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4B8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3AF end

    def Function_3_4C6(): pass

    label("Function_3_4C6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_535")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1561)
    Jump("loc_59B")

    label("loc_535")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_59B")

    Jump("loc_5CF")

    label("loc_59E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5CF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4C6 end

    def Function_4_5DD(): pass

    label("Function_4_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 3)), scpexpr(EXPR_END)), "loc_5E5")
    Return()

    label("loc_5E5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_605")
    Call(0, 5)
    Call(0, 6)
    FadeToBright(0, 0)

    label("loc_605")

    Fade(1000)
    OP_6D(2350, 0, -14430, 0)
    OP_67(0, 3840, -10000, 0)
    OP_6B(3740, 0)
    OP_6C(150000, 0)
    OP_6E(328, 0)
    OP_43(0x8, 0x3, 0x0, 0x9)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x8D, 0x1, 0x6E)
    OP_0D()
    SetChrPos(0x101, -19860, 0, 6880, 90)
    SetChrPos(0x107, -21170, 0, 7130, 90)
    SetChrPos(0xF7, -19760, 0, 8160, 90)
    SetChrPos(0xF9, -21470, 0, 8690, 90)
    OP_C8(0x200, 0x46, "C_PLAC11._CH", 0x0, 0x3E8)
    Sleep(1000)

    def lambda_6EF():
        OP_6D(-18400, -30, 6270, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6EF)

    def lambda_707():
        OP_67(0, 5570, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_707)

    def lambda_71F():
        OP_6B(3840, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_71F)

    def lambda_72F():
        OP_6C(138000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_72F)

    def lambda_73F():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_73F)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #6
        0x101,
        (
            "#1020F#2P呜哇……\x01",
            "沸腾得很厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x107,
        (
            "#065F#4P啊哇哇，要是掉下去\x01",
            "一定会被烫伤的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81B")

    ChrTalk(    #8
        0x104,
        (
            "#032F#4P沸腾的热水自不必说……\x01",
            "还要留意那些高热的蒸气。\x02\x03",

            "一不小心的话\x01",
            "可不是烫伤那么简单哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87F")

    label("loc_81B")


    ChrTalk(    #9
        0x105,
        (
            "#042F#4P沸腾的热水自不必说……\x01",
            "高热的蒸气看起来也很危险。\x02\x03",

            "一不小心的话\x01",
            "可不是烫伤那么简单了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8F0")

    ChrTalk(    #10
        0x106,
        (
            "#053F#6P啊啊……正确。\x02\x03",

            "#050F看起来是每隔一定时间\x01",
            "就会喷出来的样子啊。\x02\x03",

            "只能算准时机\x01",
            "穿越过去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95B")

    label("loc_8F0")


    ChrTalk(    #11
        0x103,
        (
            "#026F#6P嗯嗯……说得没错。\x02\x03",

            "#022F看起来是每隔一定时间\x01",
            "就会喷出来的样子呢。\x02\x03",

            "只能算准时机\x01",
            "穿越过去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95B")


    ChrTalk(    #12
        0x101,
        "#1002F#2P嗯，ＯＫ！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1423)
    OP_28(0x88, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_4_5DD end

    def Function_5_980(): pass

    label("Function_5_980")

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
        (0, "loc_9FA"),
        (1, "loc_A00"),
        (SWITCH_DEFAULT, "loc_A06"),
    )


    label("loc_9FA")

    OP_A2(0x1200)
    Jump("loc_A06")

    label("loc_A00")

    OP_A2(0x1201)
    Jump("loc_A06")

    label("loc_A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A14")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_A18")

    label("loc_A14")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_A18")

    Return()

    # Function_5_980 end

    def Function_6_A19(): pass

    label("Function_6_A19")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A53")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_A6D")

    label("loc_A53")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_A6D")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_6_A19 end

    def Function_7_A7F(): pass

    label("Function_7_A7F")

    Call(0, 8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 3)), scpexpr(EXPR_END)), "loc_AD1")
    OP_43(0x8, 0x3, 0x0, 0x9)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x8D, 0x1, 0x6E)
    Call(0, 8)

    label("loc_AD1")

    PlayEffect(0x8E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x8E, 0x1, 0x6E)
    Call(0, 8)
    PlayEffect(0x8F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x8F, 0x1, 0x6E)
    Return()

    # Function_7_A7F end

    def Function_8_B4E(): pass

    label("Function_8_B4E")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_B6F"),
        (1, "loc_B77"),
        (2, "loc_B7F"),
        (3, "loc_B87"),
        (4, "loc_B8F"),
        (SWITCH_DEFAULT, "loc_B97"),
    )


    label("loc_B6F")

    Sleep(500)
    Jump("loc_B9F")

    label("loc_B77")

    Sleep(1000)
    Jump("loc_B9F")

    label("loc_B7F")

    Sleep(1500)
    Jump("loc_B9F")

    label("loc_B87")

    Sleep(2000)
    Jump("loc_B9F")

    label("loc_B8F")

    Sleep(2500)
    Jump("loc_B9F")

    label("loc_B97")

    Sleep(3000)
    Jump("loc_B9F")

    label("loc_B9F")

    Return()

    # Function_8_B4E end

    def Function_9_BA0(): pass

    label("Function_9_BA0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB6")
    OP_22(0x10D, 0x0, 0x64)
    Sleep(7000)
    Jump("Function_9_BA0")

    label("loc_BB6")

    Return()

    # Function_9_BA0 end

    SaveToFile()

Try(main)
