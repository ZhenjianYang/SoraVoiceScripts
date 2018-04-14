from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        "Function_1_23C",          # 01, 1
        "Function_2_31E",          # 02, 2
        "Function_3_435",          # 03, 3
        "Function_4_844",          # 04, 4
        "Function_5_8E0",          # 05, 5
    )


    def Function_0_226(): pass

    label("Function_0_226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23B")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_23B")

    Return()

    # Function_0_226 end

    def Function_1_23C(): pass

    label("Function_1_23C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E")
    OP_6F(0x2, 0)
    Jump("loc_255")

    label("loc_24E")

    OP_6F(0x2, 60)

    label("loc_255")

    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2B9")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_2D2")

    label("loc_2B9")

    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)

    label("loc_2D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_300")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_C4(0x0, 0x4)

    label("loc_300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_310")
    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)
    Jump("loc_31D")

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_END)), "loc_31D")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)

    label("loc_31D")

    Return()

    # Function_1_23C end

    def Function_2_31E(): pass

    label("Function_2_31E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_38D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1960)
    Jump("loc_3F3")

    label("loc_38D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_3F3")

    Jump("loc_427")

    label("loc_3F6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_427")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_31E end

    def Function_3_435(): pass

    label("Function_3_435")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_455")
    Call(0, 4)
    FadeToBright(0, 0)
    Call(0, 5)

    label("loc_455")

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
    FadeToBright(1000, 0)

    def lambda_513():
        OP_6D(-20060, -320, -45420, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_513)

    def lambda_52B():
        OP_67(0, 8330, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52B)

    def lambda_543():
        OP_6B(3130, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_543)

    def lambda_553():
        OP_6C(189000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_553)
    OP_6E(262, 8000)

    ChrTalk(    #3
        0x101,
        (
            "#1002F#6P……这里也完全\x01",
            "被浓雾笼罩了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        (
            "#022F#6P嗯嗯……\x02\x03",

            "这里的视线本来就不好，\x01",
            "这下更加寸步难行了呢。\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (6, "loc_5F6"),
        (5, "loc_626"),
        (3, "loc_65C"),
        (4, "loc_698"),
        (7, "loc_6C8"),
        (SWITCH_DEFAULT, "loc_6FE"),
    )


    label("loc_5F6")


    ChrTalk(    #5
        0x107,
        (
            "#065F#5P稍有松懈的话\x01",
            "也许就会迷路了呢…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FE")

    label("loc_626")


    ChrTalk(    #6
        0x106,
        (
            "#051F#5P嘿，掉以轻心的话\x01",
            "马上就会迷失方向吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FE")

    label("loc_65C")


    ChrTalk(    #7
        0x104,
        (
            "#035F#5P呼，要是不集中精力的话，\x01",
            "很容易就会迷路吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FE")

    label("loc_698")


    ChrTalk(    #8
        0x105,
        (
            "#043F#5P稍微一不注意\x01",
            "就会迷失方向了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FE")

    label("loc_6C8")


    ChrTalk(    #9
        0x108,
        (
            "#074F#5P如果放松精神的话，\x01",
            "很容易就会迷路吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FE")

    label("loc_6FE")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (6, "loc_71B"),
        (5, "loc_74F"),
        (3, "loc_783"),
        (4, "loc_7B7"),
        (7, "loc_7EB"),
        (SWITCH_DEFAULT, "loc_81F"),
    )


    label("loc_71B")


    ChrTalk(    #10
        0x107,
        (
            "#062F#5P看来最好还是\x01",
            "仔细看着指南针前进啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F")

    label("loc_74F")


    ChrTalk(    #11
        0x106,
        (
            "#555F#5P看来最好还是\x01",
            "仔细看着指南针前进啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F")

    label("loc_783")


    ChrTalk(    #12
        0x104,
        (
            "#030F#5P看来最好还是\x01",
            "仔细看着指南针前进啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F")

    label("loc_7B7")


    ChrTalk(    #13
        0x105,
        (
            "#042F#5P看来最好还是\x01",
            "仔细看着指南针前进啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F")

    label("loc_7EB")


    ChrTalk(    #14
        0x108,
        (
            "#072F#5P看来最好还是\x01",
            "仔细看着指南针前进啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F")

    label("loc_81F")

    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_A2(0x1824)
    OP_28(0x92, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_3_435 end

    def Function_4_844(): pass

    label("Function_4_844")

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
        (0, "loc_8C1"),
        (1, "loc_8C7"),
        (SWITCH_DEFAULT, "loc_8CD"),
    )


    label("loc_8C1")

    OP_A2(0x1200)
    Jump("loc_8CD")

    label("loc_8C7")

    OP_A2(0x1201)
    Jump("loc_8CD")

    label("loc_8CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_8DB")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_8DF")

    label("loc_8DB")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_8DF")

    Return()

    # Function_4_844 end

    def Function_5_8E0(): pass

    label("Function_5_8E0")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_5_8E0 end

    SaveToFile()

Try(main)
