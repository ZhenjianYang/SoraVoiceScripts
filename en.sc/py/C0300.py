from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0300   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0300.x',
        MapIndex            = 19,
        MapDefaultBGM       = "ed60021",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
    )

    DeclEntryPoint(
        Unknown_00              = 20000,
        Unknown_04              = 0,
        Unknown_08              = 17000,
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
        Unknown_3A              = 19,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH12430 ._CH',             # 00
        'ED6_DT29/CH12431 ._CH',             # 01
        'ED6_DT09/CH10010 ._CH',             # 02
        'ED6_DT09/CH10011 ._CH',             # 03
        'ED6_DT09/CH10280 ._CH',             # 04
        'ED6_DT09/CH10281 ._CH',             # 05
        'ED6_DT29/CH12400 ._CH',             # 06
        'ED6_DT29/CH12401 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12430P._CP',             # 00
        'ED6_DT29/CH12431P._CP',             # 01
        'ED6_DT09/CH10010P._CP',             # 02
        'ED6_DT09/CH10011P._CP',             # 03
        'ED6_DT09/CH10280P._CP',             # 04
        'ED6_DT09/CH10281P._CP',             # 05
        'ED6_DT29/CH12400P._CP',             # 06
        'ED6_DT29/CH12401P._CP',             # 07
    )

    DeclMonster(
        X                   = -15740,
        Z                   = -150,
        Y                   = -20530,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10000,
        Z                   = -30,
        Y                   = 16830,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 11740,
        Z                   = -290,
        Y                   = 17440,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24030,
        Z                   = -200,
        Y                   = 33370,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14010,
        Z                   = -200,
        Y                   = 37450,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -15740,
        Z                   = -150,
        Y                   = -20530,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x40,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10000,
        Z                   = -30,
        Y                   = 16830,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 11740,
        Z                   = -290,
        Y                   = 17440,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24030,
        Z                   = -200,
        Y                   = 33370,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14010,
        Z                   = -200,
        Y                   = 37450,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x40,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 26850,
        TriggerZ            = 60,
        TriggerY            = 18280,
        TriggerRange        = 1000,
        ActorX              = 27590,
        ActorZ              = 60,
        ActorY              = 18320,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_226",          # 00, 0
        "Function_1_251",          # 01, 1
        "Function_2_333",          # 02, 2
        "Function_3_48F",          # 03, 3
        "Function_4_9CD",          # 04, 4
        "Function_5_A6C",          # 05, 5
    )


    def Function_0_226(): pass

    label("Function_0_226")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B")
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_250")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_250")

    Return()

    # Function_0_226 end

    def Function_1_251(): pass

    label("Function_1_251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263")
    OP_6F(0x2, 0)
    Jump("loc_26A")

    label("loc_263")

    OP_6F(0x2, 60)

    label("loc_26A")

    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2CE")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_2E7")

    label("loc_2CE")

    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)

    label("loc_2E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_315")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_315")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_C4(0x0, 0x4)

    label("loc_315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_325")
    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)
    Jump("loc_332")

    label("loc_325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_END)), "loc_332")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)

    label("loc_332")

    Return()

    # Function_1_251 end

    def Function_2_333(): pass

    label("Function_2_333")

    OP_EA(0x2, 0x1, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_3A4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1960)
    Jump("loc_408")

    label("loc_3A4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_408")

    Jump("loc_481")

    label("loc_40B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05It's empty. It wouldn't be in this predicament if\x01",
            "someone hadn't TAKEN WHAT WAS INSIDE.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_481")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_333 end

    def Function_3_48F(): pass

    label("Function_3_48F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AF")
    Call(0, 4)
    FadeToBright(0, 0)
    Call(0, 5)

    label("loc_4AF")

    SetChrPos(0x101, -20340, -280, -44000, 0)
    SetChrPos(0x103, -19310, -320, -44000, 0)
    SetChrPos(0xF8, -19370, -260, -45290, 0)
    SetChrPos(0xF9, -20400, -190, -45290, 0)
    OP_6D(-19450, -40, -4470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(200000, 0)
    OP_6E(463, 0)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_C8(0x200, 0x46, "C_PLAC14._CH", 0x1, 0x3E8)
    OP_DE("Mistwald")
    FadeToBright(1000, 0)

    def lambda_577():
        OP_6D(-20060, -320, -45420, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_577)

    def lambda_58F():
        OP_67(0, 8330, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58F)

    def lambda_5A7():
        OP_6B(3130, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A7)

    def lambda_5B7():
        OP_6C(189000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5B7)
    OP_6E(262, 8000)

    ChrTalk(    #3
        0x101,
        (
            "#1002F#5PThis area's completely engulfed in fog,\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        (
            "#022F#5PDamn.\x02\x03",

            "It was already dark and hard to see here.\x01",
            "It'll verge on the unnavigable if we don't\x01",
            "pay attention now.\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (6, "loc_6A0"),
        (5, "loc_6EC"),
        (3, "loc_73F"),
        (4, "loc_78B"),
        (7, "loc_7F4"),
        (SWITCH_DEFAULT, "loc_83A"),
    )


    label("loc_6A0")


    ChrTalk(    #5
        0x107,
        (
            "#065F#6PYeah, you could really get lost if you\x01",
            "don't pay attention!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83A")

    label("loc_6EC")


    ChrTalk(    #6
        0x106,
        (
            "#051F#6PHeh, yeah. You lose focus and you'd\x01",
            "get turned around in a second.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83A")

    label("loc_73F")


    ChrTalk(    #7
        0x104,
        (
            "#035F#6PLose focus for but a moment,\x01",
            "and you would be lost forever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83A")

    label("loc_78B")


    ChrTalk(    #8
        0x105,
        (
            "#043F#6PYes, if our attention slips for even a moment,\x01",
            "we could be lost for... a very long time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83A")

    label("loc_7F4")


    ChrTalk(    #9
        0x108,
        (
            "#074F#6PYou'd be lost in here for ages\x01",
            "if your focus slipped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83A")

    label("loc_83A")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (6, "loc_857"),
        (5, "loc_88E"),
        (3, "loc_8D7"),
        (4, "loc_921"),
        (7, "loc_95B"),
        (SWITCH_DEFAULT, "loc_9A8"),
    )


    label("loc_857")


    ChrTalk(    #10
        0x107,
        "#062F#6PLet's keep a close eye on our compass!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A8")

    label("loc_88E")


    ChrTalk(    #11
        0x106,
        (
            "#555F#6PWe should be okay if we keep a close\x01",
            "eye on our compass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A8")

    label("loc_8D7")


    ChrTalk(    #12
        0x104,
        (
            "#030F#6PIt would be wise to keep our compass\x01",
            "handy as we proceed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A8")

    label("loc_921")


    ChrTalk(    #13
        0x105,
        "#042F#6PLet's keep our compass close by as we go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A8")

    label("loc_95B")


    ChrTalk(    #14
        0x108,
        (
            "#072F#6PKeep an eye on our compass as we go,\x01",
            "and we'll be all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A8")

    label("loc_9A8")

    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_A2(0x1824)
    OP_28(0x92, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_3_48F end

    def Function_4_9CD(): pass

    label("Function_4_9CD")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Set Scherazard as Partner]\x01",      # 0
            "[Set Agate as Partner]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A4D"),
        (1, "loc_A53"),
        (SWITCH_DEFAULT, "loc_A59"),
    )


    label("loc_A4D")

    OP_A2(0x1200)
    Jump("loc_A59")

    label("loc_A53")

    OP_A2(0x1201)
    Jump("loc_A59")

    label("loc_A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A67")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_A6B")

    label("loc_A67")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_A6B")

    Return()

    # Function_4_9CD end

    def Function_5_A6C(): pass

    label("Function_5_A6C")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_5_A6C end

    SaveToFile()

Try(main)
