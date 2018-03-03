from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7312   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7312.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60224",
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
        'Lucifuge',                             # 9
        'Beelzebub',                            # 10
        'Aka Manaf',                            # 11
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
        'ED6_DT29/CH14590 ._CH',             # 00
        'ED6_DT29/CH14591 ._CH',             # 01
        'ED6_DT29/CH14060 ._CH',             # 02
        'ED6_DT29/CH14060 ._CH',             # 03
        'ED6_DT29/CH14640 ._CH',             # 04
        'ED6_DT29/CH14640 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14590P._CP',             # 00
        'ED6_DT29/CH14591P._CP',             # 01
        'ED6_DT29/CH14060P._CP',             # 02
        'ED6_DT29/CH14060P._CP',             # 03
        'ED6_DT29/CH14640P._CP',             # 04
        'ED6_DT29/CH14640P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 4000,
        Y                   = 6000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 4000,
        Y                   = 6000,
        Direction           = 180,
        Unknown2            = 2,
        Unknown3            = 131072,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 4000,
        Y                   = 6000,
        Direction           = 180,
        Unknown2            = 4,
        Unknown3            = 262144,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 40,
        Y                   = 3000,
        Z                   = 6090,
        Range               = 4000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -7420,
        TriggerZ            = 3930,
        TriggerY            = 44010,
        TriggerRange        = 3000,
        ActorX              = -7420,
        ActorZ              = 5000,
        ActorY              = 44010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_17E",          # 00, 0
        "Function_1_1AC",          # 01, 1
        "Function_2_29A",          # 02, 2
        "Function_3_2B0",          # 03, 3
        "Function_4_5EA",          # 04, 4
        "Function_5_60B",          # 05, 5
    )


    def Function_0_17E(): pass

    label("Function_0_17E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1AB")

    label("loc_196")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_1AB")

    Return()

    # Function_0_17E end

    def Function_1_1AC(): pass

    label("Function_1_1AC")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x23009F)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    LoadEffect(0x0, "map\\mpU70_01.eff")
    PlayEffect(0x0, 0x7, 0xFF, -7400, 4600, 43990, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_B2(0x0, 0x0, 0x80)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (5, "loc_229"),
        (10, "loc_247"),
        (15, "loc_270"),
        (SWITCH_DEFAULT, "loc_299"),
    )


    label("loc_229")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x199), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x582, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244")
    ClearChrFlags(0x10, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_244")

    Jump("loc_299")

    label("loc_247")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x19A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x582, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D")
    ClearChrFlags(0x11, 0x80)
    OP_B2(0x1, 0x0, 0x80)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26D")

    Jump("loc_299")

    label("loc_270")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x19B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x582, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_296")
    ClearChrFlags(0x12, 0x80)
    OP_B2(0x1, 0x0, 0x80)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_296")

    Jump("loc_299")

    label("loc_299")

    Return()

    # Function_1_1AC end

    def Function_2_29A(): pass

    label("Function_2_29A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2AF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_29A")

    label("loc_2AF")

    Return()

    # Function_2_29A end

    def Function_3_2B0(): pass

    label("Function_3_2B0")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05A dangerous fiend is lurking here.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Fight\x01",      # 0
            "Don't\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_357"),
        (SWITCH_DEFAULT, "loc_3AD"),
    )


    label("loc_357")

    Fade(500)
    SetChrPos(0x0, 0, 3930, 0, 0)
    SetChrPos(0x1, 0, 3930, 0, 0)
    SetChrPos(0x2, 0, 3930, 0, 0)
    SetChrPos(0x3, 0, 3930, 0, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_3AD")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C9")
    Battle(0x2E7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3F2")

    label("loc_3C9")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E5")
    Battle(0x2E8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3F2")

    label("loc_3E5")

    Battle(0x2E9, 0x0, 0x0, 0x0, 0xFF)

    label("loc_3F2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_3FE"),
        (SWITCH_DEFAULT, "loc_451"),
    )


    label("loc_3FE")

    EventBegin(0x1)
    SetChrPos(0x0, 0, 3930, 0, 0)
    SetChrPos(0x1, 0, 3930, 0, 0)
    SetChrPos(0x2, 0, 3930, 0, 0)
    SetChrPos(0x3, 0, 3930, 0, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_451")

    EventBegin(0x1)
    SetChrPos(0x0, -900, 3930, -190, 0)
    SetChrPos(0x1, 1170, 3930, -140, 0)
    SetChrPos(0x2, -690, 3930, -1970, 0)
    SetChrPos(0x3, 1220, 3930, -2320, 0)
    OP_69(0x0, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05Defeated the fiend!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_537")
    OP_F7(0xF, 0x1, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x582, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52E")
    OP_3E(0x33B, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Received \x1F\x3B\x03\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_52E")

    OP_A2(0x2C11)
    OP_A2(0x2C15)
    Jump("loc_5CC")

    label("loc_537")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_583")
    OP_F7(0xF, 0x2, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x582, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57A")
    OP_3E(0x33B, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Received \x1F\x3B\x03\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_57A")

    OP_A2(0x2C12)
    OP_A2(0x2C16)
    Jump("loc_5CC")

    label("loc_583")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CC")
    OP_F7(0xF, 0x3, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x582, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C6")
    OP_3E(0x33B, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05Received \x1F\x3B\x03\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_5C6")

    OP_A2(0x2C13)
    OP_A2(0x2C17)

    label("loc_5CC")

    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_30(0x0)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_3_2B0 end

    def Function_4_5EA(): pass

    label("Function_4_5EA")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (5, "loc_5FE"),
        (10, "loc_601"),
        (15, "loc_604"),
        (SWITCH_DEFAULT, "loc_607"),
    )


    label("loc_5FE")

    Jump("loc_607")

    label("loc_601")

    Jump("loc_607")

    label("loc_604")

    Jump("loc_607")

    label("loc_607")

    TalkEnd(0xFF)
    Return()

    # Function_4_5EA end

    def Function_5_60B(): pass

    label("Function_5_60B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05A mysterious spring is here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Drink\x01",        # 0
            "Refrain\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_69B"),
        (1, "loc_701"),
        (SWITCH_DEFAULT, "loc_701"),
    )


    label("loc_69B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_701")

    TalkEnd(0xFF)
    SetMapFlags(0x100000)
    Return()

    # Function_5_60B end

    SaveToFile()

Try(main)
