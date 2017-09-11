from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4123   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4123.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        'Anelace',                              # 9
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
        'ED6_DT07/CH01630 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01630P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_F5",           # 01, 1
        "Function_2_F6",           # 02, 2
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F4")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 10500, 0, 5390, 90)

    label("loc_F4")

    Return()

    # Function_0_D2 end

    def Function_1_F5(): pass

    label("Function_1_F5")

    Return()

    # Function_1_F5 end

    def Function_2_F6(): pass

    label("Function_2_F6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_351")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 9240, 0, 5790, 90)
    SetChrPos(0x102, 9180, 0, 4760, 90)
    SetChrPos(0x108, 8280, 0, 5410, 90)
    TurnDirection(0x8, 0x108, 0)
    OP_A2(0x64C)
    OP_6D(9900, 0, 5380, 1000)

    ChrTalk(    #0
        0x8,
        (
            "Well, if it isn't Zin\x01",
            "and the new recruits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        "Back from the castle already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#000FWell, yeah, I guess we are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#010FAnelace, could we have a moment\x01",
            "of your time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Hmm? You hear something juicy\x01",
            "you're looking to share with\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#000FWell...if by 'juicy' you mean\x01",
            "'spit your juice all over in\x01",
            "shock,' then yeah...\x02\x03",

            "...it's a real juice-bomb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "Ooooh! You have my undivided\x01",
            "attention!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "Should we be talking about \x01",
            "this here, or should I be\x01",
            "sitting down for it?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FF)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_351")

    TalkEnd(0x8)
    Return()

    # Function_2_F6 end

    SaveToFile()

Try(main)
