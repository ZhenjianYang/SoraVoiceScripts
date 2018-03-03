from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3117   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3117.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Ray',                                  # 9
        'Terry',                                # 10
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01660 ._CH',             # 01
        'ED6_DT07/CH01050 ._CH',             # 02
        'ED6_DT07/CH01700 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01660P._CP',             # 01
        'ED6_DT07/CH01050P._CP',             # 02
        'ED6_DT07/CH01700P._CP',             # 03
    )

    DeclNpc(
        X                   = 1730,
        Z                   = 0,
        Y                   = 15000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 1050,
        Z                   = 0,
        Y                   = 7470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_121",          # 01, 1
        "Function_2_122",          # 02, 2
        "Function_3_146",          # 03, 3
        "Function_4_3C0",          # 04, 4
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_120")

    Return()

    # Function_0_10A end

    def Function_1_121(): pass

    label("Function_1_121")

    Return()

    # Function_1_121 end

    def Function_2_122(): pass

    label("Function_2_122")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_145")
    OP_8D(0xFE, 4670, 5810, -4590, 550, 1000)
    Jump("Function_2_122")

    label("loc_145")

    Return()

    # Function_2_122 end

    def Function_3_146(): pass

    label("Function_3_146")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_3BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_223")

    ChrTalk(    #0
        0xFE,
        (
            "I can't exactly pretend to be an expert in the\x01",
            "field of making archaisms, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Maybe I should start by gathering research\x01",
            "materials, then. After that, I can get to work\x01",
            "on the blueprints.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC")

    label("loc_223")


    ChrTalk(    #2
        0xFE,
        (
            "Well, I think all of the greenhouse experiments\x01",
            "are basically done now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Which meeeans it's time to start work\x01",
            "on my next project: making an archaism\x01",
            "modeled after Tita!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Haha... Time to start with drawing up\x01",
            "those blueprints!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x106,
        (
            "#053F(Tita's mom's eyes creeped me out when\x01",
            "I saw those, but this guy doesn't seem to\x01",
            "be in his right mind, either...)\x02\x03",

            "#057F(...Maybe I oughtta stop him, too?)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3BC")

    TalkEnd(0xFE)
    Return()

    # Function_3_146 end

    def Function_4_3C0(): pass

    label("Function_4_3C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_5E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4DE")

    ChrTalk(    #6
        0xFE,
        "Now it's my turn to look after the greenhouses.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Which means I can fully dedicate myself to\x01",
            "furthering my own research. Which is great...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "...except for the bit where I've got no idea what\x01",
            "to actually work on right now. Nothing's coming\x01",
            "to mind at all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E2")

    label("loc_4DE")


    ChrTalk(    #9
        0xFE,
        (
            "Ray was able to produce a plant capable of\x01",
            "soothing people in a mere three months, which\x01",
            "is pretty amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I still can't believe he was actually able to do\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "How did he even pull it off? He barely even did\x01",
            "any selective breeding at all!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_5E2")

    TalkEnd(0xFE)
    Return()

    # Function_4_3C0 end

    SaveToFile()

Try(main)
