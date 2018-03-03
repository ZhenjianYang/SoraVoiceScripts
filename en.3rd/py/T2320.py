from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2320   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2320.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Creda',                                # 9
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
        'ED6_DT07/CH01010 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01010P._CP',             # 00
    )

    DeclNpc(
        X                   = 3470,
        Z                   = 0,
        Y                   = 8480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_FD",           # 01, 1
        "Function_2_FE",           # 02, 2
        "Function_3_103",          # 03, 3
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_E1")
    SetChrFlags(0x10, 0x80)
    Jump("loc_FC")

    label("loc_E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_EB")
    Jump("loc_FC")

    label("loc_EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_F5")
    Jump("loc_FC")

    label("loc_F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_FC")

    label("loc_FC")

    Return()

    # Function_0_D2 end

    def Function_1_FD(): pass

    label("Function_1_FD")

    Return()

    # Function_1_FD end

    def Function_2_FE(): pass

    label("Function_2_FE")

    Call(0, 3)
    Return()

    # Function_2_FE end

    def Function_3_103(): pass

    label("Function_3_103")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_110")
    Jump("loc_366")

    label("loc_110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_1F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_177")

    ChrTalk(    #0
        0x10,
        (
            "There's got to be something that would be good\x01",
            "to sell at the bazaar...but what?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F4")

    label("loc_177")


    ChrTalk(    #1
        0x10,
        (
            "Pots are no good. Not like anyone's gonna buy\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "I'm guessing Sadie's donated vases to be sold\x01",
            "there, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1F4")

    Jump("loc_366")

    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_35F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_25E")

    ChrTalk(    #3
        0x10,
        (
            "There's got to be something that would be good\x01",
            "to sell at the bazaar...but what?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C")

    label("loc_25E")


    ChrTalk(    #4
        0x10,
        (
            "Today's the start of the bazaar here in Manoria.\x01",
            "I feel like I should donate something to sell\x01",
            "there, too, but I don't know what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "It wouldn't feel right just donating leftovers\x01",
            "from the shop. I want something a bit more\x01",
            "special than that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_35C")

    Jump("loc_366")

    label("loc_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_366")

    label("loc_366")

    TalkEnd(0x10)
    Return()

    # Function_3_103 end

    SaveToFile()

Try(main)
