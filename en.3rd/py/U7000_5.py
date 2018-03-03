from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7000_5 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/U7000   ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_56F",          # 03, 3
        "Function_4_62C",          # 04, 4
        "Function_5_701",          # 05, 5
        "Function_6_7FE",          # 06, 6
        "Function_7_1D7B",         # 07, 7
        "Function_8_343A",         # 08, 8
        "Function_9_37D2",         # 09, 9
        "Function_10_3857",        # 0A, 10
        "Function_11_5428",        # 0B, 11
        "Function_12_56D3",        # 0C, 12
        "Function_13_5980",        # 0D, 13
        "Function_14_5BAC",        # 0E, 14
        "Function_15_5EA3",        # 0F, 15
        "Function_16_5EA4",        # 10, 16
        "Function_17_5EA5",        # 11, 17
        "Function_18_6302",        # 12, 18
        "Function_19_645A",        # 13, 19
        "Function_20_8530",        # 14, 20
        "Function_21_8553",        # 15, 21
        "Function_22_8599",        # 16, 22
        "Function_23_AC2C",        # 17, 23
        "Function_24_AC48",        # 18, 24
        "Function_25_ACA0",        # 19, 25
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-900, 4000, 4220, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(0, 0)
    OP_6E(435, 0)
    SetChrPos(0x0, -1040, 4000, 1270, 315)
    SetChrPos(0x1, -40, 4000, 2200, 315)
    SetChrPos(0x2, -110, 4000, -250, 315)
    SetChrPos(0x3, 870, 4000, 1110, 315)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_8C(0x22, 135, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x22,
        (
            "#1615F#5P#12CIncidentally, I have one piece of news I think you\x01",
            "may be interested in hearing.\x02\x03",

            "#1613FThe area Kevin and Ries fell into is not the only\x01",
            "part of the seventh plane that exists; I have\x01",
            "discovered another, much more vast area there.\x02\x03",

            "I also have reason to believe that it's filled to the\x01",
            "brim with devils, as well as highly dangerous.\x02\x03",

            "#1612FNonetheless, I've placed a monument down there \x01",
            "to serve as an anchor should you wish to explore.\x02\x03",

            "You should be able to warp there using the cube.#0C\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x02[The Abyss]\x07\x05 is now accessible.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #2
        (
            "\x07\x05It is now possible to warp to a new area on the\x01",
            "seventh plane through the warp menu.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #3
        (
            "\x07\x05This area contains countless powerful enemies,\x01",
            "devils included, making it the perfect place to\x01",
            "efficiently level your party members.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C21)
    OP_AA(7936)
    OP_28(0x3E, 0x1, 0x20)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-540, 4000, 1460, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, -540, 4000, 1460, 315)
    SetChrPos(0x1, -540, 4000, 1460, 315)
    SetChrPos(0x2, -540, 4000, 1460, 315)
    SetChrPos(0x3, -540, 4000, 1460, 315)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_AC end

    def Function_3_56F(): pass

    label("Function_3_56F")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62B")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Talk\x01",                          # 0
            "Take Off on the Arseille\x01",      # 1
            "Leave\x01",                         # 2
        )
    )

    MenuEnd(0x3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5F0"),
        (1, "loc_60A"),
        (SWITCH_DEFAULT, "loc_61B"),
    )


    label("loc_5F0")

    Call(5, 10)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_628")

    label("loc_60A")

    Call(5, 11)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_628")

    label("loc_61B")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_628")

    label("loc_628")

    Jump("loc_58C")

    label("loc_62B")

    Return()

    # Function_3_56F end

    def Function_4_62C(): pass

    label("Function_4_62C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_636")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_700")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Talk\x01",                                   # 0
            "Forge a Weapon Using Zemurian Ore\x01",      # 1
            "Leave\x01",                                  # 2
        )
    )

    MenuEnd(0x3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_6B6"),
        (1, "loc_6D0"),
        (SWITCH_DEFAULT, "loc_6F0"),
    )


    label("loc_6B6")

    Call(5, 10)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6FD")

    label("loc_6D0")

    Call(5, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6ED")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6ED")

    Jump("loc_6FD")

    label("loc_6F0")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6FD")

    label("loc_6FD")

    Jump("loc_636")

    label("loc_700")

    Return()

    # Function_4_62C end

    def Function_5_701(): pass

    label("Function_5_701")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FD")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Talk\x01",                                   # 0
            "Take Off on the Arseille\x01",               # 1
            "Forge a Weapon Using Zemurian Ore\x01",      # 2
            "Leave\x01",                                  # 3
        )
    )

    MenuEnd(0x3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_7A8"),
        (1, "loc_7C2"),
        (2, "loc_7D3"),
        (SWITCH_DEFAULT, "loc_7ED"),
    )


    label("loc_7A8")

    Call(5, 10)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7FA")

    label("loc_7C2")

    Call(5, 11)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7FA")

    label("loc_7D3")

    Call(5, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7EA")
    Call(5, 3)

    label("loc_7EA")

    Jump("loc_7FA")

    label("loc_7ED")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7FA")

    label("loc_7FA")

    Jump("loc_70B")

    label("loc_7FD")

    Return()

    # Function_5_701 end

    def Function_6_7FE(): pass

    label("Function_6_7FE")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-900, 4000, 4220, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(0, 0)
    OP_6E(435, 0)
    SetChrPos(0x0, -1040, 4000, 1270, 315)
    SetChrPos(0x1, -40, 4000, 2200, 315)
    SetChrPos(0x2, -110, 4000, -250, 315)
    SetChrPos(0x3, 870, 4000, 1110, 315)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_8C(0x22, 135, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x22,
        "#1614F#12C#5PWait... Could it be...?#0C\x02",
    )

    CloseMessageWindow()
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x22,
        (
            "#1612F#12C#5PI-Is that Zemurian Ore you have in your\x01",
            "possession?!\x02\x03",

            "#1613FUnbelievable... How did that end up being\x01",
            "recreated in Phantasma?\x02\x03",

            "How long has it been there?\x01",
            "...Was it perhaps there all along?#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x22, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x22)
    Sleep(500)

    ChrTalk(    #6
        0x22,
        (
            "#1615F#12C#5PWhile I believe this is also true in the time\x01",
            "period that you come from...\x02\x03",

            "...that material's composition is said to be\x01",
            "impossible to analyze by any known means.\x02\x03",

            "#1610FYet by a miraculous coincidence, the means\x01",
            "by which to process it has been discovered.\x02\x03",

            "Should you wish it, I would be able to use the\x01",
            "facilities of this garden to make a new weapon\x01",
            "for you using that ore.#0C\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #7
        "\x06\x18\x07\x05Make a Weapon Using Zemurian Ore?\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        200,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_BFD"),
        (SWITCH_DEFAULT, "loc_1BF8"),
    )


    label("loc_BFD")

    SetMessageWindowPos(-1, 30, -1, -1)

    AnonymousTalk(    #8
        "\x06\x18\x07\x05Make Which Weapon?\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        120,
        1,
        (
            "Bow - Septenary Bow\x01",                 # 0
            "Templar Sword - Photon Sword\x01",        # 1
            "Staff - Sphere Soleil\x01",               # 2
            "Twin Swords - Serenity Blades\x01",       # 3
            "Whip - Arc en Ciel\x01",                  # 4
            "Orbal Gun - Masquerader\x01",             # 5
            "One-Handed Sword - Divine Nova\x01",      # 6
            "Two-Handed Sword - Dino Fossil\x01",      # 7
            "Orbal Cannon - Meltdown Buster\x01",      # 8
            "Gauntlets - Tetra Monster\x01",           # 9
            "Katana - Houkiboshi\x01",                 # 10
            "Scythe - Nemesis Ripper\x01",             # 11
            "Cancel\x01",                              # 12
        )
    )

    MenuEnd(0x4)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_DBF"),
        (1, "loc_EE0"),
        (2, "loc_1001"),
        (3, "loc_1122"),
        (4, "loc_1243"),
        (5, "loc_1361"),
        (6, "loc_1482"),
        (7, "loc_15A3"),
        (8, "loc_16C4"),
        (9, "loc_17E5"),
        (10, "loc_1906"),
        (11, "loc_1A27"),
        (SWITCH_DEFAULT, "loc_1B48"),
    )


    label("loc_DBF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #9
        "\x07\x05Forged the \x1F\x61\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x561, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #10
        0x22,
        (
            "#1616F#12C#5PGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1BF5")

    label("loc_EE0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #11
        "\x07\x05Forged the \x1F\xBB\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x5BB, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #12
        0x22,
        (
            "#1616F#12C#5PGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1BF5")

    label("loc_1001")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #13
        "\x07\x05Forged the \x1F\xF4\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F4, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #14
        0x22,
        (
            "#1616F#12C#5PGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1BF5")

    label("loc_1122")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #15
        "\x07\x05Forged the \x1F\x24\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x424, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #16
        0x22,
        (
            "#1616F#12C#5PGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1BF5")

    label("loc_1243")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #17
        "\x07\x05Forged the \x1F\x4F\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x44F, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #18
        0x22,
        (
            "#1616F#12C#5PGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF5")

    label("loc_1361")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #19
        "\x07\x05Forged the \x1F\x7F\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x47F, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #20
        0x22,
        (
            "#1616F#12C#5PGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1BF5")

    label("loc_1482")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #21
        "\x07\x05Forged the \x1F\xAD\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x4AD, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #22
        0x22,
        (
            "#1616F#12C#5PGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1BF5")

    label("loc_15A3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #23
        "\x07\x05Forged the \x1F\xD9\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x4D9, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #24
        0x22,
        (
            "#1616F#12C#5PGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1BF5")

    label("loc_16C4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #25
        "\x07\x05Forged the \x1F\x07\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x507, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #26
        0x22,
        (
            "#1616F#12C#5PGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1BF5")

    label("loc_17E5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #27
        "\x07\x05Forged the \x1F\x30\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x530, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #28
        0x22,
        (
            "#1616F#12C#5PGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1BF5")

    label("loc_1906")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x07\x05Forged the \x1F\x89\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x589, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #30
        0x22,
        (
            "#1616F#12C#5PGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1BF5")

    label("loc_1A27")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #31
        "\x07\x05Forged the \x1F\xE0\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x5E0, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #32
        0x22,
        (
            "#1616F#12C#5PGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1BF5")

    label("loc_1B48")

    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #33
        0x22,
        (
            "#1615F#12C#5POh, I see...\x02\x03",

            "#1610FWell, if you change your mind, do come\x01",
            "and let me know.\x02\x03",

            "I'm sure whatever I could make would be\x01",
            "of great help to you.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF5")

    label("loc_1BF5")

    Jump("loc_1CA7")

    label("loc_1BF8")

    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #34
        0x22,
        (
            "#1615F#12C#5POh, I see...\x02\x03",

            "#1610FWell, if you change your mind, do come\x01",
            "and let me know.\x02\x03",

            "I'm sure whatever I could make would be\x01",
            "of great help to you.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA7")

    label("loc_1CA7")

    OP_A2(0x2C36)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-540, 4000, 1460, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, -540, 4000, 1460, 315)
    SetChrPos(0x1, -540, 4000, 1460, 315)
    SetChrPos(0x2, -540, 4000, 1460, 315)
    SetChrPos(0x3, -540, 4000, 1460, 315)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_6_7FE end

    def Function_7_1D7B(): pass

    label("Function_7_1D7B")


    ChrTalk(    #35
        0x22,
        (
            "#1610F#12CWould you like me to make a new weapon for you?\x02\x03",

            "I'd be happy to. Do you have any particular one\x01",
            "in mind?#0C\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 30, -1, -1)

    AnonymousTalk(    #36
        "\x06\x18\x07\x05Make Which Weapon?\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        120,
        1,
        (
            "Bow - Septenary Bow\x01",                 # 0
            "Templar Sword - Photon Sword\x01",        # 1
            "Staff - Sphere Soleil\x01",               # 2
            "Twin Blades - Serenity Blades\x01",       # 3
            "Whip - Arc en Ciel\x01",                  # 4
            "Orbal Gun - Masquerader\x01",             # 5
            "One-Handed Sword - Divine Nova\x01",      # 6
            "Two-Handed Sword - Dino Fossil\x01",      # 7
            "Orbal Cannon - Meltdown Buster\x01",      # 8
            "Gauntlets - Tetra Monster\x01",           # 9
            "Katana - Houkiboshi\x01",                 # 10
            "Scythe - Nemesis Ripper\x01",             # 11
            "Cancel\x01",                              # 12
        )
    )

    MenuEnd(0x4)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_1FC3"),
        (1, "loc_216B"),
        (2, "loc_2313"),
        (3, "loc_24BB"),
        (4, "loc_2663"),
        (5, "loc_280B"),
        (6, "loc_29B3"),
        (7, "loc_2B5B"),
        (8, "loc_2D03"),
        (9, "loc_2EAB"),
        (10, "loc_3053"),
        (11, "loc_31FB"),
        (SWITCH_DEFAULT, "loc_33A3"),
    )


    label("loc_1FC3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #37
        "\x07\x05Forged the \x1F\x61\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x561, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E9")

    ChrTalk(    #38
        0x22,
        (
            "#1616F#12CGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2168")

    label("loc_20E9")


    ChrTalk(    #39
        0x22,
        (
            "#1610F#12CShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2168")

    Jump("loc_3439")

    label("loc_216B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #40
        "\x07\x05Forged the \x1F\xBB\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x5BB, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2291")

    ChrTalk(    #41
        0x22,
        (
            "#1616F#12CGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2310")

    label("loc_2291")


    ChrTalk(    #42
        0x22,
        (
            "#1610F#12CShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2310")

    Jump("loc_3439")

    label("loc_2313")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #43
        "\x07\x05Forged the \x1F\xF4\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F4, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2439")

    ChrTalk(    #44
        0x22,
        (
            "#1616F#12CGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_24B8")

    label("loc_2439")


    ChrTalk(    #45
        0x22,
        (
            "#1610F#12CShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B8")

    Jump("loc_3439")

    label("loc_24BB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #46
        "\x07\x05Forged the \x1F\x24\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x424, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E1")

    ChrTalk(    #47
        0x22,
        (
            "#1616F#12CGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2660")

    label("loc_25E1")


    ChrTalk(    #48
        0x22,
        (
            "#1610F#12CShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2660")

    Jump("loc_3439")

    label("loc_2663")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #49
        "\x07\x05Forged the \x1F\x4F\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x44F, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2789")

    ChrTalk(    #50
        0x22,
        (
            "#1616F#12CGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2808")

    label("loc_2789")


    ChrTalk(    #51
        0x22,
        (
            "#1610F#12CShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2808")

    Jump("loc_3439")

    label("loc_280B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #52
        "\x07\x05Forged the \x1F\x7F\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x47F, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2931")

    ChrTalk(    #53
        0x22,
        (
            "#1616F#12CGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_29B0")

    label("loc_2931")


    ChrTalk(    #54
        0x22,
        (
            "#1610F#12CShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B0")

    Jump("loc_3439")

    label("loc_29B3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #55
        "\x07\x05Forged the \x1F\xAD\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x4AD, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AD9")

    ChrTalk(    #56
        0x22,
        (
            "#1616F#12CGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2B58")

    label("loc_2AD9")


    ChrTalk(    #57
        0x22,
        (
            "#1610F#12CShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B58")

    Jump("loc_3439")

    label("loc_2B5B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #58
        "\x07\x05Forged the \x1F\xD9\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x4D9, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C81")

    ChrTalk(    #59
        0x22,
        (
            "#1616F#12CGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2D00")

    label("loc_2C81")


    ChrTalk(    #60
        0x22,
        (
            "#1610F#12CShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D00")

    Jump("loc_3439")

    label("loc_2D03")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #61
        "\x07\x05Forged the \x1F\x07\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x507, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E29")

    ChrTalk(    #62
        0x22,
        (
            "#1616F#12CGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2EA8")

    label("loc_2E29")


    ChrTalk(    #63
        0x22,
        (
            "#1610F#12CShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA8")

    Jump("loc_3439")

    label("loc_2EAB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #64
        "\x07\x05Forged the \x1F\x30\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x530, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD1")

    ChrTalk(    #65
        0x22,
        (
            "#1616F#12CGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_3050")

    label("loc_2FD1")


    ChrTalk(    #66
        0x22,
        (
            "#1610F#12CShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3050")

    Jump("loc_3439")

    label("loc_3053")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #67
        "\x07\x05Forged the \x1F\x89\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x589, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3179")

    ChrTalk(    #68
        0x22,
        (
            "#1616F#12CGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_31F8")

    label("loc_3179")


    ChrTalk(    #69
        0x22,
        (
            "#1610F#12CShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F8")

    Jump("loc_3439")

    label("loc_31FB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #70
        "\x07\x05Forged the \x1F\xE0\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x5E0, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3321")

    ChrTalk(    #71
        0x22,
        (
            "#1616F#12CGood! I'm glad the process went successfully.\x02\x03",

            "#1611FShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_33A0")

    label("loc_3321")


    ChrTalk(    #72
        0x22,
        (
            "#1610F#12CShould you find any more of that ore, bring it\x01",
            "to me right away.\x02\x03",

            "I'd be happy to make a new weapon for you.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33A0")

    Jump("loc_3439")

    label("loc_33A3")

    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #73
        0x22,
        (
            "#1610F#12CWell, if you change your mind, do come\x01",
            "and let me know.\x02\x03",

            "I'm sure whatever I could make would be\x01",
            "of great help to you.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3439")

    label("loc_3439")

    Return()

    # Function_7_1D7B end

    def Function_8_343A(): pass

    label("Function_8_343A")


    ChrTalk(    #74
        0x22,
        (
            "#1611F#12CHeehee. Renne gave me quite the surprise\x01",
            "when she summoned her friend.\x02\x03",

            "#1610FStill, while it may have been possible to do so,\x01",
            "unexpected actions like that in this world take\x01",
            "a serious toll on you mentally and physically.\x02\x03",

            "#1616FI would suggest not doing things like that any\x01",
            "more than you have to.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37CE")

    ChrTalk(    #75
        0x110,
        (
            "#268F*sigh* Well, okay...\x02\x03",

            "#267FI'm satisfied as long as I have Pater-Mater,\x01",
            "anyway, so I've got no reason to.\x02\x03",

            "#260FSo I suppose I can do what I'm told this once.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36B2")

    ChrTalk(    #76
        0x105,
        (
            "#1165F(Not many people have the experience of being\x01",
            "told off by someone who lived over a thousand\x01",
            "years ago.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A4")

    label("loc_36B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_372E")

    ChrTalk(    #77
        0x101,
        (
            "#1016F(Ahaha. Not often you can say you were scolded\x01",
            "by someone who lived over a thousand years ago.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A4")

    label("loc_372E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37A4")

    ChrTalk(    #78
        0x109,
        (
            "#1077F(Haha... Not many people get to be scolded by \x01",
            "someone who lived over a thousand years ago.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A4")


    ChrTalk(    #79
        0x22,
        "#1611F#12CI'm happy to hear that.#0C\x02",
    )

    CloseMessageWindow()

    label("loc_37CE")

    OP_A2(0x2657)
    Return()

    # Function_8_343A end

    def Function_9_37D2(): pass

    label("Function_9_37D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37E8")
    Call(5, 8)
    Jump("loc_3853")

    label("loc_37E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_382A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37FE")
    Call(5, 2)
    Jump("loc_3827")

    label("loc_37FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3823")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_381C")
    Call(5, 6)
    Jump("loc_3820")

    label("loc_381C")

    Call(5, 5)

    label("loc_3820")

    Jump("loc_3827")

    label("loc_3823")

    Call(5, 3)

    label("loc_3827")

    Jump("loc_3853")

    label("loc_382A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_384F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3848")
    Call(5, 6)
    Jump("loc_384C")

    label("loc_3848")

    Call(5, 4)

    label("loc_384C")

    Jump("loc_3853")

    label("loc_384F")

    Call(5, 10)

    label("loc_3853")

    TalkEnd(0xFE)
    Return()

    # Function_9_37D2 end

    def Function_10_3857(): pass

    label("Function_10_3857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_3A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C1")
    OP_A2(0x3)

    ChrTalk(    #80
        0x22,
        (
            "#1616F#12C...It's been too long since I last felt this place\x01",
            "was brimming with life.\x02\x03",

            "It's interesting that there should be sixteen of\x01",
            "you, too.\x02\x03",

            "#1611FAfter all, there were sixteen central members in\x01",
            "our group back when we were working to seal the\x01",
            "Aureole.\x02\x03",

            "I wonder if this is a coincidence, or maybe even\x01",
            "the will of the Goddess?#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A62")

    label("loc_39C1")


    ChrTalk(    #81
        0x22,
        (
            "#1616F#12CAs soon as you're ready to go, come and let me\x01",
            "know.\x02\x03",

            "#1611FI intend to use the garden's power to aid you in\x01",
            "making the white wings fly again.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A62")

    Jump("loc_5427")

    label("loc_3A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_3D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD3")

    ChrTalk(    #82
        0x22,
        (
            "#1615F#12CThe final barrier that's stopping you has disappeared\x01",
            "from what I can tell.\x02\x03",

            "#1613FHowever, I'm afraid I'm unable to ascertain anything\x01",
            "about the area beyond it...\x02\x03",

            "I couldn't tell you why...#0C\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_END)), "loc_3BD0")

    ChrTalk(    #83
        0x109,
        (
            "#1060FI think Ries is the key to passing through there.\x02\x03",

            "#1075FIt's worth a try, anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BD0")

    ChrTalk(    #84
        0x10F,
        "#1802F...\x02",
    )

    CloseMessageWindow()

    label("loc_3BD0")

    Jump("loc_3BE9")

    label("loc_3BD3")


    ChrTalk(    #85
        0x22,
        "#1613F#12C...#0C\x02",
    )

    CloseMessageWindow()

    label("loc_3BE9")

    OP_A2(0x3)
    Jump("loc_3D64")

    label("loc_3BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CAE")

    ChrTalk(    #86
        0x22,
        (
            "#1615F#12CI'm afraid I'm unable to ascertain anything about\x01",
            "the next area...\x02\x03",

            "#1613FPerhaps it, too, needs some sort of key in order\x01",
            "to step inside.#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x109,
        "#1067F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D4B")

    label("loc_3CAE")


    ChrTalk(    #88
        0x22,
        (
            "#1615F#12CI'm afraid I'm unable to ascertain anything about\x01",
            "the next area...\x02\x03",

            "#1613FPerhaps it, too, needs some sort of key in order\x01",
            "to step inside.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D4B")

    Jump("loc_3D64")

    label("loc_3D4E")


    ChrTalk(    #89
        0x22,
        "#1613F#12C...#0C\x02",
    )

    CloseMessageWindow()

    label("loc_3D64")

    Jump("loc_5427")

    label("loc_3D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_4109")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E3F")

    ChrTalk(    #90
        0x22,
        (
            "#1615F#12CSo the time has finally come to enter the last\x01",
            "part of this plane...\x02\x03",

            "I can sense something truly terrifying from the\x01",
            "other side of the gate.\x02\x03",

            "#1612FI beg you: be careful.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FC7")

    label("loc_3E3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EA1")
    TurnDirection(0x22, 0x102, 0)

    ChrTalk(    #91
        0x22,
        (
            "#1613F#12C...\x02\x03",

            "#1610FI beg you: be careful.#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x102,
        "#1500F...I will.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FC7")

    label("loc_3EA1")


    ChrTalk(    #93
        0x22,
        "#1613F#12CYou need an orphan of a lost village, yes?#0C\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x109,
        "#1063FI think Joshua's up, then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F21")

    ChrTalk(    #95
        0x101,
        "#1002F...\x02",
    )

    CloseMessageWindow()

    label("loc_3F21")


    ChrTalk(    #96
        0x22,
        (
            "#1615F#12CThe key to the nohval gate is near the spring.\x02\x03",

            "#1612FHe seems to be ready to depart at any time, too.\x01",
            "So please let him know when you require him.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FC7")

    OP_A2(0x3)
    Jump("loc_4106")

    label("loc_3FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_405D")

    ChrTalk(    #97
        0x22,
        (
            "#1612F#12CThe next area should be the last of the sixth\x01",
            "plane's trials.\x02\x03",

            "#1613FBut within is...#0C\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_405A")

    ChrTalk(    #98
        0x102,
        "#1503F...\x02",
    )

    CloseMessageWindow()

    label("loc_405A")

    Jump("loc_4106")

    label("loc_405D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4097")

    ChrTalk(    #99
        0x22,
        "#1610F#12CI beg you: be careful.#0C\x02",
    )

    CloseMessageWindow()
    Jump("loc_4106")

    label("loc_4097")


    ChrTalk(    #100
        0x22,
        (
            "#1615F#12CThe key to the nohval gate is near the spring.\x02\x03",

            "#1613FHe seems to be ready to depart, too...#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4106")

    Jump("loc_5427")

    label("loc_4109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_45A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41AE")

    ChrTalk(    #101
        0x22,
        (
            "#1613F#12C...\x02\x03",

            "It's gradual, but the Lord of Phantasma's power\x01",
            "is growing ever greater the more time passes.\x02\x03",

            "#1612FPlease, hurry.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43AF")

    label("loc_41AE")


    ChrTalk(    #102
        0x22,
        (
            "#1610F#12CIn order to pass through the carnelia gate, you will\x01",
            "need the Divine Blade's successor.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_432B")

    ChrTalk(    #103
        0x10C,
        "#115FIn other words, me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x22,
        (
            "#1615F#12CI believe so.\x02\x03",

            "#1610FThe Lord of Phantasma appears to be creating the\x01",
            "trials you face from your feelings and memories.\x02\x03",

            "I can only ask that you are careful--the greatest\x01",
            "challenges are clearly still to come.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43AF")

    label("loc_432B")


    ChrTalk(    #105
        0x109,
        "#1060FRichard, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x22,
        (
            "#1616F#12CIndeed. I believe him to be over on the plateau.\x02\x03",

            "#1610FPlease, go and speak with him.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43AF")

    OP_A2(0x3)
    Jump("loc_45A1")

    label("loc_43B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_444C")

    ChrTalk(    #107
        0x22,
        (
            "#1615F#12CThe majority of my power is dedicated to the\x01",
            "preservation of this garden...\x02\x03",

            "...but at this rate...\x02\x03",

            "#1610FPlease, hurry.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A1")

    label("loc_444C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44E1")

    ChrTalk(    #108
        0x22,
        (
            "#1613F#12CThe trial on the other side of the carnelia gate\x01",
            "is bound to be challenging...\x02\x03",

            "#1610F...but I wish you all luck.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A1")

    label("loc_44E1")


    ChrTalk(    #109
        0x22,
        (
            "#1610F#12CIn order to pass through the carnelia gate, you will\x01",
            "need the Divine Blade's successor.\x02\x03",

            "#1616FHe appears to be on the plateau at the moment.\x02\x03",

            "Please, go and speak with him.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45A1")

    Jump("loc_5427")

    label("loc_45A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_4CAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4731")

    ChrTalk(    #110
        0x22,
        (
            "#1610F#12CI've confirmed the existence of four gates so far.\x02\x03",

            "Each of them leads to another area created by\x01",
            "the Lord of Phantasma.\x02\x03",

            "#1613F...\x02\x03",

            "Beyond those is another area, but I'm afraid\x01",
            "no matter how hard I try, I can't learn a thing\x01",
            "about it.\x02\x03",

            "#1615FI fear only you'll be able to tear down the wall\x01",
            "blocking access to it to find out what is on the\x01",
            "other side.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49BF")

    label("loc_4731")


    ChrTalk(    #111
        0x22,
        (
            "#1610F#12CIf you want to pass through the amberl gate,\x01",
            "you're going to need the sword-wielding dame,\x01",
            "it seems.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_490C")

    ChrTalk(    #112
        0x10A,
        "#814FUmm... And that's me, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x22,
        (
            "#1610F#12CIndeed.\x02\x03",

            "#1615FOn the other side of the last monument was an area\x01",
            "created by the Lord of Phantasma.\x02\x03",

            "Seeing as the last one was based on your memories,\x01",
            "it's very possible that there will be something similar\x01",
            "on the other side of this one, too.\x02\x03",

            "#1610FEither way, please do be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49BF")

    label("loc_490C")


    ChrTalk(    #114
        0x109,
        "#1060FThat's Anelace, right?#0C\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x22,
        (
            "#1610F#12CCorrect.\x02\x03",

            "#1616FI believe she's near the big tree at the moment.\x02\x03",

            "#1610FI'm sure she'll be happy to go with you if you ask.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49BF")

    OP_A2(0x3)
    Jump("loc_4CA7")

    label("loc_49C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB8")

    ChrTalk(    #116
        0x22,
        (
            "#1610F#12CI've confirmed the existence of four gates so far.\x02\x03",

            "Each of them will require a different member of\x01",
            "your group in order to gain access.\x02\x03",

            "#1615FIn short, you'll all need to work as one in order\x01",
            "to get through them.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CA7")

    label("loc_4AB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BC0")

    ChrTalk(    #117
        0x22,
        (
            "#1612F#12COn the other side of the last monument was an area\x01",
            "created by the Lord of Phantasma.\x02\x03",

            "Seeing as the last one was based on your memories,\x01",
            "it's very possible that there will be something similar\x01",
            "on the other side of this one, too.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CA7")

    label("loc_4BC0")


    ChrTalk(    #118
        0x22,
        (
            "#1610F#12CIf you want to pass through the amberl gate,\x01",
            "you're going to need the sword-wielding dame,\x01",
            "it seems.#0C\x02\x03",

            "#1616FI believe she's near the big tree at the moment.\x02\x03",

            "I'm sure she'll be happy to go with you if you ask.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CA7")

    Jump("loc_5427")

    label("loc_4CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_5427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5106")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D8A")

    ChrTalk(    #119
        0x22,
        (
            "#1615F#12CI myself am but a shadow bound by the laws of\x01",
            "Phantasma.\x02\x03",

            "As such, I'm afraid I'm limited in what I can do.\x02\x03",

            "#1610FBut I'll be sure to do all I can to support you in\x01",
            "your efforts.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5100")

    label("loc_4D8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F7A")

    ChrTalk(    #120
        0x22,
        (
            "#1615F#12CIt seems as though passing through the gates\x01",
            "created by the Lord of Phantasma requires you\x01",
            "to have a specific person accompanying you.\x02\x03",

            "#1612FIn the case of the sapphirl gate, that is the\x01",
            "'white wings.'#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x105,
        "#1167F...Which refers to me, doesn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x22,
        (
            "#1613F#12CI believe so.\x02\x03",

            "#1612FAs it stands, rules established by the Lord of\x01",
            "Phantasma are absolute in this world.\x02\x03",

            "So I fear that if you wish to proceed, you will\x01",
            "have little choice but to follow them.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5100")

    label("loc_4F7A")


    ChrTalk(    #123
        0x22,
        (
            "#1615F#12CIt seems as though passing through the gates\x01",
            "created by the Lord of Phantasma requires you\x01",
            "to have a specific person accompanying you.\x02\x03",

            "In the case of the sapphirl gate, that is the\x01",
            "'white wings.'#0C#4350W #20W \x01",
            "#1612FThat most likely refers to my descendant.\x02\x03",

            "#1610FShe's over in the library at the moment.\x01",
            "I'm sure she would be happy to accompany\x01",
            "you if you went and spoke to her.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5100")

    OP_A2(0x3)
    Jump("loc_5427")

    label("loc_5106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51FF")

    ChrTalk(    #124
        0x22,
        (
            "#1610F#12CI, too, am bound by the laws of Phantasma,\x01",
            "so I'm limited in what I can do to support you...\x02\x03",

            "...but know that I will do so in every way that\x01",
            "I can.\x02\x03",

            "#1611FIf there's anything I can do to assist you,\x01",
            "please let me know.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5427")

    label("loc_51FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52FE")

    ChrTalk(    #125
        0x22,
        (
            "#1615F#12CIn order to pass through the sapphirl gate,\x01",
            "you will need my descendant accompanying\x01",
            "you.\x02\x03",

            "#1612FThere are also likely to be a number of ordeals\x01",
            "awaiting you on the other side as well.\x02\x03",

            "Please, be prepared for anything.#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5427")

    label("loc_52FE")


    ChrTalk(    #126
        0x22,
        (
            "#1615F#12CIn order to pass through the sapphirl gate,\x01",
            "you will need my descendant accompanying\x01",
            "you.\x02\x03",

            "#1610FI believe she's over in the library at the moment.\x02\x03",

            "I've already explained the situation to her,\x01",
            "so I'm sure she will be more than happy to\x01",
            "accompany you if you go and speak to her.#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5427")

    Return()

    # Function_10_3857 end

    def Function_11_5428(): pass

    label("Function_11_5428")


    ChrTalk(    #127
        0x22,
        (
            "#1613F#12COnce you depart on board the Arseille,\x01",
            "there will be no turning back.\x02\x03",

            "You will never be able to return to this garden\x01",
            "again.\x02\x03",

            "#1612FAre you completely sure that you are ready?#0C\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5508")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56D2")

    Menu(
        2,
        -1,
        150,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x4)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_554B"),
        (SWITCH_DEFAULT, "loc_56C2"),
    )


    label("loc_554B")

    EventBegin(0x0)
    EventBegin(0x0)
    Fade(500)
    OP_6D(-900, 4000, 4220, 0)
    OP_67(0, 5450, -10000, 0)
    OP_6B(2120, 0)
    OP_6C(0, 0)
    OP_6E(410, 0)
    SetChrPos(0x0, -1040, 4000, 1270, 315)
    SetChrPos(0x1, -40, 4000, 2200, 315)
    SetChrPos(0x2, -110, 4000, -250, 315)
    SetChrPos(0x3, 870, 4000, 1110, 315)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_8C(0x22, 135, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #128
        0x22,
        (
            "#1616F#5P#12C...Very well, then.\x02\x03",

            "#1610FIn that case, let's call the others and leave\x01",
            "for the Arseille at once.#0C\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5688():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5688)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/M7002   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_56CF")

    label("loc_56C2")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_56CF")

    label("loc_56CF")

    Jump("loc_5508")

    label("loc_56D2")

    Return()

    # Function_11_5428 end

    def Function_12_56D3(): pass

    label("Function_12_56D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 0)), scpexpr(EXPR_END)), "loc_57E0")

    ChrTalk(    #129
        0x21,
        (
            "#1065FWe've only got one chance to get out of\x01",
            "here safely. We can't blow it.\x02\x03",

            "#1063FSo let's make sure we've done everything\x01",
            "we need to before taking off from here.\x02\x03",

            "#1062FAs long as we're absolutely sure we've done\x01",
            "all we can do, we'll be just fine!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_597C")

    label("loc_57E0")

    SetChrSubChip(0xFE, 0)

    ChrTalk(    #130
        0x21,
        (
            "#1065FYou guys have stuck with me through all that's\x01",
            "happened here.\x02\x03",

            "#1067FEven after finding out it was all my fault, you\x01",
            "stuck by me and even agreed to keep helping.\x02\x03",

            "#1063FSo I've got something I really wanna say to you\x01",
            "all...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    ChrTalk(    #131
        0x21,
        (
            "#1062F...but it can wait until we all get the hell out of\x01",
            "here.\x02\x03",

            "#1061FI'll keep it to myself until then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5979")

    ChrTalk(    #132
        0x10F,
        "#1952F...Right!\x02",
    )

    CloseMessageWindow()

    label("loc_5979")

    OP_A2(0x2658)

    label("loc_597C")

    TalkEnd(0xFE)
    Return()

    # Function_12_56D3 end

    def Function_13_5980(): pass

    label("Function_13_5980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_5BAB")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AAD")

    ChrTalk(    #133
        0x16,
        (
            "#1164FHi there.\x02\x03",

            "#1160FWe're just about in a state where we can get\x01",
            "the Arseille moving once we're ready.\x02\x03",

            "#1382FBut we aren't going to be able to resupply once\x01",
            "we depart, as I'm sure you well know.\x02\x03",

            "Make sure you're well rested and ready before\x01",
            "giving the word to leave.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_5BA8")

    label("loc_5AAD")


    ChrTalk(    #134
        0x16,
        (
            "#1160FAs I'm sure you well know, we aren't going to be\x01",
            "able to resupply once we depart on the Arseille.\x02\x03",

            "#1382FThere's no telling what we could encounter on our\x01",
            "way to where the Lord of Phantasma awaits, either,\x01",
            "so be sure to rest while you can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BA8")

    TalkEnd(0xFE)

    label("loc_5BAB")

    Return()

    # Function_13_5980 end

    def Function_14_5BAC(): pass

    label("Function_14_5BAC")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E7C")
    EventBegin(0x0)
    Fade(500)
    OP_6D(5480, 4000, -8340, 0)
    OP_67(0, 6420, -10000, 0)
    OP_6B(2180, 0)
    OP_6C(315000, 0)
    OP_6E(400, 0)
    SetChrPos(0x109, 6530, 4000, -9150, 180)
    SetChrPos(0xEF, 7370, 4000, -7880, 180)
    SetChrPos(0xF0, 5500, 4000, -7630, 180)
    SetChrPos(0xF1, 6290, 4000, -6550, 180)
    OP_8C(0x1A, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #135
        0x1A,
        "#814FOh, 'sup? Anything wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x109,
        "#1060FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #137
        (
            "\x07\x05Kevin explained to Anelace that they thought she was the person the amberl\x01",
            "monument's inscription was asking for.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #138
        0x1A,
        (
            "#1317FMe? The 'sword-wielding dame'?\x02\x03",

            "#819FI dunnooo... I mean, it's a cool-sounding title\x01",
            "and all, but does it really fit me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x109,
        (
            "#1077FIt does if you ask me. But hey, even if you're\x01",
            "not sure, it's worth a try, right?\x02\x03",

            "#1078FDo you mind coming with us and giving it a go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x1A,
        (
            "#810FYou got it.\x02\x03",

            "#1310FOff we go, then!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B0B)
    Sleep(300)
    EventEnd(0x0)
    Jump("loc_5E9F")

    label("loc_5E7C")


    ChrTalk(    #141
        0x1A,
        "#810F◆Normal message display\x02",
    )

    CloseMessageWindow()

    label("loc_5E9F")

    TalkEnd(0x1A)
    Return()

    # Function_14_5BAC end

    def Function_15_5EA3(): pass

    label("Function_15_5EA3")

    Return()

    # Function_15_5EA3 end

    def Function_16_5EA4(): pass

    label("Function_16_5EA4")

    Return()

    # Function_16_5EA4 end

    def Function_17_5EA5(): pass

    label("Function_17_5EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_6301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61E6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6045")
    TalkBegin(0xFE)

    ChrTalk(    #142
        0x12,
        (
            "#170FI will be here going over the steps we'll need to\x01",
            "go through before the Arseille is ready.\x02\x03",

            "#176FI can't foresee any major problems getting it to\x01",
            "move again, but I will admit that not having any\x01",
            "of its regular crew makes me uneasy.\x02\x03",

            "#178FStill, that makes my responsibility as its captain\x01",
            "all the more important--and I will not let you all\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_61E0")

    label("loc_6045")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #143
        0x12,
        (
            "#176FThat's a valid point. I don't think we can\x01",
            "discount the possibility there may be foes\x01",
            "inside the Arseille.\x02\x03",

            "#178FAfter reaching there, Major Vander and\x01",
            "I will assess the situation before the rest\x01",
            "us step inside.\x02\x03",

            "Once those checks are complete, we'll check\x01",
            "the state of the main engines before\x01",
            "attempting to activate the ship itself.\x02\x03",

            "#179FAs for the personnel on the bridge... Hmm...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_61E0")

    OP_A2(0x4)
    Jump("loc_6301")

    label("loc_61E6")

    TalkBegin(0xFE)

    ChrTalk(    #144
        0x12,
        (
            "#170FWe shouldn't face any major obstacles in\x01",
            "getting the Arseille up and running.\x02\x03",

            "#176FStill, we will be heading into completely \x01",
            "unfamiliar territory by journeying outside\x01",
            "the planes. Anything could await us.\x02\x03",

            "#178FBe sure that you are fully prepared before\x01",
            "we depart.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_6301")

    Return()

    # Function_17_5EA5 end

    def Function_18_6302(): pass

    label("Function_18_6302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_6459")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63EA")

    ChrTalk(    #145
        0x13,
        (
            "#272FSo the Lord of Phantasma is Rufina Argent...\x02\x03",

            "Her negotiation and problem-solving abilities\x01",
            "were highly regarded in life...\x02\x03",

            "#276F...but that probably just makes her all the more\x01",
            "deadly as our foe.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_6456")

    label("loc_63EA")


    ChrTalk(    #146
        0x13,
        (
            "#278FI don't think I can afford to rest on my laurels.\x01",
            "I should do some more training before we leave.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6456")

    TalkEnd(0xFE)

    label("loc_6459")

    Return()

    # Function_18_6302 end

    def Function_19_645A(): pass

    label("Function_19_645A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x27023E, 0x270248, 0x13)
    OP_D2(0x270244, 0x27024E, 0x14)
    OP_D2(0x270022, 0x270025, 0x15)
    LoadEffect(0x0, "map\\mp252_04.eff")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64EC")
    SetChrPos(0xF1, 1660, 4000, 480, 180)
    SetChrPos(0xF0, -10, 4000, 730, 180)
    SetChrPos(0xEF, 1450, 4000, 2260, 180)
    SetChrPos(0xEE, -70, 4000, 2280, 180)
    Jump("loc_65E8")

    label("loc_64EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6541")
    SetChrPos(0xF1, 1660, 4000, 480, 180)
    SetChrPos(0xF0, -10, 4000, 730, 180)
    SetChrPos(0xEE, 1450, 4000, 2260, 180)
    SetChrPos(0xEF, -70, 4000, 2280, 180)
    Jump("loc_65E8")

    label("loc_6541")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6596")
    SetChrPos(0xF1, 1660, 4000, 480, 180)
    SetChrPos(0xEF, -10, 4000, 730, 180)
    SetChrPos(0xEE, 1450, 4000, 2260, 180)
    SetChrPos(0xF0, -70, 4000, 2280, 180)
    Jump("loc_65E8")

    label("loc_6596")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65E8")
    SetChrPos(0xF0, 1660, 4000, 480, 180)
    SetChrPos(0xEF, -10, 4000, 730, 180)
    SetChrPos(0xEE, 1450, 4000, 2260, 180)
    SetChrPos(0xF1, -70, 4000, 2280, 180)

    label("loc_65E8")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-1200, 4000, 3500, 0)
    OP_67(0, 6250, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(432, 0)

    def lambda_6657():
        OP_6B(2100, 6000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_6657)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66B1")
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xF1, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xF0, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xEF, 0x0, 0x5, 0x15)
    Sleep(4000)
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xEE, 0x0, 0x5, 0x15)
    Jump("loc_6780")

    label("loc_66B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66F7")
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xF1, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xF0, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xEE, 0x0, 0x5, 0x15)
    Sleep(4000)
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xEF, 0x0, 0x5, 0x15)
    Jump("loc_6780")

    label("loc_66F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_673D")
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xF1, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xEF, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xEE, 0x0, 0x5, 0x15)
    Sleep(4000)
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xF0, 0x0, 0x5, 0x15)
    Jump("loc_6780")

    label("loc_673D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6780")
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xF0, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xEF, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xEE, 0x0, 0x5, 0x15)
    Sleep(2000)
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xF1, 0x0, 0x5, 0x15)

    label("loc_6780")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(1000)
    WaitChrThread(0x22, 0x0)

    ChrTalk(    #147
        0x22,
        "\x07\x0C#1610F#5PWelcome back, everyone.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_62(0x110, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    ChrTalk(    #148
        0x110,
        "#268F#2P*sigh*\x02",
    )

    CloseMessageWindow()
    OP_62(0x110, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6840")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_68A7")

    label("loc_6840")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6868")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_68A7")

    label("loc_6868")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6890")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_68A7")

    label("loc_6890")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_68A7")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68D4")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_693B")

    label("loc_68D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68FC")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_693B")

    label("loc_68FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6924")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_693B")

    label("loc_6924")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_693B")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6968")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_69CF")

    label("loc_6968")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6990")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_69CF")

    label("loc_6990")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69B8")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_69CF")

    label("loc_69B8")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_69CF")

    Sleep(1000)
    Jump("loc_6F3B")

    label("loc_69D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BA4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A0D")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6A74")

    label("loc_6A0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A35")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6A74")

    label("loc_6A35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A5D")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6A74")

    label("loc_6A5D")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6A74")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AA1")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6B08")

    label("loc_6AA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AC9")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6B08")

    label("loc_6AC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AF1")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6B08")

    label("loc_6AF1")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6B08")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B35")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6B9C")

    label("loc_6B35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B5D")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6B9C")

    label("loc_6B5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B85")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6B9C")

    label("loc_6B85")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6B9C")

    Sleep(1000)
    Jump("loc_6F3B")

    label("loc_6BA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BDA")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6C41")

    label("loc_6BDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C02")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6C41")

    label("loc_6C02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C2A")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6C41")

    label("loc_6C2A")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6C41")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C6E")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6CD5")

    label("loc_6C6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C96")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6CD5")

    label("loc_6C96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CBE")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6CD5")

    label("loc_6CBE")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6CD5")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D02")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6D69")

    label("loc_6D02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D2A")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6D69")

    label("loc_6D2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D52")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6D69")

    label("loc_6D52")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6D69")

    Sleep(1000)
    Jump("loc_6F3B")

    label("loc_6D71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F3B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DA7")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6E0E")

    label("loc_6DA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DCF")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6E0E")

    label("loc_6DCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DF7")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6E0E")

    label("loc_6DF7")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6E0E")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E3B")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6EA2")

    label("loc_6E3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E63")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6EA2")

    label("loc_6E63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E8B")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6EA2")

    label("loc_6E8B")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6EA2")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6ECF")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6F36")

    label("loc_6ECF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EF7")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6F36")

    label("loc_6EF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F1F")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6F36")

    label("loc_6F1F")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6F36")

    Sleep(1000)

    label("loc_6F3B")


    def lambda_6F41():
        OP_6D(-600, 4000, 2600, 1500)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_6F41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F91")

    def lambda_6F67():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6F67)
    Sleep(100)

    def lambda_6F7A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_6F7A)
    Sleep(100)
    OP_8C(0xF1, 315, 400)
    Jump("loc_7048")

    label("loc_6F91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FCF")

    def lambda_6FA5():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_6FA5)
    Sleep(100)

    def lambda_6FB8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_6FB8)
    Sleep(100)
    OP_8C(0xF1, 315, 400)
    Jump("loc_7048")

    label("loc_6FCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_700D")

    def lambda_6FE3():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_6FE3)
    Sleep(100)

    def lambda_6FF6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6FF6)
    Sleep(100)
    OP_8C(0xF1, 315, 400)
    Jump("loc_7048")

    label("loc_700D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7048")

    def lambda_7021():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_7021)
    Sleep(100)

    def lambda_7034():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_7034)
    Sleep(100)
    OP_8C(0xF0, 315, 400)

    label("loc_7048")

    WaitChrThread(0x22, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70FC")

    ChrTalk(    #149
        0x109,
        (
            "#1064FYou okay, Renne?\x02\x03",

            "#1066FIf you're feeling tired, why don't you rest here\x01",
            "in the garden for a bit?\x02\x03",

            "All the others are here--you wouldn't be alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E9")

    label("loc_70FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_716D")

    ChrTalk(    #150
        0x101,
        (
            "#1004FYou okay, Renne?\x02\x03",

            "#1015FWe can stop here and rest for a bit if you're\x01",
            "feeling tired.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E9")

    label("loc_716D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_720D")

    ChrTalk(    #151
        0x107,
        (
            "#064FUmm... Are you feeling tired, Renne?\x02\x03",

            "#062FMaybe we should stop and rest for a bit?\x02\x03",

            "There's no shame in admitting you need a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E9")

    label("loc_720D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72A6")

    ChrTalk(    #152
        0x102,
        (
            "#1504FAre you feeling tired, Renne?\x02\x03",

            "#1503FDo you want to stop and rest for a while?\x01",
            "There's a rest area in front of the fountain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E9")

    label("loc_72A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_7351")

    ChrTalk(    #153
        0x10F,
        (
            "#1938FIf you're feeling tired, you'd be well advised\x01",
            "to rest for a while.\x02\x03",

            "#1937FNothing good comes from pushing your body\x01",
            "beyond its limits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73E4")

    label("loc_7351")


    ChrTalk(    #154
        0x10F,
        (
            "#1440FIf you're feeling tired, you'd be well advised\x01",
            "to rest for a while.\x02\x03",

            "#1446FNothing good comes from pushing your body\x01",
            "beyond its limits.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73E4")

    Jump("loc_77E9")

    label("loc_73E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7464")

    ChrTalk(    #155
        0x105,
        (
            "#1382FUmm... Should we rest a while if you're tired?\x02\x03",

            "#1165FI'd be happy to make some tea if you want.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E9")

    label("loc_7464")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74E5")

    ChrTalk(    #156
        0x10A,
        (
            "#814FUmm... Are you feeling tired, Renne?\x02\x03",

            "#819FHeehee. Why don't we stop and rest\x01",
            "here for a while, then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E9")

    label("loc_74E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7550")

    ChrTalk(    #157
        0x10B,
        (
            "#213FUmm... Are you feeling tired?\x02\x03",

            "#210FWhy don't we take a break over there,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E9")

    label("loc_7550")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75CB")

    ChrTalk(    #158
        0x106,
        (
            "#052F...You feelin' tired?\x02\x03",

            "#053FGo rest, then. No good comes from kids pushing\x01",
            "themselves too hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E9")

    label("loc_75CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7674")

    ChrTalk(    #159
        0x10C,
        (
            "#115FIf you feel tired, you should rest, Renne.\x02\x03",

            "#110FYou're an important member of the team--\x01",
            "we want you to be in the best condition you\x01",
            "can be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E9")

    label("loc_7674")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76E3")

    ChrTalk(    #160
        0x103,
        (
            "#1523FOh, you feeling tired?\x02\x03",

            "#1520FMaybe you should go sit down\x01",
            "in the rest area, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E9")

    label("loc_76E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_776B")

    ChrTalk(    #161
        0x10D,
        (
            "#272FIf you're feeling tired, you should go and rest.\x02\x03",

            "We don't want your judgment impaired when\x01",
            "we need it most.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E9")

    label("loc_776B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77E9")

    ChrTalk(    #162
        0x10E,
        (
            "#176FAre you feeling tired, Renne?\x02\x03",

            "#170FPerhaps you should spend some time in the rest\x01",
            "area recuperating?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77E9")

    OP_63(0x110)
    Sleep(150)
    OP_8C(0x110, 135, 400)

    ChrTalk(    #163
        0x110,
        (
            "#266F#5PI'm not tired at all!\x02\x03",

            "#267FI've just got something on my mind.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7884")

    ChrTalk(    #164
        0x101,
        "#1011FSomething on your mind? Like what?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A9E")

    label("loc_7884")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_78AC")

    ChrTalk(    #165
        0x10F,
        "#1930F...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_78BC")

    label("loc_78AC")


    ChrTalk(    #166
        0x10F,
        "#1440F...?\x02",
    )

    CloseMessageWindow()

    label("loc_78BC")

    Jump("loc_7A9E")

    label("loc_78BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78F7")

    ChrTalk(    #167
        0x104,
        "#1543FOh? And what might that be?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A9E")

    label("loc_78F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_792D")

    ChrTalk(    #168
        0x108,
        "#072FHmm... What might that be?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A9E")

    label("loc_792D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_796D")

    ChrTalk(    #169
        0x109,
        (
            "#1064FSomething on your mind?\x02\x03",

            "Like what?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A9E")

    label("loc_796D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79A0")

    ChrTalk(    #170
        0x10E,
        "#172FSomething on your mind?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A9E")

    label("loc_79A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79C0")

    ChrTalk(    #171
        0x10D,
        "#270FHmm?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A9E")

    label("loc_79C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79EB")

    ChrTalk(    #172
        0x103,
        "#1522FOh? Like what?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A9E")

    label("loc_79EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A0E")

    ChrTalk(    #173
        0x10B,
        "#213F...Huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A9E")

    label("loc_7A0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A30")

    ChrTalk(    #174
        0x10A,
        "#814FUmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A9E")

    label("loc_7A30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A53")

    ChrTalk(    #175
        0x105,
        "#1164FUmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A9E")

    label("loc_7A53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A74")

    ChrTalk(    #176
        0x106,
        "#555FUh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A9E")

    label("loc_7A74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A9E")

    ChrTalk(    #177
        0x107,
        "#564FUmm... Like what?\x02",
    )

    CloseMessageWindow()

    label("loc_7A9E")

    OP_62(0x110, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x110)
    Sleep(150)

    ChrTalk(    #178
        0x110,
        (
            "#263F#5PHmm... Well, I suppose it can't hurt.\x02\x03",

            "#269FLet me give it a try.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_7B17():
        OP_6D(-3580, 4000, 3190, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_7B17)

    def lambda_7B2F():
        OP_67(0, 6380, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_7B2F)

    def lambda_7B47():
        OP_6B(2270, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_7B47)

    def lambda_7B57():
        OP_6C(326000, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_7B57)

    def lambda_7B67():
        OP_6E(419, 2000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_7B67)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BCD")
    OP_43(0xEE, 0x0, 0x5, 0x14)

    def lambda_7B8C():

        label("loc_7B8C")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7B8C")

    QueueWorkItem2(0x22, 0, lambda_7B8C)

    def lambda_7B9D():

        label("loc_7B9D")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7B9D")

    QueueWorkItem2(0xEF, 0, lambda_7B9D)

    def lambda_7BAE():

        label("loc_7BAE")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7BAE")

    QueueWorkItem2(0xF0, 0, lambda_7BAE)

    def lambda_7BBF():

        label("loc_7BBF")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7BBF")

    QueueWorkItem2(0xF1, 0, lambda_7BBF)
    Jump("loc_7CDE")

    label("loc_7BCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C29")
    OP_43(0xEF, 0x0, 0x5, 0x14)

    def lambda_7BE8():

        label("loc_7BE8")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7BE8")

    QueueWorkItem2(0x22, 0, lambda_7BE8)

    def lambda_7BF9():

        label("loc_7BF9")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7BF9")

    QueueWorkItem2(0xEE, 0, lambda_7BF9)

    def lambda_7C0A():

        label("loc_7C0A")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7C0A")

    QueueWorkItem2(0xF0, 0, lambda_7C0A)

    def lambda_7C1B():

        label("loc_7C1B")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7C1B")

    QueueWorkItem2(0xF1, 0, lambda_7C1B)
    Jump("loc_7CDE")

    label("loc_7C29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C85")
    OP_43(0xF0, 0x0, 0x5, 0x14)

    def lambda_7C44():

        label("loc_7C44")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7C44")

    QueueWorkItem2(0x22, 0, lambda_7C44)

    def lambda_7C55():

        label("loc_7C55")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7C55")

    QueueWorkItem2(0xEE, 0, lambda_7C55)

    def lambda_7C66():

        label("loc_7C66")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7C66")

    QueueWorkItem2(0xEF, 0, lambda_7C66)

    def lambda_7C77():

        label("loc_7C77")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7C77")

    QueueWorkItem2(0xF1, 0, lambda_7C77)
    Jump("loc_7CDE")

    label("loc_7C85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CDE")
    OP_43(0xF1, 0x0, 0x5, 0x14)

    def lambda_7CA0():

        label("loc_7CA0")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7CA0")

    QueueWorkItem2(0x22, 0, lambda_7CA0)

    def lambda_7CB1():

        label("loc_7CB1")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7CB1")

    QueueWorkItem2(0xEE, 0, lambda_7CB1)

    def lambda_7CC2():

        label("loc_7CC2")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7CC2")

    QueueWorkItem2(0xEF, 0, lambda_7CC2)

    def lambda_7CD3():

        label("loc_7CD3")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_7CD3")

    QueueWorkItem2(0xF0, 0, lambda_7CD3)

    label("loc_7CDE")

    WaitChrThread(0xEE, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7ECC")
    OP_62(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D35")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7D9C")

    label("loc_7D35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D5D")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7D9C")

    label("loc_7D5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D85")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7D9C")

    label("loc_7D85")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7D9C")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DC9")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7E30")

    label("loc_7DC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DF1")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7E30")

    label("loc_7DF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E19")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7E30")

    label("loc_7E19")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7E30")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E5D")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7EC4")

    label("loc_7E5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E85")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7EC4")

    label("loc_7E85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EAD")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7EC4")

    label("loc_7EAD")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7EC4")

    Sleep(1000)
    Jump("loc_8484")

    label("loc_7ECC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80B5")
    OP_62(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1E")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7F85")

    label("loc_7F1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F46")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7F85")

    label("loc_7F46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F6E")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7F85")

    label("loc_7F6E")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7F85")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FB2")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8019")

    label("loc_7FB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FDA")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8019")

    label("loc_7FDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8002")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8019")

    label("loc_8002")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8019")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8046")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_80AD")

    label("loc_8046")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_806E")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_80AD")

    label("loc_806E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8096")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_80AD")

    label("loc_8096")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_80AD")

    Sleep(1000)
    Jump("loc_8484")

    label("loc_80B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_829E")
    OP_62(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8107")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_816E")

    label("loc_8107")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_812F")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_816E")

    label("loc_812F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8157")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_816E")

    label("loc_8157")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_816E")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_819B")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8202")

    label("loc_819B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81C3")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8202")

    label("loc_81C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81EB")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8202")

    label("loc_81EB")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8202")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_822F")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8296")

    label("loc_822F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8257")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8296")

    label("loc_8257")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_827F")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8296")

    label("loc_827F")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8296")

    Sleep(1000)
    Jump("loc_8484")

    label("loc_829E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8484")
    OP_62(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82F0")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8357")

    label("loc_82F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8318")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8357")

    label("loc_8318")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8340")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8357")

    label("loc_8340")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8357")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8384")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_83EB")

    label("loc_8384")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83AC")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_83EB")

    label("loc_83AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83D4")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_83EB")

    label("loc_83D4")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_83EB")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8418")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_847F")

    label("loc_8418")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8440")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_847F")

    label("loc_8440")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8468")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_847F")

    label("loc_8468")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_847F")

    Sleep(1000)

    label("loc_8484")

    OP_44(0x22, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)

    ChrTalk(    #179
        0x22,
        "\x07\x0C#1614FUmm...\x07\x00\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x110, 19)
    SetChrSubChip(0x110, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x110, 20)
    SetChrSubChip(0x110, 1)

    def lambda_84E2():
        OP_6D(-4000, 4000, 3300, 500)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_84E2)

    def lambda_84FA():
        OP_6B(2100, 500)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_84FA)
    OP_0D()
    Sleep(500)

    ChrTalk(    #180
        0x110,
        "#263F#5PPater...Mater!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Call(5, 25)
    Return()

    # Function_19_645A end

    def Function_20_8530(): pass

    label("Function_20_8530")

    OP_8C(0x110, 270, 400)
    OP_8E(0xFE, 0xFFFFF330, 0xFA0, 0x6EA, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_20_8530 end

    def Function_21_8553(): pass

    label("Function_21_8553")

    PlayEffect(0x0, 0xFF, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
    Return()

    # Function_21_8553 end

    def Function_22_8599(): pass

    label("Function_22_8599")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x27023E, 0x270248, 0x13)
    OP_D2(0x270244, 0x27024E, 0x14)
    OP_D2(0x270022, 0x270025, 0x15)
    LoadEffect(0x0, "map\\mp204_02.eff")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_862F")
    SetChrPos(0xF1, -640, 11920, 40680, 180)
    SetChrPos(0xF0, 1290, 11920, 40570, 180)
    SetChrPos(0xEF, 370, 11920, 39610, 180)
    SetChrPos(0xEE, 220, 11920, 41870, 180)
    Jump("loc_872B")

    label("loc_862F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8684")
    SetChrPos(0xF1, -640, 11920, 40680, 180)
    SetChrPos(0xF0, 1290, 11920, 40570, 180)
    SetChrPos(0xEE, 370, 11920, 39610, 180)
    SetChrPos(0xEF, 220, 11920, 41870, 180)
    Jump("loc_872B")

    label("loc_8684")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86D9")
    SetChrPos(0xF1, -640, 11920, 40680, 180)
    SetChrPos(0xEF, 1290, 11920, 40570, 180)
    SetChrPos(0xEE, 370, 11920, 39610, 180)
    SetChrPos(0xF0, 220, 11920, 41870, 180)
    Jump("loc_872B")

    label("loc_86D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_872B")
    SetChrPos(0xF0, -640, 11920, 40680, 180)
    SetChrPos(0xEF, 1290, 11920, 40570, 180)
    SetChrPos(0xEE, 370, 11920, 39610, 180)
    SetChrPos(0xF1, 220, 11920, 41870, 180)

    label("loc_872B")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-500, 11920, 41690, 0)
    OP_67(0, 7590, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(419, 0)

    def lambda_879A():
        OP_6B(1880, 6000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_879A)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8908")
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 370, 11920, 39610, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_8801():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8801)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, 1290, 11920, 40570, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_884D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_884D)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, -640, 11920, 40680, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_8899():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_8899)
    Sleep(1500)
    PlayEffect(0x0, 0xFF, 0xFF, 220, 11920, 41870, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_88EF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_88EF)
    WaitChrThread(0xEE, 0x1)
    Sleep(1000)
    Jump("loc_8D13")

    label("loc_8908")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A62")
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 370, 11920, 39610, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_895B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_895B)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, 1290, 11920, 40570, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_89A7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_89A7)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, -640, 11920, 40680, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_89F3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_89F3)
    Sleep(1500)
    PlayEffect(0x0, 0xFF, 0xFF, 220, 11920, 41870, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_8A49():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8A49)
    WaitChrThread(0xEF, 0x1)
    Sleep(1000)
    Jump("loc_8D13")

    label("loc_8A62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BBC")
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 370, 11920, 39610, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_8AB5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_8AB5)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, 1290, 11920, 40570, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_8B01():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8B01)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, -640, 11920, 40680, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_8B4D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_8B4D)
    Sleep(1500)
    PlayEffect(0x0, 0xFF, 0xFF, 220, 11920, 41870, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_8BA3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_8BA3)
    WaitChrThread(0xF0, 0x1)
    Sleep(1000)
    Jump("loc_8D13")

    label("loc_8BBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D13")
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 370, 11920, 39610, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_8C0F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_8C0F)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, 1290, 11920, 40570, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_8C5B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8C5B)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, -640, 11920, 40680, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_8CA7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_8CA7)
    Sleep(1500)
    PlayEffect(0x0, 0xFF, 0xFF, 220, 11920, 41870, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_8CFD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_8CFD)
    WaitChrThread(0xF1, 0x1)
    Sleep(1000)

    label("loc_8D13")

    OP_62(0x110, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    ChrTalk(    #181
        0x110,
        "#268F#2P*sigh*\x02",
    )

    CloseMessageWindow()
    OP_62(0x110, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x22, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F3B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DA4")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8E0B")

    label("loc_8DA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DCC")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8E0B")

    label("loc_8DCC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DF4")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8E0B")

    label("loc_8DF4")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8E0B")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E38")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8E9F")

    label("loc_8E38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E60")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8E9F")

    label("loc_8E60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E88")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8E9F")

    label("loc_8E88")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8E9F")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ECC")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8F33")

    label("loc_8ECC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EF4")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8F33")

    label("loc_8EF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F1C")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8F33")

    label("loc_8F1C")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8F33")

    Sleep(1000)
    Jump("loc_949F")

    label("loc_8F3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9108")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F71")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8FD8")

    label("loc_8F71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F99")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8FD8")

    label("loc_8F99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FC1")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8FD8")

    label("loc_8FC1")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8FD8")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9005")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_906C")

    label("loc_9005")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_902D")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_906C")

    label("loc_902D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9055")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_906C")

    label("loc_9055")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_906C")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9099")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9100")

    label("loc_9099")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90C1")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9100")

    label("loc_90C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90E9")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9100")

    label("loc_90E9")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_9100")

    Sleep(1000)
    Jump("loc_949F")

    label("loc_9108")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_913E")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_91A5")

    label("loc_913E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9166")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_91A5")

    label("loc_9166")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_918E")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_91A5")

    label("loc_918E")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_91A5")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91D2")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9239")

    label("loc_91D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91FA")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9239")

    label("loc_91FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9222")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9239")

    label("loc_9222")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_9239")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9266")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_92CD")

    label("loc_9266")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_928E")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_92CD")

    label("loc_928E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92B6")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_92CD")

    label("loc_92B6")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_92CD")

    Sleep(1000)
    Jump("loc_949F")

    label("loc_92D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_949F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_930B")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9372")

    label("loc_930B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9333")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9372")

    label("loc_9333")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_935B")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9372")

    label("loc_935B")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_9372")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_939F")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9406")

    label("loc_939F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93C7")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9406")

    label("loc_93C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93EF")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9406")

    label("loc_93EF")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_9406")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9433")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_949A")

    label("loc_9433")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_945B")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_949A")

    label("loc_945B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9483")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_949A")

    label("loc_9483")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_949A")

    Sleep(1000)

    label("loc_949F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94DD")

    def lambda_94B3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_94B3)
    Sleep(100)

    def lambda_94C6():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_94C6)
    Sleep(100)
    OP_8C(0xF1, 0, 0)
    Jump("loc_9594")

    label("loc_94DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_951B")

    def lambda_94F1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_94F1)
    Sleep(100)

    def lambda_9504():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_9504)
    Sleep(100)
    OP_8C(0xF1, 0, 400)
    Jump("loc_9594")

    label("loc_951B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9559")

    def lambda_952F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_952F)
    Sleep(100)

    def lambda_9542():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_9542)
    Sleep(100)
    OP_8C(0xF1, 0, 400)
    Jump("loc_9594")

    label("loc_9559")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9594")

    def lambda_956D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_956D)
    Sleep(100)

    def lambda_9580():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_9580)
    Sleep(100)
    OP_8C(0xF0, 0, 400)

    label("loc_9594")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9643")

    ChrTalk(    #182
        0x109,
        (
            "#1064FYou okay, Renne?\x02\x03",

            "#1066FIf you're feeling tired, why don't you rest here\x01",
            "in the garden for a bit?\x02\x03",

            "All the others are here--you wouldn't be alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D30")

    label("loc_9643")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_96B4")

    ChrTalk(    #183
        0x101,
        (
            "#1004FYou okay, Renne?\x02\x03",

            "#1015FWe can stop here and rest for a bit if you're\x01",
            "feeling tired.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D30")

    label("loc_96B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9754")

    ChrTalk(    #184
        0x107,
        (
            "#064FUmm... Are you feeling tired, Renne?\x02\x03",

            "#062FMaybe we should stop and rest for a bit?\x02\x03",

            "There's no shame in admitting you need a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D30")

    label("loc_9754")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_97ED")

    ChrTalk(    #185
        0x102,
        (
            "#1504FAre you feeling tired, Renne?\x02\x03",

            "#1503FDo you want to stop and rest for a while?\x01",
            "There's a rest area in front of the fountain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D30")

    label("loc_97ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_992E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_9898")

    ChrTalk(    #186
        0x10F,
        (
            "#1938FIf you're feeling tired, you'd be well advised\x01",
            "to rest for a while.\x02\x03",

            "#1937FNothing good comes from pushing your body\x01",
            "beyond its limits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_992B")

    label("loc_9898")


    ChrTalk(    #187
        0x10F,
        (
            "#1440FIf you're feeling tired, you'd be well advised\x01",
            "to rest for a while.\x02\x03",

            "#1446FNothing good comes from pushing your body\x01",
            "beyond its limits.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_992B")

    Jump("loc_9D30")

    label("loc_992E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_99AB")

    ChrTalk(    #188
        0x105,
        (
            "#1382FUmm... Should we rest a while if you're tired?\x02\x03",

            "#1165FI'd be happy to make some tea if you want.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D30")

    label("loc_99AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A2C")

    ChrTalk(    #189
        0x10A,
        (
            "#814FUmm... Are you feeling tired, Renne?\x02\x03",

            "#819FHeehee. Why don't we stop and rest\x01",
            "here for a while, then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D30")

    label("loc_9A2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A97")

    ChrTalk(    #190
        0x10B,
        (
            "#213FUmm... Are you feeling tired?\x02\x03",

            "#210FWhy don't we take a break over there,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D30")

    label("loc_9A97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B12")

    ChrTalk(    #191
        0x106,
        (
            "#052F...You feelin' tired?\x02\x03",

            "#053FGo rest, then. No good comes from kids pushing\x01",
            "themselves too hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D30")

    label("loc_9B12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9BBB")

    ChrTalk(    #192
        0x10C,
        (
            "#115FIf you feel tired, you should rest, Renne.\x02\x03",

            "#110FYou're an important member of the team--\x01",
            "we want you to be in the best condition you\x01",
            "can be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D30")

    label("loc_9BBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C2A")

    ChrTalk(    #193
        0x103,
        (
            "#1523FOh, you feeling tired?\x02\x03",

            "#1520FMaybe you should go sit down\x01",
            "in the rest area, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D30")

    label("loc_9C2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9CB2")

    ChrTalk(    #194
        0x10D,
        (
            "#272FIf you're feeling tired, you should go and rest.\x02\x03",

            "We don't want your judgment impaired when\x01",
            "we need it most.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D30")

    label("loc_9CB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D30")

    ChrTalk(    #195
        0x10E,
        (
            "#176FAre you feeling tired, Renne?\x02\x03",

            "#170FPerhaps you should spend some time in the rest\x01",
            "area recuperating?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D30")

    OP_63(0x110)
    Sleep(300)

    ChrTalk(    #196
        0x110,
        (
            "#266F#11PI'm not tired at all!\x02\x03",

            "#267FI've just got something on my mind.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DC5")

    ChrTalk(    #197
        0x101,
        "#1011FSomething on your mind? Like what?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FDF")

    label("loc_9DC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_9DED")

    ChrTalk(    #198
        0x10F,
        "#1930F...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9DFD")

    label("loc_9DED")


    ChrTalk(    #199
        0x10F,
        "#1440F...?\x02",
    )

    CloseMessageWindow()

    label("loc_9DFD")

    Jump("loc_9FDF")

    label("loc_9E00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E38")

    ChrTalk(    #200
        0x104,
        "#1543FOh? And what might that be?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FDF")

    label("loc_9E38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E6E")

    ChrTalk(    #201
        0x108,
        "#072FHmm... What might that be?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FDF")

    label("loc_9E6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9EAE")

    ChrTalk(    #202
        0x109,
        (
            "#1064FSomething on your mind?\x02\x03",

            "Like what?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FDF")

    label("loc_9EAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9EE1")

    ChrTalk(    #203
        0x10E,
        "#172FSomething on your mind?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FDF")

    label("loc_9EE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F01")

    ChrTalk(    #204
        0x10D,
        "#270FHmm?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FDF")

    label("loc_9F01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F2C")

    ChrTalk(    #205
        0x103,
        "#1522FOh? Like what?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FDF")

    label("loc_9F2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F4F")

    ChrTalk(    #206
        0x10B,
        "#213F...Huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FDF")

    label("loc_9F4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F71")

    ChrTalk(    #207
        0x10A,
        "#814FUmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FDF")

    label("loc_9F71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F94")

    ChrTalk(    #208
        0x105,
        "#1164FUmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FDF")

    label("loc_9F94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FB5")

    ChrTalk(    #209
        0x106,
        "#555FUh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FDF")

    label("loc_9FB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FDF")

    ChrTalk(    #210
        0x107,
        "#564FUmm... Like what?\x02",
    )

    CloseMessageWindow()

    label("loc_9FDF")

    OP_62(0x110, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x110)
    Sleep(150)

    ChrTalk(    #211
        0x110,
        (
            "#263F#11PHmm... Well, I suppose it can't hurt.\x02\x03",

            "#269FLet me give it a try.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A21B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A084")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A0EB")

    label("loc_A084")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0AC")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A0EB")

    label("loc_A0AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0D4")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A0EB")

    label("loc_A0D4")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_A0EB")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A118")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A17F")

    label("loc_A118")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A140")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A17F")

    label("loc_A140")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A168")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A17F")

    label("loc_A168")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_A17F")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1AC")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A213")

    label("loc_A1AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1D4")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A213")

    label("loc_A1D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1FC")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A213")

    label("loc_A1FC")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_A213")

    Sleep(1000)
    Jump("loc_A77F")

    label("loc_A21B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3E8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A251")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A2B8")

    label("loc_A251")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A279")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A2B8")

    label("loc_A279")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2A1")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A2B8")

    label("loc_A2A1")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_A2B8")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2E5")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A34C")

    label("loc_A2E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A30D")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A34C")

    label("loc_A30D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A335")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A34C")

    label("loc_A335")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_A34C")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A379")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A3E0")

    label("loc_A379")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3A1")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A3E0")

    label("loc_A3A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3C9")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A3E0")

    label("loc_A3C9")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_A3E0")

    Sleep(1000)
    Jump("loc_A77F")

    label("loc_A3E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A41E")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A485")

    label("loc_A41E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A446")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A485")

    label("loc_A446")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A46E")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A485")

    label("loc_A46E")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_A485")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4B2")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A519")

    label("loc_A4B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4DA")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A519")

    label("loc_A4DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A502")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A519")

    label("loc_A502")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_A519")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A546")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A5AD")

    label("loc_A546")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A56E")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A5AD")

    label("loc_A56E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A596")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A5AD")

    label("loc_A596")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_A5AD")

    Sleep(1000)
    Jump("loc_A77F")

    label("loc_A5B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A77F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5EB")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A652")

    label("loc_A5EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A613")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A652")

    label("loc_A613")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A63B")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A652")

    label("loc_A63B")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_A652")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A67F")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A6E6")

    label("loc_A67F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6A7")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A6E6")

    label("loc_A6A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6CF")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A6E6")

    label("loc_A6CF")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_A6E6")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A713")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A77A")

    label("loc_A713")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A73B")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A77A")

    label("loc_A73B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A763")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_A77A")

    label("loc_A763")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_A77A")

    Sleep(1000)

    label("loc_A77F")


    ChrTalk(    #212
        0x110,
        (
            "#1305F#11PHeehee. Come this way.\x02\x03",

            "I haven't got enough space here.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x110, 0x0, 0x5, 0x18)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A812")

    def lambda_A7E2():

        label("loc_A7E2")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_A7E2")

    QueueWorkItem2(0xEF, 0, lambda_A7E2)

    def lambda_A7F3():

        label("loc_A7F3")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_A7F3")

    QueueWorkItem2(0xF0, 0, lambda_A7F3)

    def lambda_A804():

        label("loc_A804")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_A804")

    QueueWorkItem2(0xF1, 0, lambda_A804)
    Jump("loc_A8DB")

    label("loc_A812")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A856")

    def lambda_A826():

        label("loc_A826")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_A826")

    QueueWorkItem2(0xEE, 0, lambda_A826)

    def lambda_A837():

        label("loc_A837")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_A837")

    QueueWorkItem2(0xF0, 0, lambda_A837)

    def lambda_A848():

        label("loc_A848")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_A848")

    QueueWorkItem2(0xF1, 0, lambda_A848)
    Jump("loc_A8DB")

    label("loc_A856")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A89A")

    def lambda_A86A():

        label("loc_A86A")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_A86A")

    QueueWorkItem2(0xEE, 0, lambda_A86A)

    def lambda_A87B():

        label("loc_A87B")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_A87B")

    QueueWorkItem2(0xEF, 0, lambda_A87B)

    def lambda_A88C():

        label("loc_A88C")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_A88C")

    QueueWorkItem2(0xF1, 0, lambda_A88C)
    Jump("loc_A8DB")

    label("loc_A89A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8DB")

    def lambda_A8AE():

        label("loc_A8AE")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_A8AE")

    QueueWorkItem2(0xEE, 0, lambda_A8AE)

    def lambda_A8BF():

        label("loc_A8BF")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_A8BF")

    QueueWorkItem2(0xEF, 0, lambda_A8BF)

    def lambda_A8D0():

        label("loc_A8D0")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_A8D0")

    QueueWorkItem2(0xF0, 0, lambda_A8D0)

    label("loc_A8DB")

    Sleep(2500)

    def lambda_A8E6():
        OP_6D(-500, 11000, 36690, 6000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_A8E6)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A92D")
    OP_43(0xEF, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xF0, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xF1, 0x0, 0x5, 0x17)
    Jump("loc_A9BA")

    label("loc_A92D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A95D")
    OP_43(0xEE, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xF0, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xF1, 0x0, 0x5, 0x17)
    Jump("loc_A9BA")

    label("loc_A95D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A98D")
    OP_43(0xEE, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xEF, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xF1, 0x0, 0x5, 0x17)
    Jump("loc_A9BA")

    label("loc_A98D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9BA")
    OP_43(0xEE, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xEF, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xF0, 0x0, 0x5, 0x17)

    label("loc_A9BA")

    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x22, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA60")
    SetChrPos(0xF1, 1660, 4000, 480, 270)
    SetChrPos(0xF0, -10, 4000, 730, 270)
    SetChrPos(0xEF, 1450, 4000, 2260, 270)
    SetChrPos(0xEE, -3280, 4000, 1770, 270)
    Jump("loc_AB5C")

    label("loc_AA60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAB5")
    SetChrPos(0xF1, 1660, 4000, 480, 270)
    SetChrPos(0xF0, -10, 4000, 730, 270)
    SetChrPos(0xEE, 1450, 4000, 2260, 270)
    SetChrPos(0xEF, -3280, 4000, 1770, 270)
    Jump("loc_AB5C")

    label("loc_AAB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB0A")
    SetChrPos(0xF1, 1660, 4000, 480, 270)
    SetChrPos(0xEF, -10, 4000, 730, 270)
    SetChrPos(0xEE, 1450, 4000, 2260, 270)
    SetChrPos(0xF0, -3280, 4000, 1770, 270)
    Jump("loc_AB5C")

    label("loc_AB0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB5C")
    SetChrPos(0xF0, 1660, 4000, 480, 270)
    SetChrPos(0xEF, -10, 4000, 730, 270)
    SetChrPos(0xEE, 1450, 4000, 2260, 270)
    SetChrPos(0xF1, -3280, 4000, 1770, 270)

    label("loc_AB5C")

    OP_8C(0x22, 180, 0)
    OP_6D(-3580, 4000, 3190, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(326000, 0)
    OP_6E(419, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x110, 19)
    SetChrSubChip(0x110, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x110, 20)
    SetChrSubChip(0x110, 1)

    def lambda_ABDE():
        OP_6D(-4000, 4000, 3300, 500)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_ABDE)

    def lambda_ABF6():
        OP_6B(2100, 500)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_ABF6)
    OP_0D()
    Sleep(500)

    ChrTalk(    #213
        0x110,
        "#263F#5PPater...Mater!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Call(5, 25)
    Return()

    # Function_22_8599 end

    def Function_23_AC2C(): pass

    label("Function_23_AC2C")

    OP_8C(0xFE, 180, 0)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
    Return()

    # Function_23_AC2C end

    def Function_24_AC48(): pass

    label("Function_24_AC48")

    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x9F6, 0x2E90, 0xA12C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x8E8, 0x2E90, 0x966E, 0xBB8, 0x0)
    OP_8E(0xFE, 0x122, 0x2E90, 0x8CC8, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1E0, 0xFA0, 0x4196, 0xBB8, 0x0)
    Return()

    # Function_24_AC48 end

    def Function_25_ACA0(): pass

    label("Function_25_ACA0")

    EventBegin(0x0)
    SetChrSubChip(0x110, 1)

    def lambda_ACAD():

        label("loc_ACAD")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_ACAD")

    QueueWorkItem2(0x10, 3, lambda_ACAD)
    OP_22(0x113, 0x1, 0x46)
    Sleep(1000)

    def lambda_ACD2():

        label("loc_ACD2")

        OP_7C(0x1E, 0x1E, 0xBB8, 0x64)
        OP_48()
        Jump("loc_ACD2")

    QueueWorkItem2(0x10, 3, lambda_ACD2)
    OP_22(0x113, 0x1, 0x50)
    Sleep(1000)

    def lambda_ACF7():

        label("loc_ACF7")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_ACF7")

    QueueWorkItem2(0x10, 3, lambda_ACF7)
    OP_22(0x113, 0x1, 0x5A)
    Sleep(1000)

    def lambda_AD1C():

        label("loc_AD1C")

        OP_7C(0x50, 0x50, 0xBB8, 0x64)
        OP_48()
        Jump("loc_AD1C")

    QueueWorkItem2(0x10, 3, lambda_AD1C)
    OP_22(0x113, 0x1, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-6890, 12700, 3150, 0)
    OP_67(0, 9030, -10000, 0)
    OP_6B(2210, 0)
    OP_6C(335000, 0)
    OP_6E(567, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADDB")
    SetChrPos(0xF1, 990, 4000, -870, 315)
    SetChrPos(0xF0, -970, 4000, -580, 315)
    SetChrPos(0xEF, 890, 4000, 750, 315)
    SetChrPos(0xEE, -4400, 4000, 2420, 315)
    Jump("loc_AED7")

    label("loc_ADDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE30")
    SetChrPos(0xF1, 990, 4000, -870, 315)
    SetChrPos(0xF0, -970, 4000, -580, 315)
    SetChrPos(0xEE, 890, 4000, 750, 315)
    SetChrPos(0xEF, -4400, 4000, 2420, 315)
    Jump("loc_AED7")

    label("loc_AE30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE85")
    SetChrPos(0xF1, 990, 4000, -870, 315)
    SetChrPos(0xEF, -970, 4000, -580, 315)
    SetChrPos(0xEE, 890, 4000, 750, 315)
    SetChrPos(0xF0, -4400, 4000, 2420, 315)
    Jump("loc_AED7")

    label("loc_AE85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AED7")
    SetChrPos(0xF0, 990, 4000, -870, 315)
    SetChrPos(0xEF, -970, 4000, -580, 315)
    SetChrPos(0xEE, 890, 4000, 750, 315)
    SetChrPos(0xF1, -4400, 4000, 2420, 315)

    label("loc_AED7")

    OP_8C(0x22, 270, 0)

    def lambda_AEE4():
        OP_6B(1600, 1000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_AEE4)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, -8000, 22000, 5590, 135)
    OP_A1(0x10, 0x17)
    OP_72(0x417, 0x0)
    ExitThread()
    OP_B0(0x17, 0xF)
    OP_6F(0x17, 260)
    OP_70(0x17, 0xF1)

    def lambda_AF27():
        OP_8F(0xFE, 0xFFFFE0C0, 0xFA0, 0x1612, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_AF27)
    Sleep(1000)
    OP_72(0x2017, 0x0)
    ExitThread()
    OP_6F(0x17, 221)
    OP_70(0x17, 0xF0)
    OP_44(0x22, 0x0)
    OP_6D(-10490, 5100, 8140, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(442, 0)

    def lambda_AF9C():
        OP_6B(2300, 3000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_AF9C)
    OP_44(0x10, 0x3)
    OP_23(0x113)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0x1388, 0x5DC)
    WaitChrThread(0x10, 0x1)
    OP_73(0x17)
    OP_71(0x2017, 0x0)
    ExitThread()
    OP_D8(0x17, 0x3E8)
    OP_6F(0x17, 1)
    OP_70(0x17, 0x28)
    Sleep(1000)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_B006():
        OP_6D(-9100, 4500, 7000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B006)

    def lambda_B01E():
        OP_67(0, 3500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B01E)

    def lambda_B036():
        OP_6B(3400, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_B036)

    def lambda_B046():
        OP_6E(348, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_B046)
    WaitChrThread(0x10, 0x0)

    ChrTalk(    #214
        0x110,
        "#261F#5PHaha. I knew you'd come.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x110, 19)
    SetChrSubChip(0x110, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #215
        0x110,
        (
            "#263F#5PPater-Mater, switch to standby mode.\x02\x03",

            "#260FRight. That's that.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B0EC():
        OP_6D(-8970, 4000, 6760, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B0EC)

    def lambda_B104():
        OP_67(0, 3300, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B104)

    def lambda_B11C():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_B11C)

    def lambda_B12C():
        OP_6E(330, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_B12C)
    OP_8C(0x110, 135, 400)
    Sleep(300)
    SetChrFlags(0x110, 0x2)
    SetChrChipByIndex(0x110, 21)
    SetChrSubChip(0x110, 0)
    OP_99(0x110, 0x0, 0x4, 0x5DC)
    OP_22(0x1F6, 0x0, 0x64)
    OP_99(0x110, 0x5, 0x16, 0x708)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #216
        "\x07\x05Renne learned the \x07\x02[Pater-Mater]\x07\x05 S-Craft!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x21E, 0x0, 0x64)
    OP_35(0xF, 0x11D)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #217
        "\x07\x05Set \x07\x02[Pater-Mater]\x07\x05 as Renne's S-Break?\x18\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B217")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B276")

    Menu(
        1,
        -1,
        200,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B252"),
        (SWITCH_DEFAULT, "loc_B266"),
    )


    label("loc_B252")

    OP_BB(0xF, 0x6, 0x11D)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B273")

    label("loc_B266")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B273")

    label("loc_B273")

    Jump("loc_B217")

    label("loc_B276")

    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x110, 0x2)
    SetChrChipByIndex(0x110, 65535)
    SetChrSubChip(0x110, 0)
    SetChrPos(0x110, -3280, 4000, 1770, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2E3")
    SetChrPos(0xF1, 800, 4000, -650, 270)
    SetChrPos(0xF0, -810, 4000, -380, 270)
    SetChrPos(0xEF, 520, 4000, 1410, 270)
    Jump("loc_B3AC")

    label("loc_B2E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B327")
    SetChrPos(0xF1, 800, 4000, -650, 270)
    SetChrPos(0xF0, -810, 4000, -380, 270)
    SetChrPos(0xEE, 520, 4000, 1410, 270)
    Jump("loc_B3AC")

    label("loc_B327")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B36B")
    SetChrPos(0xF1, 800, 4000, -650, 270)
    SetChrPos(0xEF, -810, 4000, -380, 270)
    SetChrPos(0xEE, 520, 4000, 1410, 270)
    Jump("loc_B3AC")

    label("loc_B36B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3AC")
    SetChrPos(0xF0, 800, 4000, -650, 270)
    SetChrPos(0xEF, -810, 4000, -380, 270)
    SetChrPos(0xEE, 520, 4000, 1410, 270)

    label("loc_B3AC")

    OP_8C(0x22, 180, 0)
    OP_6D(-2400, 5080, 2800, 0)
    OP_67(0, 4320, -10000, 0)
    OP_6B(2630, 0)
    OP_6C(336000, 0)
    OP_6E(419, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B43A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_B42B")

    ChrTalk(    #218
        0x10F,
        "#1934F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B43A")

    label("loc_B42B")


    ChrTalk(    #219
        0x10F,
        "#1444F...\x02",
    )

    CloseMessageWindow()

    label("loc_B43A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B462")

    ChrTalk(    #220
        0x107,
        "#065F#12PU-Umm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B521")

    label("loc_B462")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B48B")

    ChrTalk(    #221
        0x101,
        "#1016F#12PU-Umm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B521")

    label("loc_B48B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4B7")

    ChrTalk(    #222
        0x109,
        "#1066F#12PR-Renne...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B521")

    label("loc_B4B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4DF")

    ChrTalk(    #223
        0x10A,
        "#812F#12PU-Umm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B521")

    label("loc_B4DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B507")

    ChrTalk(    #224
        0x10B,
        "#215F#12PU-Umm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B521")

    label("loc_B507")


    ChrTalk(    #225
        0x22,
        "\x07\x0C#1614F#11PErm...\x07\x00\x02",
    )

    CloseMessageWindow()

    label("loc_B521")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B552")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B5AA")

    label("loc_B552")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B575")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B5AA")

    label("loc_B575")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B598")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B5AA")

    label("loc_B598")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_B5AA")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5D2")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B62A")

    label("loc_B5D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5F5")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B62A")

    label("loc_B5F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B618")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B62A")

    label("loc_B618")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_B62A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B652")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B6AA")

    label("loc_B652")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B675")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B6AA")

    label("loc_B675")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B698")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B6AA")

    label("loc_B698")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_B6AA")

    Sleep(1000)
    Jump("loc_BB62")

    label("loc_B6B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B843")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6E3")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B73B")

    label("loc_B6E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B706")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B73B")

    label("loc_B706")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B729")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B73B")

    label("loc_B729")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_B73B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B763")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B7BB")

    label("loc_B763")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B786")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B7BB")

    label("loc_B786")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7A9")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B7BB")

    label("loc_B7A9")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_B7BB")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7E3")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B83B")

    label("loc_B7E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B806")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B83B")

    label("loc_B806")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B829")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B83B")

    label("loc_B829")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_B83B")

    Sleep(1000)
    Jump("loc_BB62")

    label("loc_B843")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9D4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B874")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B8CC")

    label("loc_B874")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B897")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B8CC")

    label("loc_B897")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8BA")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B8CC")

    label("loc_B8BA")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_B8CC")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8F4")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B94C")

    label("loc_B8F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B917")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B94C")

    label("loc_B917")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B93A")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B94C")

    label("loc_B93A")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_B94C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B974")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B9CC")

    label("loc_B974")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B997")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B9CC")

    label("loc_B997")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9BA")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_B9CC")

    label("loc_B9BA")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_B9CC")

    Sleep(1000)
    Jump("loc_BB62")

    label("loc_B9D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB62")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA05")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_BA5D")

    label("loc_BA05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA28")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_BA5D")

    label("loc_BA28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA4B")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_BA5D")

    label("loc_BA4B")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_BA5D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA85")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_BADD")

    label("loc_BA85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAA8")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_BADD")

    label("loc_BAA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BACB")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_BADD")

    label("loc_BACB")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_BADD")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB05")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_BB5D")

    label("loc_BB05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB28")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_BB5D")

    label("loc_BB28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB4B")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_BB5D")

    label("loc_BB4B")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_BB5D")

    Sleep(1000)

    label("loc_BB62")

    SetMessageWindowPos(300, 330, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(    #226
        "\x07\x00#4SWhaaaaaat?!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x1F4)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    ChrTalk(    #227
        0x110,
        (
            "#269F#5PTeehee. And why do you all look so surprised?\x02\x03",

            "#263FThis world can be directly influenced by people's\x01",
            "thoughts. We've established that much already.\x02\x03",

            "#265FSo why wouldn't Pater-Mater come for me?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_BC86():
        OP_6B(3400, 5000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_BC86)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x22, 0x0)
    OP_71(0x417, 0x0)
    ExitThread()
    OP_28(0x17, 0x4, 0x20)
    OP_A2(0x2C35)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 510, 4000, -1300, 180)
    SetChrPos(0x1, 510, 4000, -1300, 180)
    SetChrPos(0x2, 510, 4000, -1300, 180)
    SetChrPos(0x3, 510, 4000, -1300, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_8C(0x22, 135, 0)
    Sleep(1000)
    Call(0, 9)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_BD84")
    SetMapFlags(0x2000000)

    label("loc_BD84")

    Return()

    # Function_25_ACA0 end

    SaveToFile()

Try(main)
