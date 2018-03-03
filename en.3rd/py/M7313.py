from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7313   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7313.x',
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
        'Tempest Pom',                          # 9
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
        'ED6_DT29/CH14050 ._CH',             # 00
        'ED6_DT29/CH14051 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT29/CH14050P._CP',             # 00
        'ED6_DT29/CH14051P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 7530,
        Y                   = 41000,
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


    DeclEvent(
        X                   = 0,
        Y                   = 7000,
        Z                   = 41000,
        Range               = 4000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -3020,
        TriggerZ            = 5530,
        TriggerY            = 7170,
        TriggerRange        = 1000,
        ActorX              = -4500,
        ActorZ              = 8550,
        ActorY              = 7500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_11E",          # 00, 0
        "Function_1_13B",          # 01, 1
        "Function_2_194",          # 02, 2
        "Function_3_1AA",          # 03, 3
        "Function_4_433",          # 04, 4
        "Function_5_48C",          # 05, 5
        "Function_6_638",          # 06, 6
        "Function_7_6FB",          # 07, 7
    )


    def Function_0_11E(): pass

    label("Function_0_11E")

    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_13A")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_13A")

    Return()

    # Function_0_11E end

    def Function_1_13B(): pass

    label("Function_1_13B")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x2300A0)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    OP_82(0x89, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_16A")
    OP_82(0x8A, 0x0)
    Jump("loc_16D")

    label("loc_16A")

    OP_82(0x8B, 0x0)

    label("loc_16D")

    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x583, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x582, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x582, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x582, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_193")
    ClearChrFlags(0x10, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_193")

    Return()

    # Function_1_13B end

    def Function_2_194(): pass

    label("Function_2_194")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_194")

    label("loc_1A9")

    Return()

    # Function_2_194 end

    def Function_3_1AA(): pass

    label("Function_3_1AA")

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
        "\x07\x05A mysterious monster is lurking here.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Fight\x01",            # 0
            "Don't Fight\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_25A"),
        (SWITCH_DEFAULT, "loc_2B0"),
    )


    label("loc_25A")

    Fade(500)
    SetChrPos(0x0, 0, 7530, 35620, 0)
    SetChrPos(0x1, 0, 7530, 35620, 0)
    SetChrPos(0x2, 0, 7530, 35620, 0)
    SetChrPos(0x3, 0, 7530, 35620, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_2B0")

    Battle(0x2ED, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_2C9"),
        (SWITCH_DEFAULT, "loc_31C"),
    )


    label("loc_2C9")

    EventBegin(0x1)
    SetChrPos(0x0, 0, 7530, 35620, 0)
    SetChrPos(0x1, 0, 7530, 35620, 0)
    SetChrPos(0x2, 0, 7530, 35620, 0)
    SetChrPos(0x3, 0, 7530, 35620, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_31C")

    EventBegin(0x1)
    SetChrPos(0x0, -880, 7530, 35170, 0)
    SetChrPos(0x1, 1000, 7530, 34930, 0)
    SetChrPos(0x2, -710, 7530, 32930, 0)
    SetChrPos(0x3, 1130, 7530, 32800, 0)
    OP_69(0x0, 0x0)
    SetChrFlags(0x10, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05Defeated the monster!\x02",
    )

    CloseMessageWindow()
    OP_F7(0xF, 0x4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x582, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F")
    OP_3E(0x33B, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Received \x1F\x3B\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_3E(0x183, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Received \x1F\x83\x01\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_40F")

    OP_A2(0x2C14)
    OP_A2(0x2C18)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_30(0x0)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_3_1AA end

    def Function_4_433(): pass

    label("Function_4_433")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_4_433 end

    def Function_5_48C(): pass

    label("Function_5_48C")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -1860, 5530, 7870, 270)
    SetChrPos(0x1, -1890, 5530, 6130, 270)
    SetChrPos(0x2, -170, 5530, 7760, 270)
    SetChrPos(0x3, -100, 5530, 6090, 270)
    OP_6D(-2670, 5530, 7150, 0)
    OP_67(0, 5980, -10000, 0)
    OP_6B(4240, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_562")
    OP_28(0xF, 0x4, 0x2)
    OP_82(0x8A, 0x2)
    PlayEffect(0x8B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_562")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #5
        (
            "\x07\x05#40WBring to me the girl loved by the\x01",
            "world's darkness.\x01",
            "#500W \x01",
            "#40WOnly then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_627")
    Call(0, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_624")
    Call(0, 6)

    label("loc_624")

    Jump("loc_627")

    label("loc_627")

    FadeToBright(300, 0)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_5_48C end

    def Function_6_638(): pass

    label("Function_6_638")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x89, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x0)
    Sleep(500)

    def lambda_6A1():
        OP_6B(3400, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6A1)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    ClearMapFlags(0x100000)
    ClearMapFlags(0x2000000)
    OP_23(0x17B)
    OP_E3(0x0, 0x3, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_638 end

    def Function_7_6FB(): pass

    label("Function_7_6FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -1860, 5530, 7870, 270)
    SetChrPos(0x1, -1890, 5530, 6130, 270)
    SetChrPos(0x2, -170, 5530, 7760, 270)
    SetChrPos(0x3, -100, 5530, 6090, 270)
    OP_6D(-2670, 5530, 7150, 0)
    OP_67(0, 5980, -10000, 0)
    OP_6B(4240, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_7_6FB end

    SaveToFile()

Try(main)
