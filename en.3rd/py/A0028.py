from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'A0028   ._SN',
        MapName             = 'Minigame',
        Location            = 'MG05_00.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        'Gilbert',                              # 9
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 0,
        Unknown_18              = 0,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 10000,
        Unknown_28              = 2800,
        Unknown_2C              = 1400,
        Unknown_30              = 0,
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

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 0,
        Unknown_18              = 0,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 10000,
        Unknown_28              = 2800,
        Unknown_2C              = 1400,
        Unknown_30              = 0,
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_10E",          # 00, 0
        "Function_1_132",          # 01, 1
        "Function_2_133",          # 02, 2
        "Function_3_180",          # 03, 3
        "Function_4_58C",          # 04, 4
        "Function_5_5D1",          # 05, 5
        "Function_6_618",          # 06, 6
    )


    def Function_0_10E(): pass

    label("Function_0_10E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121")
    Event(0, 4)
    Jump("loc_131")

    label("loc_121")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131")
    Event(0, 5)

    label("loc_131")

    Return()

    # Function_0_10E end

    def Function_1_132(): pass

    label("Function_1_132")

    Return()

    # Function_1_132 end

    def Function_2_133(): pass

    label("Function_2_133")

    OP_E2(0x3, 0x2)

    Menu(
        0,
        -1,
        330,
        0,
        (
            "[Play] (Debug)\x01",      # 0
            "[Skip] (Debug)\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_179"),
        (SWITCH_DEFAULT, "loc_17F"),
    )


    label("loc_179")

    OP_A2(0x0)
    Jump("loc_17F")

    label("loc_17F")

    Return()

    # Function_2_133 end

    def Function_3_180(): pass

    label("Function_3_180")

    FadeToDark(0, 0, -1)
    OP_E2(0x3, 0x2)
    OP_1D(0xC2)
    OP_AD(0x240144, 0x0, 0x0, 0x1F4)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56B")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Start\x01",         # 0
            "Rules\x01",         # 1
            "Settings\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_204"),
        (1, "loc_260"),
        (2, "loc_560"),
        (3, "loc_565"),
        (SWITCH_DEFAULT, "loc_568"),
    )


    label("loc_204")


    Menu(
        1,
        -1,
        330,
        1,
        (
            "[Normal]\x01",      # 0
            "[Easy]\x01",        # 1
        )
    )

    MenuEnd(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_247"),
        (1, "loc_24D"),
        (SWITCH_DEFAULT, "loc_253"),
    )


    label("loc_247")

    OP_E2(0xB, 0x0)
    Jump("loc_25D")

    label("loc_24D")

    OP_E2(0xB, 0x1)
    Jump("loc_25D")

    label("loc_253")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25D")

    Jump("loc_568")

    label("loc_260")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01",
            "　\x01",
            "　Shoot down approaching enemies and missiles\x01",
            "　using Josette's machine gun.\x01",
            "　The controls are as follows.\x01",
            "　\x01",
            "　Arrow Keys/Mouse    : Aim\x01",
            "　OK Key/Button       : Fire (Hold)\x01",
            "　Cancel Key/Button   : Zoom (Hold)\x01",
            "  Notebook Key/Button : Change View\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01",
            "　\x01",
            "　You have unlimited ammo, but take heed:\x01",
            "　Shoot for too long, and you'll shoot slower.\x01",
            "　Shot speed recovers gradually when not shooting.\x01",
            "　\x01",
            "　If the Bobcat's health falls to 0,\x01",
            "　you'll get a Game Over, so be careful!\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_568")

    label("loc_560")

    OP_E2(0x7)
    Jump("loc_568")

    label("loc_565")

    Jump("loc_568")

    label("loc_568")

    Jump("loc_1B1")

    label("loc_56B")

    FadeToBright(0, 0)
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_180 end

    def Function_4_58C(): pass

    label("Function_4_58C")

    Call(0, 3)
    OP_E2(0x9, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C6")
    Sleep(1000)
    OP_E2(0x8)
    Sleep(1000)
    OP_E2(0x4, 0x0)
    Sleep(1000)
    OP_E2(0x0, 0x1)
    OP_E2(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0xA)"), scpexpr(EXPR_END)), "loc_5C6")
    OP_A2(0x2509)
    OP_E2(0x5, 2163187, 0x0)
    ExitThread()

    label("loc_5C6")

    OP_A2(0x2506)
    OP_E2(0x5, 2162855, 0x0)
    Return()

    # Function_4_58C end

    def Function_5_5D1(): pass

    label("Function_5_5D1")

    OP_E2(0x9, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D")
    OP_E2(0x4, 0x0)
    OP_E2(0x0, 0x2)
    OP_E2(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0xA)"), scpexpr(EXPR_END)), "loc_5F6")
    OP_A2(0x2509)
    OP_E2(0x5, 2163187, 0x64)
    ExitThread()

    label("loc_5F6")

    OP_E2(0x3, 0x0)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    Sleep(4000)

    label("loc_60D")

    OP_A2(0x2506)
    OP_E2(0x5, 2163187, 0x0)
    Return()

    # Function_5_5D1 end

    def Function_6_618(): pass

    label("Function_6_618")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_77F")

    label("loc_63D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_656")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_77F")

    label("loc_656")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_77F")

    label("loc_66F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_688")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_77F")

    label("loc_688")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A1")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_77F")

    label("loc_6A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BA")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_77F")

    label("loc_6BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D3")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_77F")

    label("loc_6D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EC")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_77F")

    label("loc_6EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_705")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_77F")

    label("loc_705")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_77F")

    label("loc_71E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_737")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_77F")

    label("loc_737")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_750")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_77F")

    label("loc_750")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_769")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_77F")

    label("loc_769")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_77F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_794")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_77F")

    label("loc_794")

    Return()

    # Function_6_618 end

    SaveToFile()

Try(main)
