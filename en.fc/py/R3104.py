from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3104   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3104.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60020",
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
        'Monster',                              # 9
        'Monster',                              # 10
        'Monster',                              # 11
        'Monster',                              # 12
        'Monster',                              # 13
        'Tratt Plains Road',                    # 14
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
        Unknown_3A              = 144,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10060 ._CH',             # 00
        'ED6_DT09/CH10061 ._CH',             # 01
        'ED6_DT07/CH00100 ._CH',             # 02
        'ED6_DT07/CH00101 ._CH',             # 03
        'ED6_DT07/CH00110 ._CH',             # 04
        'ED6_DT07/CH00111 ._CH',             # 05
        'ED6_DT07/CH00150 ._CH',             # 06
        'ED6_DT07/CH00151 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10060P._CP',             # 00
        'ED6_DT09/CH10061P._CP',             # 01
        'ED6_DT07/CH00100P._CP',             # 02
        'ED6_DT07/CH00101P._CP',             # 03
        'ED6_DT07/CH00110P._CP',             # 04
        'ED6_DT07/CH00111P._CP',             # 05
        'ED6_DT07/CH00150P._CP',             # 06
        'ED6_DT07/CH00151P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 50,
        Z                   = -130,
        Y                   = -59690,
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


    ScpFunction(
        "Function_0_1AA",          # 00, 0
        "Function_1_1E9",          # 01, 1
        "Function_2_232",          # 02, 2
        "Function_3_3BA",          # 03, 3
        "Function_4_1264",         # 04, 4
        "Function_5_1297",         # 05, 5
    )


    def Function_0_1AA(): pass

    label("Function_0_1AA")

    ClearMapFlags(0x40000000)
    AddParty(0xFF, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1C2"),
        (101, "loc_1D5"),
        (SWITCH_DEFAULT, "loc_1E8"),
    )


    label("loc_1C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D2")
    Event(0, 3)

    label("loc_1D2")

    Jump("loc_1E8")

    label("loc_1D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E5")
    Event(0, 5)

    label("loc_1E5")

    Jump("loc_1E8")

    label("loc_1E8")

    Return()

    # Function_0_1AA end

    def Function_1_1E9(): pass

    label("Function_1_1E9")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x30031)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_210")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_228")
    OP_B1("R3104_y")
    Jump("loc_231")

    label("loc_228")

    OP_B1("R3104_n")

    label("loc_231")

    Return()

    # Function_1_1E9 end

    def Function_2_232(): pass

    label("Function_2_232")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3A4")

    label("loc_262")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3A4")

    label("loc_27B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3A4")

    label("loc_294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3A4")

    label("loc_2AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C6")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3A4")

    label("loc_2C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3A4")

    label("loc_2DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3A4")

    label("loc_2F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3A4")

    label("loc_311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3A4")

    label("loc_32A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3A4")

    label("loc_343")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3A4")

    label("loc_35C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_375")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3A4")

    label("loc_375")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3A4")

    label("loc_38E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3A4")

    label("loc_3B9")

    Return()

    # Function_2_232 end

    def Function_3_3BA(): pass

    label("Function_3_3BA")

    EventBegin(0x0)
    OP_6D(620, -50, -47670, 0)
    SetChrPos(0x101, 430, -70, -48480, 0)
    SetChrPos(0x106, 950, -90, -49600, 0)
    SetChrPos(0x102, -1020, -40, -49790, 0)
    FadeToBright(1000, 0)
    OP_66(0x0)

    def lambda_412():
        OP_67(-22360, 30130, -70650, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_412)
    OP_6D(270, 5050, -6000, 6000)
    Fade(1000)
    OP_66(0x1)
    OP_6D(380, 650, -19840, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 380, -100, -22070, 0)
    SetChrPos(0x106, 1170, -30, -23100, 0)
    SetChrPos(0x102, -1140, -60, -23590, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#002FSo this is the Carnelia Tower...\x02\x03",

            "Are the kidnappers really\x01",
            "holding the professor here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x106,
        (
            "#552FYep. Look at the big\x01",
            "jumble of footprints.\x02\x03",

            "If you need a hiding place,\x01",
            "this would probably be a \x01",
            "good place for it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 4)
    OP_0D()

    ChrTalk(    #2
        0x102,
        "#016FLook out!\x02",
    )

    CloseMessageWindow()

    def lambda_5D5():
        OP_6C(32000, 2000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5D5)
    OP_6D(-150, 3850, -10760, 2000)
    SetChrPos(0x8, -1210, 5050, -5570, 0)
    SetChrPos(0x9, -670, 4650, -6550, 0)
    SetChrPos(0xA, 260, 5050, -5940, 0)
    SetChrPos(0xB, 990, 5050, -5750, 0)
    SetChrPos(0xC, 1500, 5050, -5570, 0)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)

    def lambda_664():
        OP_6D(400, 650, -19840, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_664)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x106, 6)
    ClearChrFlags(0x8, 0x80)

    def lambda_68B():
        OP_8E(0xFE, 0xFFFFFBE6, 0x41A, 0xFFFFB762, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_68B)
    Sleep(200)
    ClearChrFlags(0xC, 0x80)

    def lambda_6B0():
        OP_8E(0xFE, 0x55A, 0x41A, 0xFFFFB7C6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6B0)
    Sleep(500)
    ClearChrFlags(0xA, 0x80)

    def lambda_6D5():
        OP_8E(0xFE, 0x1E, 0x41A, 0xFFFFB668, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6D5)
    Sleep(500)
    ClearChrFlags(0x9, 0x80)

    def lambda_6FA():
        OP_8E(0xFE, 0xFFFFFE0C, 0x5AA, 0xFFFFBD2A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6FA)
    Sleep(200)
    ClearChrFlags(0xB, 0x80)

    def lambda_71F():
        OP_8E(0xFE, 0x2E4, 0x5AA, 0xFFFFBD3E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_71F)
    OP_43(0x106, 0x0, 0x0, 0x4)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x4)

    def lambda_74B():
        OP_96(0xFE, 0xFFFFF646, 0xBEA, 0xFFFFAC54, 0x9C4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_74B)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x4)
    OP_96(0xC, 0x9CE, 0xBEA, 0xFFFFAC54, 0x9C4, 0x1B58)
    Sleep(1000)

    ChrTalk(    #3
        0x101,
        "#005FMonsters!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x106,
        "#054FHeh... As I expected!\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    SetChrChipByIndex(0x9, 1)
    SetChrChipByIndex(0xA, 1)
    SetChrChipByIndex(0xB, 1)

    def lambda_7DE():
        OP_8E(0xFE, 0xA0, 0xFFFFFFCE, 0xFFFF7DF6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7DE)

    def lambda_7F9():
        OP_8E(0xFE, 0xA0, 0xFFFFFFCE, 0xFFFF7DF6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7F9)

    def lambda_814():
        OP_8E(0xFE, 0xA0, 0xFFFFFFCE, 0xFFFF7DF6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_814)
    Sleep(150)
    OP_44(0x8, 0xFF)
    SetChrChipByIndex(0x8, 1)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x8, 0x101, 0)

    def lambda_84F():
        OP_96(0xFE, 0xFFFFFF7E, 0xFFFFFFA6, 0xFFFFA394, 0x384, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_84F)
    Sleep(100)
    OP_44(0xC, 0xFF)
    SetChrChipByIndex(0xC, 1)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xC, 0x101, 0)

    def lambda_88D():
        OP_96(0xFE, 0xFFFFFF7E, 0xFFFFFFA6, 0xFFFFA394, 0x384, 0x1B58)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_88D)
    Sleep(250)
    Battle(0x3A6, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_8C3"),
        (SWITCH_DEFAULT, "loc_8C6"),
    )


    label("loc_8C3")

    OP_B4(0x0)
    Return()

    label("loc_8C6")

    EventBegin(0x0)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, 380, -100, -22070, 0)
    SetChrPos(0x106, 880, -30, -23670, 0)
    SetChrPos(0x102, -1140, -60, -23590, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrChipByIndex(0x102, 65535)
    OP_6D(310, -90, -21210, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #5
        0x101,
        (
            "#002F#3PWhat are monsters like that\x01",
            "doing here...?\x02\x03",

            "#004FOh, maybe...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_9A3)

    def lambda_9B1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B1)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[It's just a coincidence?]\x01",                               # 0
            "[They live in the tower?]\x01",                                # 1
            "[They're tied somehow to the men in black clothes?]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A77"),
        (1, "loc_BB9"),
        (2, "loc_CFF"),
        (SWITCH_DEFAULT, "loc_DB0"),
    )


    label("loc_A77")


    ChrTalk(    #6
        0x101,
        "#005F#3PIt's just a coincidence?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x106,
        "#053FDon't be such an idiot.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 600)

    ChrTalk(    #8
        0x101,
        "#509F#3PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#012F#1PIt's not impossible...but I think it's\x01",
            "far more likely that the men in the\x01",
            "black clothes brought them here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x106,
        (
            "#057FGot it in one.\x02\x03",

            "They've probably been trained for combat by\x01",
            "our little friends in black.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB0")

    label("loc_BB9")


    ChrTalk(    #11
        0x101,
        "#005F#3PThey live in the tower?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x106,
        "#053FDon't be such an idiot.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 600)

    ChrTalk(    #13
        0x101,
        "#509F#3PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#012F#1PIt's not impossible...but I think it's\x01",
            "far more likely that the men in the\x01",
            "black clothes brought them here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x106,
        (
            "#057FGot it in one.\x02\x03",

            "They've probably been trained for combat by\x01",
            "our little friends in black.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x41, 0x1)
    Jump("loc_DB0")

    label("loc_CFF")


    ChrTalk(    #16
        0x101,
        (
            "#005F#3PThey're tied somehow to the\x01",
            "men in black clothes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x106,
        (
            "#057FGot it in one.\x02\x03",

            "They've probably been trained for combat by\x01",
            "our little friends in black.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x41, 0x3)
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_DB0")

    label("loc_DB0")


    def lambda_DB6():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB6)

    ChrTalk(    #18
        0x101,
        "#580F#3PTrained...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x106,
        (
            "#552FEver since I started checking\x01",
            "these guys out, I've gotten\x01",
            "attacked by monsters constantly.\x02\x03",

            "Ain't no way that's a coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#007F#3PI see...\x02\x03",

            "#005FSo...that means that the checkpoint\x01",
            "up in the mountain pass was attacked\x01",
            "because YOU were there?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x106,
        (
            "#053FI guess.\x02\x03",

            "#050FIt was your old man who assigned\x01",
            "me this gig in the first place.\x02\x03",

            "It ain't like it's been a night at\x01",
            "the strip club for me, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#509F#3PStrip club, huh?\x01",
            "How very...YOU.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#012F#1PAh...anyway... This reminds me.\x01",
            "Jean mentioned something about\x01",
            "that, right?\x02\x03",

            "Can you share some details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x106,
        (
            "#551FHe showed up just before that whole sky bandit\x01",
            "mess started and dumped it on me.\x02\x03",

            "Said something about some crap coming up that\x01",
            "really couldn't wait.\x02\x03",

            "An 'easy' job, he says. That old man always\x01",
            "plays innocent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#505F#3P(That is so very Dad...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x106,
        (
            "#057FAnd after the last couple of run-ins with\x01",
            "them, there's NO WAY I'm giving anyone\x01",
            "else the satisfaction of catching them.\x02\x03",

            "I especially want to get that one little\x01",
            "bastard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#002F#3P???\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        "#014F#1PWhich would be whom?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x106,
        (
            "#552F...Never mind.\x02\x03",

            "Let's just arrest these guys\x01",
            "and rescue the professor.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x539)
    EventEnd(0x0)
    Return()

    # Function_3_3BA end

    def Function_4_1264(): pass

    label("Function_4_1264")

    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 0)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 0)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 0)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 0)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 0)
    Return()

    # Function_4_1264 end

    def Function_5_1297(): pass

    label("Function_5_1297")

    EventBegin(0x0)
    OP_6D(120, 5050, -5370, 0)
    SetChrPos(0x101, 0, 5050, -5210, 0)
    SetChrPos(0x102, -830, 5050, -5210, 0)
    SetChrPos(0x107, 900, 5050, -5210, 0)
    SetChrPos(0x106, 0, 5050, -5210, 0)

    def lambda_12F4():
        OP_6D(250, 3850, -10670, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12F4)

    def lambda_130C():
        OP_8E(0xFE, 0xFFFFFFF6, 0xF0A, 0xFFFFD1B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_130C)
    Sleep(400)

    def lambda_132C():
        OP_8E(0xFE, 0xFFFFFBD2, 0xF0A, 0xFFFFD378, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_132C)
    Sleep(200)

    def lambda_134C():
        OP_8E(0xFE, 0x2C6, 0xF0A, 0xFFFFD83C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_134C)
    Sleep(200)

    def lambda_136C():
        OP_8E(0xFE, 0x50, 0xF0A, 0xFFFFDCD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_136C)
    WaitChrThread(0x106, 0x1)

    ChrTalk(    #30
        0x106,
        "#053F...\x02",
    )

    OP_9E(0x106, 0x1E, 0x0, 0x258, 0xBB8)

    def lambda_13AC():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13AC)

    def lambda_13BA():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13BA)

    def lambda_13C8():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_13C8)
    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#004FWh-What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x106,
        (
            "#552FIt's nothing.\x02\x03",

            "Just...felt a little dizzy for a sec.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x107,
        (
            "#065F#4PAh...!\x02\x03",

            "Maybe from when you protected\x01",
            "me, earlier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#004FThat's right...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        (
            "#012FYou did get shot...but I thought\x01",
            "you blocked it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x106,
        (
            "#053FJust a scratch.\x01",
            "It's no big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x107,
        "#063F#4PB-But... It's my fault...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x106,
        (
            "#055FListen. I get worse injuries\x01",
            "than this from shaving.\x02\x03",

            "Now, quit fussing, and let's\x01",
            "just get back to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#002FO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        "#012F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x53B)
    EventEnd(0x0)
    Return()

    # Function_5_1297 end

    SaveToFile()

Try(main)
