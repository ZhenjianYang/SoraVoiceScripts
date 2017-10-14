from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        TriggerX            = 19000,
        TriggerZ            = 0,
        TriggerY            = 52800,
        TriggerRange        = 1000,
        ActorX              = 19000,
        ActorZ              = 1000,
        ActorY              = 52800,
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
        ActorX              = 13390,
        ActorZ              = 0,
        ActorY              = -53090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_212",          # 00, 0
        "Function_1_213",          # 01, 1
        "Function_2_3AF",          # 02, 2
        "Function_3_511",          # 03, 3
        "Function_4_63C",          # 04, 4
        "Function_5_AEC",          # 05, 5
        "Function_6_B84",          # 06, 6
        "Function_7_BEA",          # 07, 7
        "Function_8_CB9",          # 08, 8
        "Function_9_D0B",          # 09, 9
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

    OP_EA(0x2, 0xBE, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_487")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_420")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1560)
    Jump("loc_484")

    label("loc_420")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_484")

    Jump("loc_503")

    label("loc_487")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05We're sorry; the item fairies haven't restocked\x01",
            "this chest yet. Please come visit again soon.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_503")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3AF end

    def Function_3_511(): pass

    label("Function_3_511")

    OP_EA(0x2, 0xBF, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_582")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1561)
    Jump("loc_5E6")

    label("loc_582")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_5E6")

    Jump("loc_62E")

    label("loc_5E9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05There was an item here. It's gone now.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_62E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_511 end

    def Function_4_63C(): pass

    label("Function_4_63C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 3)), scpexpr(EXPR_END)), "loc_644")
    Return()

    label("loc_644")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_664")
    Call(0, 5)
    Call(0, 6)
    FadeToBright(0, 0)

    label("loc_664")

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
    OP_DE("Hot Springs Fountainhead")
    Sleep(1000)

    def lambda_768():
        OP_6D(-18400, -30, 6270, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_768)

    def lambda_780():
        OP_67(0, 5570, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_780)

    def lambda_798():
        OP_6B(3840, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_798)

    def lambda_7A8():
        OP_6C(138000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7A8)

    def lambda_7B8():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_7B8)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #6
        0x101,
        "#1020F#4PWowza, it's really boiling in here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x107,
        (
            "#065F#2PIf you fell in there, the burns\x01",
            "could kill you! It's scary...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F6")

    ChrTalk(    #8
        0x104,
        (
            "#032F#2PWhile the boiling water can cook us like\x01",
            "lobsters, the steam is an even greater\x01",
            "concern.\x02\x03",

            "Water need not be liquid to be deadly.\x01",
            "We must be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99D")

    label("loc_8F6")


    ChrTalk(    #9
        0x105,
        (
            "#042F#2PThe water is certainly dangerous, but\x01",
            "I'm even more worried about the steam.\x02\x03",

            "The steam is harder to avoid... and just\x01",
            "as hot and dangerous as the water.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A2B")

    ChrTalk(    #10
        0x106,
        (
            "#053F#5PYeah... good point.\x02\x03",

            "#050FLooks like there's a pattern\x01",
            "to when they blow.\x02\x03",

            "We'll have to time our movements carefully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC1")

    label("loc_A2B")


    ChrTalk(    #11
        0x103,
        (
            "#026F#5PYes... a very good point.\x02\x03",

            "#022FThe geysers seem to follow a pattern.\x02\x03",

            "We should watch them carefully,\x01",
            "and move when we have an opening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC1")


    ChrTalk(    #12
        0x101,
        "#1002F#4POkay! Follow me!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1423)
    OP_28(0x88, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_4_63C end

    def Function_5_AEC(): pass

    label("Function_5_AEC")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B65"),
        (1, "loc_B6B"),
        (SWITCH_DEFAULT, "loc_B71"),
    )


    label("loc_B65")

    OP_A2(0x1200)
    Jump("loc_B71")

    label("loc_B6B")

    OP_A2(0x1201)
    Jump("loc_B71")

    label("loc_B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B7F")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_B83")

    label("loc_B7F")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_B83")

    Return()

    # Function_5_AEC end

    def Function_6_B84(): pass

    label("Function_6_B84")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_BBE")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_BD8")

    label("loc_BBE")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_BD8")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_6_B84 end

    def Function_7_BEA(): pass

    label("Function_7_BEA")

    Call(0, 8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 3)), scpexpr(EXPR_END)), "loc_C3C")
    OP_43(0x8, 0x3, 0x0, 0x9)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x8D, 0x1, 0x6E)
    Call(0, 8)

    label("loc_C3C")

    PlayEffect(0x8E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x8E, 0x1, 0x6E)
    Call(0, 8)
    PlayEffect(0x8F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x8F, 0x1, 0x6E)
    Return()

    # Function_7_BEA end

    def Function_8_CB9(): pass

    label("Function_8_CB9")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_CDA"),
        (1, "loc_CE2"),
        (2, "loc_CEA"),
        (3, "loc_CF2"),
        (4, "loc_CFA"),
        (SWITCH_DEFAULT, "loc_D02"),
    )


    label("loc_CDA")

    Sleep(500)
    Jump("loc_D0A")

    label("loc_CE2")

    Sleep(1000)
    Jump("loc_D0A")

    label("loc_CEA")

    Sleep(1500)
    Jump("loc_D0A")

    label("loc_CF2")

    Sleep(2000)
    Jump("loc_D0A")

    label("loc_CFA")

    Sleep(2500)
    Jump("loc_D0A")

    label("loc_D02")

    Sleep(3000)
    Jump("loc_D0A")

    label("loc_D0A")

    Return()

    # Function_8_CB9 end

    def Function_9_D0B(): pass

    label("Function_9_D0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D21")
    OP_22(0x10D, 0x0, 0x64)
    Sleep(7000)
    Jump("Function_9_D0B")

    label("loc_D21")

    Return()

    # Function_9_D0B end

    SaveToFile()

Try(main)
