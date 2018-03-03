from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0001_5 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0001.x',
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
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_6A1",          # 01, 1
        "Function_2_6A5",          # 02, 2
        "Function_3_985",          # 03, 3
        "Function_4_A9E",          # 04, 4
        "Function_5_C00",          # 05, 5
        "Function_6_D09",          # 06, 6
        "Function_7_DFF",          # 07, 7
        "Function_8_F1C",          # 08, 8
        "Function_9_1075",         # 09, 9
        "Function_10_12EF",        # 0A, 10
        "Function_11_15E7",        # 0B, 11
        "Function_12_18C9",        # 0C, 12
        "Function_13_1A25",        # 0D, 13
        "Function_14_1AEC",        # 0E, 14
        "Function_15_1BF4",        # 0F, 15
        "Function_16_1C78",        # 10, 16
        "Function_17_1D6B",        # 11, 17
        "Function_18_1E90",        # 12, 18
        "Function_19_1F9A",        # 13, 19
        "Function_20_2019",        # 14, 20
        "Function_21_209D",        # 15, 21
        "Function_22_2198",        # 16, 22
        "Function_23_2284",        # 17, 23
        "Function_24_23AD",        # 18, 24
        "Function_25_242B",        # 19, 25
        "Function_26_24B6",        # 1A, 26
        "Function_27_25A1",        # 1B, 27
        "Function_28_2643",        # 1C, 28
        "Function_29_27C5",        # 1D, 29
        "Function_30_28A9",        # 1E, 30
        "Function_31_290E",        # 1F, 31
        "Function_32_2A41",        # 20, 32
        "Function_33_2AF4",        # 21, 33
        "Function_34_2C32",        # 22, 34
        "Function_35_2D1E",        # 23, 35
        "Function_36_2E7D",        # 24, 36
        "Function_37_2F01",        # 25, 37
        "Function_38_30A2",        # 26, 38
        "Function_39_3107",        # 27, 39
        "Function_40_316C",        # 28, 40
        "Function_41_31D1",        # 29, 41
        "Function_42_3236",        # 2A, 42
        "Function_43_329B",        # 2B, 43
        "Function_44_4E01",        # 2C, 44
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(    #0
        (
            "\x06エピソード選択。◎＝スクリプト調整済。\x01",
            "▼未入力データあり。Ａ＝ＡＰＬ。Ｅ＝エフェクト。\x01",
            "Ｐ＝ポートレート。Ｂ＝ＢＧＭ＆ＳＥ。Ｓ＝シーン未入力\x02",
        )
    )


    label("loc_13A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_691")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "◎EP00 Julia's Day Off\x01",                             # 0
            "◎EP01 Capua's Delivery Service (Minigame)\x01",         # 1
            "◎EP02 Journey's End\x01",                               # 2
            "◎EP03 Paradise\x01",                                    # 3
            "◎EP05 The Banquet\x01",                                 # 4
            "◎EP06 Return to the Empire\x01",                        # 5
            "◎EP07 Client\x01",                                      # 6
            "◎EP08 Descended Wings\x01",                             # 7
            "◎EP09 The Happiness Stone\x01",                         # 8
            "◎EP10 Campanella's Quiz Game (Minigame)\x01",           # 9
            "◎EP11 The Casino (Minigame)\x01",                       # 10
            "◎EP12 Legendary Angler Estelle (Minigame)\x01",         # 11
            "◎EP13 Training, Agate-Style\x01",                       # 12
            "◎EP16 Arena (Minigame)\x01",                            # 13
            "◎EP17 Departure\x01",                                   # 14
            "◎EP18 Swordsmanship\x01",                               # 15
            "◎EP19 Like a Mother\x01",                               # 16
            "◎EP20 I Accept Your Request\x01",                       # 17
            "◎EP25 Orbal Gear Project Part 1\x01",                   # 18
            "◎EP26 Orbal Gear Project Part 2\x01",                   # 19
            "◎EP29 Phantasmal Blaze\x01",                            # 20
            "◎EP30 The Salt Pale (Lore)\x01",                        # 21
            "◎EP31 Phantom Thief B Report (Lore)\x01",               # 22
            "◎EP32 The Epstein Foundation (Lore)\x01",               # 23
            "◎EP33 Assault on the Imperial Guilds (Lore)\x01",       # 24
            "◎EP34 Gordias-Class Experiment Report (Lore)\x01",      # 25
        )
    )

    MenuEnd(0x0)
    Call(5, 1)
    OP_A2(0x2F00)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4BA"),
        (1, "loc_4C1"),
        (2, "loc_4DF"),
        (3, "loc_4F8"),
        (4, "loc_4FF"),
        (5, "loc_506"),
        (6, "loc_50D"),
        (7, "loc_514"),
        (8, "loc_51B"),
        (9, "loc_522"),
        (10, "loc_536"),
        (11, "loc_54A"),
        (12, "loc_568"),
        (13, "loc_5A9"),
        (14, "loc_5B0"),
        (15, "loc_5B7"),
        (16, "loc_5D8"),
        (17, "loc_5F1"),
        (18, "loc_5F8"),
        (19, "loc_5FF"),
        (20, "loc_606"),
        (21, "loc_61D"),
        (22, "loc_631"),
        (23, "loc_645"),
        (24, "loc_659"),
        (25, "loc_66D"),
        (SWITCH_DEFAULT, "loc_681"),
    )


    label("loc_4BA")

    Call(5, 3)
    Jump("loc_68E")

    label("loc_4C1")

    OP_D6(0x0)
    OP_E3(0x0, 0x1, 1024, 0x0)
    ClearParty()
    AddParty(0xA, 0xEE, 0xFF)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_4DF")

    OP_D6(0x0)
    OP_E3(0x0, 0x2, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_4F8")

    Call(5, 4)
    Jump("loc_68E")

    label("loc_4FF")

    Call(5, 5)
    Jump("loc_68E")

    label("loc_506")

    Call(5, 6)
    Jump("loc_68E")

    label("loc_50D")

    Call(5, 9)
    Jump("loc_68E")

    label("loc_514")

    Call(5, 10)
    Jump("loc_68E")

    label("loc_51B")

    Call(5, 11)
    Jump("loc_68E")

    label("loc_522")

    OP_E3(0x0, 0xA, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_536")

    OP_E3(0x0, 0xB, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_54A")

    OP_D6(0x0)
    OP_E3(0x0, 0xC, 1, 0x0)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_568")

    OP_A3(0x2F90)
    OP_A3(0x2F91)
    OP_A3(0x2F92)
    OP_A3(0x2F93)
    OP_A3(0x2F94)
    OP_A3(0x2F95)
    OP_A3(0x2F96)
    OP_A3(0x2F97)
    OP_D6(0x0)
    OP_E3(0x0, 0xD, 0, 0x0)
    ClearParty()
    AddParty(0x12, 0xF0, 0xFF)
    AddParty(0x10, 0xEE, 0xFF)
    AddParty(0x11, 0xEF, 0xFF)
    OP_C2(0x1, 0x4)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C1401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_5A9")

    Call(5, 2)
    Jump("loc_68E")

    label("loc_5B0")

    Call(5, 12)
    Jump("loc_68E")

    label("loc_5B7")

    OP_A3(0x2FA6)
    OP_D6(0x0)
    OP_E3(0x0, 0x12, 512, 0x0)
    ClearParty()
    AddParty(0x9, 0xEE, 0xFF)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_5D8")

    OP_D6(0x0)
    OP_E3(0x0, 0x13, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_5F1")

    Call(5, 13)
    Jump("loc_68E")

    label("loc_5F8")

    Call(5, 7)
    Jump("loc_68E")

    label("loc_5FF")

    Call(5, 8)
    Jump("loc_68E")

    label("loc_606")

    OP_E3(0x0, 0x1D, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_61D")

    OP_E3(0x0, 0x1E, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_631")

    OP_E3(0x0, 0x1F, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_645")

    OP_E3(0x0, 0x20, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_659")

    OP_E3(0x0, 0x21, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_66D")

    OP_E3(0x0, 0x22, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_68E")

    label("loc_681")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68E")

    label("loc_68E")

    Jump("loc_13A")

    label("loc_691")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_6A1(): pass

    label("Function_1_6A1")

    OP_A3(0x2F00)
    Return()

    # Function_1_6A1 end

    def Function_2_6A5(): pass

    label("Function_2_6A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_975")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■最初から\x01",                        # 0
            "■タイトルから（未達成）\x01",          # 1
            "■タイトルから（初級達成済）\x01",      # 2
            "■タイトルから（中級達成済）\x01",      # 3
            "■タイトルから（上級達成済）\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_756"),
        (1, "loc_7AE"),
        (2, "loc_818"),
        (3, "loc_887"),
        (4, "loc_8FB"),
        (SWITCH_DEFAULT, "loc_965"),
    )


    label("loc_756")

    OP_DB(0x0, 0xE)
    OP_DB(0x0, 0x6)
    OP_DB(0x0, 0xD)
    OP_DB(0x0, 0x1)
    OP_DB(0x0, 0xC)
    OP_DB(0x0, 0xA)
    OP_DB(0x0, 0x4)
    OP_DB(0x0, 0x9)
    OP_DB(0x0, 0x2)
    OP_DB(0x0, 0x5)
    OP_DB(0x0, 0xB)
    OP_DB(0x0, 0x3)
    OP_DB(0x0, 0x7)
    OP_DB(0x0, 0x0)
    OP_DB(0x0, 0xF)
    OP_DD(0x1, 0x0, 0x0, 0, 0, 0, 0)
    OP_E3(0x0, 0x10, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_972")

    label("loc_7AE")

    OP_DB(0x0, 0xE)
    OP_DB(0x0, 0x6)
    OP_DB(0x0, 0xD)
    OP_DB(0x0, 0x1)
    OP_DB(0x0, 0xC)
    OP_DB(0x0, 0xA)
    OP_DB(0x0, 0x4)
    OP_DB(0x0, 0x9)
    OP_DB(0x0, 0x2)
    OP_DB(0x0, 0x5)
    OP_DB(0x0, 0xB)
    OP_DB(0x0, 0x3)
    OP_DB(0x0, 0x7)
    OP_DB(0x0, 0x0)
    OP_DB(0x0, 0xF)
    OP_DD(0x1, 0x0, 0x0, 0, 0, 0, 0)
    OP_A2(0x2F13)
    OP_28(0x21, 0x3, 0x20)
    OP_28(0x22, 0x3, 0x20)
    OP_28(0x23, 0x3, 0x20)
    OP_E3(0x0, 0x10, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_972")

    label("loc_818")

    OP_DB(0x0, 0xE)
    OP_DB(0x0, 0x6)
    OP_DB(0x0, 0xD)
    OP_DB(0x0, 0x1)
    OP_DB(0x0, 0xC)
    OP_DB(0x0, 0xA)
    OP_DB(0x0, 0x4)
    OP_DB(0x0, 0x9)
    OP_DB(0x0, 0x2)
    OP_DB(0x0, 0x5)
    OP_DB(0x0, 0xB)
    OP_DB(0x0, 0x3)
    OP_DB(0x0, 0x7)
    OP_DB(0x0, 0x0)
    OP_DB(0x0, 0xF)
    OP_DD(0x1, 0x0, 0x0, 0, 0, 0, 0)
    OP_A2(0x2F13)
    OP_28(0x21, 0x4, 0x20)
    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x3, 0x20)
    OP_28(0x23, 0x3, 0x20)
    OP_E3(0x0, 0x10, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_972")

    label("loc_887")

    OP_DB(0x0, 0xE)
    OP_DB(0x0, 0x6)
    OP_DB(0x0, 0xD)
    OP_DB(0x0, 0x1)
    OP_DB(0x0, 0xC)
    OP_DB(0x0, 0xA)
    OP_DB(0x0, 0x4)
    OP_DB(0x0, 0x9)
    OP_DB(0x0, 0x2)
    OP_DB(0x0, 0x5)
    OP_DB(0x0, 0xB)
    OP_DB(0x0, 0x3)
    OP_DB(0x0, 0x7)
    OP_DB(0x0, 0x0)
    OP_DB(0x0, 0xF)
    OP_DD(0x1, 0x0, 0x0, 0, 0, 0, 0)
    OP_A2(0x2F13)
    OP_28(0x21, 0x4, 0x20)
    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x20)
    OP_28(0x23, 0x4, 0x8)
    OP_28(0x23, 0x3, 0x20)
    OP_E3(0x0, 0x10, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_972")

    label("loc_8FB")

    OP_DB(0x0, 0xE)
    OP_DB(0x0, 0x6)
    OP_DB(0x0, 0xD)
    OP_DB(0x0, 0x1)
    OP_DB(0x0, 0xC)
    OP_DB(0x0, 0xA)
    OP_DB(0x0, 0x4)
    OP_DB(0x0, 0x9)
    OP_DB(0x0, 0x2)
    OP_DB(0x0, 0x5)
    OP_DB(0x0, 0xB)
    OP_DB(0x0, 0x3)
    OP_DB(0x0, 0x7)
    OP_DB(0x0, 0x0)
    OP_DB(0x0, 0xF)
    OP_DD(0x1, 0x0, 0x0, 0, 0, 0, 0)
    OP_A2(0x2F13)
    OP_28(0x21, 0x4, 0x20)
    OP_28(0x22, 0x4, 0x20)
    OP_28(0x23, 0x4, 0x20)
    OP_E3(0x0, 0x10, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_972")

    label("loc_965")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_972")

    label("loc_972")

    Jump("Function_2_6A5")

    label("loc_975")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_6A5 end

    def Function_3_985(): pass

    label("Function_3_985")


    AnonymousTalk(    #1
        "\x06どっから？\x02",
    )


    label("loc_993")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A8E")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■最初から\x01",                  # 0
            "■ユリア様に突撃\x01",            # 1
            "■シスター・エレン登場\x01",      # 2
            "■ミュラーとの会話\x01",          # 3
            "■城でクローゼと会う\x01",        # 4
        )
    )

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x0, 8192, 0x0)
    ClearParty()
    AddParty(0xD, 0xEE, 0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A33"),
        (1, "loc_A42"),
        (2, "loc_A51"),
        (3, "loc_A60"),
        (4, "loc_A6F"),
        (SWITCH_DEFAULT, "loc_A7E"),
    )


    label("loc_A33")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_A8B")

    label("loc_A42")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_A8B")

    label("loc_A51")

    OP_A2(0x2506)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_A8B")

    label("loc_A60")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_A8B")

    label("loc_A6F")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_A8B")

    label("loc_A7E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8B")

    label("loc_A8B")

    Jump("loc_993")

    label("loc_A8E")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_985 end

    def Function_4_A9E(): pass

    label("Function_4_A9E")


    AnonymousTalk(    #2
        "\x06どっから？\x02",
    )


    label("loc_AAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF0")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■１．楽園\x01",                    # 0
            "■２．お姫様\x01",                  # 1
            "■３．遊戯\x01",                    # 2
            "■４．レン\x01",                    # 3
            "■～幕間～\x01",                    # 4
            "■５．夢の続き\x01",                # 5
            "■街道・夜　クロスベルへ\x01",      # 6
            "■夜スカイマップ\x01",              # 7
        )
    )

    MenuEnd(0x0)
    OP_E3(0x0, 0x3, 0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B68"),
        (1, "loc_B77"),
        (2, "loc_B86"),
        (3, "loc_B95"),
        (4, "loc_BA4"),
        (5, "loc_BB3"),
        (6, "loc_BC2"),
        (7, "loc_BD1"),
        (SWITCH_DEFAULT, "loc_BE0"),
    )


    label("loc_B68")

    OP_A2(0x2504)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_BED")

    label("loc_B77")

    OP_A2(0x2505)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_BED")

    label("loc_B86")

    OP_A2(0x2506)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_BED")

    label("loc_B95")

    OP_A2(0x2507)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_BED")

    label("loc_BA4")

    OP_A2(0x2508)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_BED")

    label("loc_BB3")

    OP_A2(0x2509)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_BED")

    label("loc_BC2")

    OP_A2(0x250A)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_BED")

    label("loc_BD1")

    OP_A2(0x2504)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_BED")

    label("loc_BE0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BED")

    label("loc_BED")

    Jump("loc_AAC")

    label("loc_BF0")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_A9E end

    def Function_5_C00(): pass

    label("Function_5_C00")

    OP_A3(0x2F9A)
    OP_A3(0x2F9B)
    OP_A3(0x2F9C)
    OP_A3(0x2F9D)
    OP_A3(0x2F9E)
    OP_A3(0x2F9F)
    OP_A3(0x2FA0)
    OP_A3(0x2FA1)
    OP_A3(0x2FA2)
    OP_A3(0x2FA3)

    AnonymousTalk(    #3
        "\x06どっから？\x02",
    )


    label("loc_C2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF9")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■最初から\x01",            # 0
            "■フリー移動から\x01",      # 1
            "■クローゼの告白\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x5, 2, 0x0)
    ClearParty()
    AddParty(0x1, 0xEE, 0xFF)
    OP_BB(0x1, 0x1, 0x1C)
    OP_BD()
    OP_C2(0x1, 0x1F)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CA1"),
        (1, "loc_CB0"),
        (2, "loc_CBF"),
        (SWITCH_DEFAULT, "loc_CE9"),
    )


    label("loc_CA1")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_CF6")

    label("loc_CB0")

    OP_A2(0x2F9A)
    NewScene("ED6_DT21/T4206   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_CF6")

    label("loc_CBF")

    OP_A2(0x2F9A)
    OP_A2(0x2F9B)
    OP_A2(0x2F9C)
    OP_A2(0x2F9D)
    OP_A2(0x2F9E)
    OP_A2(0x2F9F)
    OP_A2(0x2FA0)
    OP_A2(0x2FA1)
    OP_A2(0x2FA2)
    OP_A2(0x2FA3)
    NewScene("ED6_DT21/T4206   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_CF6")

    label("loc_CE9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF6")

    label("loc_CF6")

    Jump("loc_C2C")

    label("loc_CF9")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_C00 end

    def Function_6_D09(): pass

    label("Function_6_D09")


    AnonymousTalk(    #4
        "\x06どっから？\x02",
    )


    label("loc_D17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEF")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■最初から\x01",          # 0
            "■城・謁見の間\x01",      # 1
            "■対話×２\x01",          # 2
            "■発着場にて\x01",        # 3
            "■皇子の祝福\x01",        # 4
        )
    )

    MenuEnd(0x0)
    OP_E3(0x0, 0x6, 0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D94"),
        (1, "loc_DA3"),
        (2, "loc_DB2"),
        (3, "loc_DC1"),
        (4, "loc_DD0"),
        (SWITCH_DEFAULT, "loc_DDF"),
    )


    label("loc_D94")

    OP_A2(0x2504)
    NewScene("ED6_DT21/U4163   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_DEC")

    label("loc_DA3")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_DEC")

    label("loc_DB2")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T4221   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_DEC")

    label("loc_DC1")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_DEC")

    label("loc_DD0")

    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_DEC")

    label("loc_DDF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DEC")

    label("loc_DEC")

    Jump("loc_D17")

    label("loc_DEF")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_D09 end

    def Function_7_DFF(): pass

    label("Function_7_DFF")


    AnonymousTalk(    #5
        "\x06どっから？\x02",
    )


    label("loc_E0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F0C")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■最初から\x01",              # 0
            "■夕食後\x01",                # 1
            "■２日目・朝\x01",            # 2
            "■開発開始\x01",              # 3
            "■ＶＳエリカ\x01",            # 4
            "■オーバルギア完成\x01",      # 5
        )
    )

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x19, 64, 0x0)
    ClearParty()
    AddParty(0x6, 0xEE, 0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EA2"),
        (1, "loc_EB1"),
        (2, "loc_EC0"),
        (3, "loc_ECF"),
        (4, "loc_EDE"),
        (5, "loc_EED"),
        (SWITCH_DEFAULT, "loc_EFC"),
    )


    label("loc_EA2")

    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_F09")

    label("loc_EB1")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T3172   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_F09")

    label("loc_EC0")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_F09")

    label("loc_ECF")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T3115   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_F09")

    label("loc_EDE")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T3116   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_F09")

    label("loc_EED")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_F09")

    label("loc_EFC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F09")

    label("loc_F09")

    Jump("loc_E0D")

    label("loc_F0C")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_DFF end

    def Function_8_F1C(): pass

    label("Function_8_F1C")

    OP_A3(0x2F85)
    OP_A3(0x2F86)
    OP_A3(0x2F87)
    OP_A3(0x2F88)
    OP_A3(0x2F89)
    OP_A3(0x2F8A)
    OP_A3(0x2F8B)
    OP_A3(0x2F8C)
    OP_A3(0x2F8D)

    AnonymousTalk(    #6
        "\x06どっから？\x02",
    )


    label("loc_F45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1065")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■最初から\x01",                  # 0
            "■ギルドでエリカに会う\x01",      # 1
            "■地下実験場へ\x01",              # 2
            "■テスト開始\x01",                # 3
            "■オーバルギア暴走\x01",          # 4
            "■エピローグ\x01",                # 5
        )
    )

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x1A, 32, 0x0)
    ClearParty()
    AddParty(0x5, 0xEE, 0xFF)
    OP_C2(0x1, 0x1F)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_FEF"),
        (1, "loc_FFE"),
        (2, "loc_100D"),
        (3, "loc_101F"),
        (4, "loc_1031"),
        (5, "loc_1043"),
        (SWITCH_DEFAULT, "loc_1055"),
    )


    label("loc_FEF")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T3102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1062")

    label("loc_FFE")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1062")

    label("loc_100D")

    OP_A2(0x2F85)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1062")

    label("loc_101F")

    OP_A2(0x2F85)
    OP_A2(0x2507)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1062")

    label("loc_1031")

    OP_A2(0x2F85)
    OP_A2(0x250A)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1062")

    label("loc_1043")

    OP_A2(0x2F85)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1062")

    label("loc_1055")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1062")

    label("loc_1062")

    Jump("loc_F45")

    label("loc_1065")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_F1C end

    def Function_9_1075(): pass

    label("Function_9_1075")


    AnonymousTalk(    #7
        "\x06どっから？\x02",
    )

    OP_A3(0x2F4A)
    OP_A3(0x2F4B)
    OP_A3(0x2F4C)
    OP_A3(0x2F4D)
    OP_A3(0x2F4E)
    OP_A3(0x2F4F)
    OP_A3(0x2F50)
    OP_A3(0x2F51)
    OP_A3(0x2F52)
    OP_A3(0x2F53)
    OP_A3(0x2F54)
    OP_A3(0x2F55)
    OP_A3(0x2F56)
    OP_A3(0x2F57)
    OP_A3(0x2F58)
    OP_A3(0x2F59)
    OP_A3(0x2F5A)

    label("loc_10B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12DF")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■最初から\x01",                      # 0
            "■エーデル百貨店にて\x01",            # 1
            "■ホテル前にて\x01",                  # 2
            "■闘技場前\x01",                      # 3
            "■地下水道で回想\x01",                # 4
            "■地下から脱出する\x01",              # 5
            "■翌日グランセル城へ向かう\x01",      # 6
            "■城前、叔父との対決\x01",            # 7
            "■エピローグ\x01",                    # 8
        )
    )

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x7, 0, 0x0)
    ClearParty()
    AddParty(0x2, 0xEE, 0xFF)
    OP_BB(0x2, 0x1, 0x18)
    OP_BD()
    OP_C2(0x1, 0x4)
    OP_31(0x2, 0x0, 0xA)
    OP_31(0x2, 0xFE, 0x0)
    OP_41(0x2, 0x44E, 0xFF)
    OP_41(0x2, 0x63F, 0xFF)
    OP_41(0x2, 0x7F, 0xFF)
    OP_35(0x2, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11CE"),
        (1, "loc_11DA"),
        (2, "loc_11ED"),
        (3, "loc_1206"),
        (4, "loc_1222"),
        (5, "loc_123E"),
        (6, "loc_1260"),
        (7, "loc_1285"),
        (8, "loc_12AA"),
        (SWITCH_DEFAULT, "loc_12CF"),
    )


    label("loc_11CE")

    NewScene("ED6_DT21/T0135   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12DC")

    label("loc_11DA")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    NewScene("ED6_DT21/T4122   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12DC")

    label("loc_11ED")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    NewScene("ED6_DT21/T4103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12DC")

    label("loc_1206")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12DC")

    label("loc_1222")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    OP_A2(0x2F4D)
    NewScene("ED6_DT21/C4201   ._SN", 115, 0, 0)
    IdleLoop()
    Jump("loc_12DC")

    label("loc_123E")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    OP_A2(0x2F4D)
    OP_A2(0x2F4E)
    OP_A2(0x2F4F)
    NewScene("ED6_DT21/C4200   ._SN", 114, 0, 0)
    IdleLoop()
    Jump("loc_12DC")

    label("loc_1260")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    OP_A2(0x2F4D)
    OP_A2(0x2F4E)
    OP_A2(0x2F4F)
    OP_A2(0x2F50)
    NewScene("ED6_DT21/T4102   ._SN", 111, 0, 0)
    IdleLoop()
    Jump("loc_12DC")

    label("loc_1285")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    OP_A2(0x2F4D)
    OP_A2(0x2F4E)
    OP_A2(0x2F4F)
    OP_A2(0x2F50)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12DC")

    label("loc_12AA")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    OP_A2(0x2F4D)
    OP_A2(0x2F4E)
    OP_A2(0x2F4F)
    OP_A2(0x2F50)
    NewScene("ED6_DT21/T4150   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12DC")

    label("loc_12CF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12DC")

    label("loc_12DC")

    Jump("loc_10B6")

    label("loc_12DF")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_1075 end

    def Function_10_12EF(): pass

    label("Function_10_12EF")


    AnonymousTalk(    #8
        "\x06どっから？\x02",
    )

    OP_A3(0x2F65)
    OP_A3(0x2F66)
    OP_A3(0x2F67)
    OP_A3(0x2F68)
    OP_A3(0x2F69)
    OP_A3(0x2F6A)
    OP_A3(0x2F6B)
    OP_A3(0x2F6C)
    OP_A3(0x2F6D)
    OP_A3(0x2F6E)
    OP_A3(0x2F6F)
    OP_A3(0x2F70)
    OP_A3(0x2F71)
    OP_A3(0x2F72)
    OP_A3(0x2F73)
    OP_A3(0x2F74)
    OP_A3(0x2F75)
    OP_A3(0x2F76)
    OP_A3(0x2F77)
    OP_A3(0x2F78)
    OP_A3(0x2F79)
    OP_A3(0x2F7A)
    OP_A3(0x2F7B)
    OP_A3(0x2F7C)
    OP_A3(0x2F7D)
    OP_A3(0x2F7E)
    OP_A3(0x2F7F)
    OP_A3(0x2F80)
    OP_A3(0x2F81)
    OP_A3(0x2F82)
    OP_A3(0x2F83)
    OP_A3(0x2FA7)

    label("loc_135D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D7")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■最初から\x01",                # 0
            "■プリントを配る\x01",          # 1
            "■レクターを探せ\x01",          # 2
            "■定期試験\x01",                # 3
            "■ルーアンへ行こう\x01",        # 4
            "■クラムと会う\x01",            # 5
            "■ジルと喧嘩する\x01",          # 6
            "■ジル、ハンスに会う\x01",      # 7
            "■ジル、孤児院に行く\x01",      # 8
            "■エピローグ\x01",              # 9
        )
    )

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x8, 0, 0x0)
    ClearParty()
    AddParty(0x4, 0xEE, 0xFF)
    OP_BB(0x4, 0x1, 0x4)
    OP_BD()
    OP_C2(0x1, 0x1F)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1463"),
        (1, "loc_146F"),
        (2, "loc_147E"),
        (3, "loc_14A2"),
        (4, "loc_14C6"),
        (5, "loc_14ED"),
        (6, "loc_1514"),
        (7, "loc_153E"),
        (8, "loc_156D"),
        (9, "loc_1597"),
        (SWITCH_DEFAULT, "loc_15C7"),
    )


    label("loc_1463")

    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_15D4")

    label("loc_146F")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_15D4")

    label("loc_147E")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_15D4")

    label("loc_14A2")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_15D4")

    label("loc_14C6")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2F6C)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_15D4")

    label("loc_14ED")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2F6C)
    OP_A2(0x2F6D)
    NewScene("ED6_DT21/R2202   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_15D4")

    label("loc_1514")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2F6C)
    OP_A2(0x2F6D)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2800   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_15D4")

    label("loc_153E")

    ClearParty()
    AddParty(0x3A, 0xEE, 0xFF)
    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2F6C)
    OP_A2(0x2F6D)
    OP_A2(0x2F6E)
    NewScene("ED6_DT21/T2812   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_15D4")

    label("loc_156D")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2F6C)
    OP_A2(0x2F6D)
    OP_A2(0x2F6E)
    NewScene("ED6_DT21/T2400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_15D4")

    label("loc_1597")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2F6C)
    OP_A2(0x2F6D)
    OP_A2(0x2F6E)
    OP_A2(0x2F6F)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_15D4")

    label("loc_15C7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15D4")

    label("loc_15D4")

    Jump("loc_135D")

    label("loc_15D7")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_12EF end

    def Function_11_15E7(): pass

    label("Function_11_15E7")


    AnonymousTalk(    #9
        "\x06どっから？\x02",
    )

    OP_A3(0x2F17)
    OP_A3(0x2F18)
    OP_A3(0x2F19)
    OP_A3(0x2F1A)
    OP_A3(0x2F1B)
    OP_A3(0x2F1C)
    OP_A3(0x2F1D)
    OP_A3(0x2F1E)
    OP_A3(0x2F1F)
    OP_A3(0x2F20)
    OP_A3(0x2F21)
    OP_A3(0x2F22)
    OP_A3(0x2F23)
    OP_A3(0x2F24)
    OP_A3(0x2F25)
    OP_A3(0x2F26)
    OP_A3(0x2F28)
    OP_A3(0x2F29)
    OP_A3(0x2F3A)
    OP_A3(0x2F3B)
    OP_A3(0x2F3C)
    OP_A3(0x2F3D)
    OP_A3(0x2F3E)
    OP_A3(0x2F3F)
    OP_A3(0x2F40)
    OP_A3(0x2F41)
    OP_A3(0x2F42)
    OP_A3(0x2F43)
    OP_A3(0x2F44)
    OP_A3(0x2F45)

    label("loc_164F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B9")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■最初から\x01",                      # 0
            "■砂浜で貝殻を集める\x01",            # 1
            "■バザー会場にて\x01",                # 2
            "■マノリア間道で迷子になる\x01",      # 3
            "■クローネ峠で迷子になる\x01",        # 4
            "■薪を拾う\x01",                      # 5
            "■朝、魔獣がいない\x01",              # 6
            "■実は飛べるんです\x01",              # 7
            "■エピローグ\x01",                    # 8
        )
    )

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x9, 0, 0x0)
    ClearParty()
    AddParty(0x4D, 0xEE, 0xFF)
    OP_C2(0x1, 0x1F)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_174A"),
        (1, "loc_1756"),
        (2, "loc_1769"),
        (3, "loc_178E"),
        (4, "loc_17B6"),
        (5, "loc_17E3"),
        (6, "loc_1807"),
        (7, "loc_183D"),
        (8, "loc_1873"),
        (SWITCH_DEFAULT, "loc_18A9"),
    )


    label("loc_174A")

    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18B6")

    label("loc_1756")

    AddParty(0x4E, 0xFF, 0xFF)
    OP_A2(0x2F17)
    NewScene("ED6_DT21/R2200   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_18B6")

    label("loc_1769")

    AddParty(0x4E, 0xFF, 0xFF)
    OP_A2(0x2F17)
    OP_A2(0x2F1B)
    OP_A2(0x2F1C)
    OP_A2(0x2F1D)
    OP_A2(0x2F1E)
    OP_A2(0x2F1F)
    OP_A2(0x2F20)
    NewScene("ED6_DT21/T2310   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_18B6")

    label("loc_178E")

    AddParty(0x4E, 0xFF, 0xFF)
    OP_A2(0x2F17)
    OP_A2(0x2F1B)
    OP_A2(0x2F1C)
    OP_A2(0x2F1D)
    OP_A2(0x2F1E)
    OP_A2(0x2F1F)
    OP_A2(0x2F20)
    OP_A2(0x2F21)
    NewScene("ED6_DT21/R2101   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_18B6")

    label("loc_17B6")

    OP_A2(0x2F17)
    OP_A2(0x2F1B)
    OP_A2(0x2F1C)
    OP_A2(0x2F1D)
    OP_A2(0x2F1E)
    OP_A2(0x2F1F)
    OP_A2(0x2F20)
    OP_A2(0x2F21)
    OP_A2(0x2F22)
    OP_A2(0x2F23)
    OP_A2(0x2F24)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18B6")

    label("loc_17E3")

    OP_A2(0x2F17)
    OP_A2(0x2F20)
    OP_A2(0x2F21)
    OP_A2(0x2F22)
    OP_A2(0x2F23)
    OP_A2(0x2F24)
    OP_A2(0x2F25)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18B6")

    label("loc_1807")

    OP_A2(0x2F17)
    OP_A2(0x2F1B)
    OP_A2(0x2F1C)
    OP_A2(0x2F1D)
    OP_A2(0x2F1E)
    OP_A2(0x2F1F)
    OP_A2(0x2F20)
    OP_A2(0x2F21)
    OP_A2(0x2F22)
    OP_A2(0x2F23)
    OP_A2(0x2F24)
    OP_A2(0x2F25)
    OP_A2(0x2F26)
    OP_A2(0x2506)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18B6")

    label("loc_183D")

    OP_A2(0x2F17)
    OP_A2(0x2F1B)
    OP_A2(0x2F1C)
    OP_A2(0x2F1D)
    OP_A2(0x2F1E)
    OP_A2(0x2F1F)
    OP_A2(0x2F20)
    OP_A2(0x2F21)
    OP_A2(0x2F22)
    OP_A2(0x2F23)
    OP_A2(0x2F24)
    OP_A2(0x2F25)
    OP_A2(0x2F26)
    OP_A2(0x2506)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18B6")

    label("loc_1873")

    OP_A2(0x2F17)
    OP_A2(0x2F1B)
    OP_A2(0x2F1C)
    OP_A2(0x2F1D)
    OP_A2(0x2F1E)
    OP_A2(0x2F1F)
    OP_A2(0x2F20)
    OP_A2(0x2F21)
    OP_A2(0x2F22)
    OP_A2(0x2F23)
    OP_A2(0x2F24)
    OP_A2(0x2F25)
    OP_A2(0x2F26)
    OP_A2(0x2504)
    NewScene("ED6_DT21/R2101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18B6")

    label("loc_18A9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18B6")

    label("loc_18B6")

    Jump("loc_164F")

    label("loc_18B9")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_15E7 end

    def Function_12_18C9(): pass

    label("Function_12_18C9")


    AnonymousTalk(    #10
        "\x06どっから？\x02",
    )

    OP_A3(0x2F60)
    OP_A3(0x2F61)
    OP_A3(0x2F62)

    label("loc_18E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A15")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■最初から\x01",                # 0
            "■２週目\x01",                  # 1
            "■夜・カシウスと話す\x01",      # 2
            "■パーゼル農園にて\x01",        # 3
            "■芳香剤を作る\x01",            # 4
            "■ミストヴァルトの森\x01",      # 5
            "■エピローグ\x01",              # 6
        )
    )

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x11, 0, 0x0)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_BB(0x0, 0x1, 0x44)
    OP_BD()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_19A2"),
        (1, "loc_19AE"),
        (2, "loc_19BD"),
        (3, "loc_19C9"),
        (4, "loc_19D5"),
        (5, "loc_19E1"),
        (6, "loc_19F3"),
        (SWITCH_DEFAULT, "loc_1A05"),
    )


    label("loc_19A2")

    NewScene("ED6_DT21/T0311   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A12")

    label("loc_19AE")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A12")

    label("loc_19BD")

    NewScene("ED6_DT21/T0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A12")

    label("loc_19C9")

    NewScene("ED6_DT21/R0201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A12")

    label("loc_19D5")

    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A12")

    label("loc_19E1")

    OP_A2(0x2F61)
    OP_A2(0x2F62)
    NewScene("ED6_DT21/C0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A12")

    label("loc_19F3")

    OP_A2(0x2F61)
    OP_A2(0x2F62)
    NewScene("ED6_DT21/T0700   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A12")

    label("loc_1A05")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A12")

    label("loc_1A12")

    Jump("loc_18E0")

    label("loc_1A15")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_18C9 end

    def Function_13_1A25(): pass

    label("Function_13_1A25")


    AnonymousTalk(    #11
        "\x06どっから？\x02",
    )


    label("loc_1A33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ADC")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■最初から\x01",                # 0
            "■夜・発着場に向かう\x01",      # 1
            "■翌日\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x14, 2048, 0x0)
    ClearParty()
    AddParty(0xB, 0xEE, 0xFF)
    OP_BB(0xB, 0x1, 0x53)
    OP_BD()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A9F"),
        (1, "loc_1AAE"),
        (2, "loc_1ABD"),
        (SWITCH_DEFAULT, "loc_1ACC"),
    )


    label("loc_1A9F")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1AD9")

    label("loc_1AAE")

    OP_A2(0x2506)
    NewScene("ED6_DT21/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1AD9")

    label("loc_1ABD")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T2102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1AD9")

    label("loc_1ACC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AD9")

    label("loc_1AD9")

    Jump("loc_1A33")

    label("loc_1ADC")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_1A25 end

    def Function_14_1AEC(): pass

    label("Function_14_1AEC")


    AnonymousTalk(    #12
        "\x06どこ？\x02",
    )


    label("loc_1AF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE4")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T3100  工房都市ツァイス外部（街区）\x01",             # 0
            "T3111  工房都市ツァイス内部（工房区）B1/1F\x01",      # 1
            "T3133  ラッセル工房\x01",                             # 2
            "T3121  (新規）地下実験場\x01",                        # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BA4"),
        (1, "loc_1BB0"),
        (2, "loc_1BBC"),
        (3, "loc_1BC8"),
        (SWITCH_DEFAULT, "loc_1BD4"),
    )


    label("loc_1BA4")

    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1BE1")

    label("loc_1BB0")

    NewScene("ED6_DT21/T3111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1BE1")

    label("loc_1BBC")

    NewScene("ED6_DT21/T3133   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1BE1")

    label("loc_1BC8")

    NewScene("ED6_DT21/T3121   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BE1")

    label("loc_1BD4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BE1")

    label("loc_1BE1")

    Jump("loc_1AF6")

    label("loc_1BE4")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_1AEC end

    def Function_15_1BF4(): pass

    label("Function_15_1BF4")


    AnonymousTalk(    #13
        "\x06どこ？\x02",
    )


    label("loc_1BFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C68")

    Menu(
        4,
        -1,
        -1,
        1,
        "R1204 （新規）西ボース街道（R1203改造）\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C4C"),
        (SWITCH_DEFAULT, "loc_1C58"),
    )


    label("loc_1C4C")

    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C65")

    label("loc_1C58")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C65")

    label("loc_1C65")

    Jump("loc_1BFE")

    label("loc_1C68")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_1BF4 end

    def Function_16_1C78(): pass

    label("Function_16_1C78")


    AnonymousTalk(    #14
        "\x06どこ？\x02",
    )


    label("loc_1C82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D5B")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "C3100  工房都市ツァイス外部（街区）\x01",             # 0
            "C3101  工房都市ツァイス内部（工房区）B1/1F\x01",      # 1
            "C3110  レイストン水上要塞内部（司令塔）\x01",         # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D27"),
        (1, "loc_1D33"),
        (2, "loc_1D3F"),
        (SWITCH_DEFAULT, "loc_1D4B"),
    )


    label("loc_1D27")

    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1D58")

    label("loc_1D33")

    NewScene("ED6_DT21/C3101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1D58")

    label("loc_1D3F")

    NewScene("ED6_DT21/C3110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1D58")

    label("loc_1D4B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D58")

    label("loc_1D58")

    Jump("loc_1C82")

    label("loc_1D5B")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_1C78 end

    def Function_17_1D6B(): pass

    label("Function_17_1D6B")


    AnonymousTalk(    #15
        "\x06どこ？\x02",
    )


    label("loc_1D75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E80")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "C5400  グロリアス内部（エステル監禁部屋）\x01",      # 0
            "C5407  グロリアス内部　エレベーター箱\x01",          # 1
            "C5401  グロリアス内部（ワイスマンの間）\x01",        # 2
            "C5408  グロリアス外装（甲板）\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E3D"),
        (1, "loc_1E4C"),
        (2, "loc_1E58"),
        (3, "loc_1E64"),
        (SWITCH_DEFAULT, "loc_1E70"),
    )


    label("loc_1E3D")

    OP_A2(0x2504)
    NewScene("ED6_DT21/C5400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1E7D")

    label("loc_1E4C")

    NewScene("ED6_DT21/C5407   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1E7D")

    label("loc_1E58")

    NewScene("ED6_DT21/C5401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1E7D")

    label("loc_1E64")

    NewScene("ED6_DT21/C5408   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E7D")

    label("loc_1E70")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E7D")

    label("loc_1E7D")

    Jump("loc_1D75")

    label("loc_1E80")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_1D6B end

    def Function_18_1E90(): pass

    label("Function_18_1E90")


    AnonymousTalk(    #16
        "\x06どこ？\x02",
    )


    label("loc_1E9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F8A")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T4101  王都グランセル外部（東街区）\x01",      # 0
            "T4138  帝國大使館内部\x01",                    # 1
            "T4200  グランセル城外部(町と接続)\x01",        # 2
            "T4220  グランセル城内部(謁見の間)\x01",        # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F4A"),
        (1, "loc_1F56"),
        (2, "loc_1F62"),
        (3, "loc_1F6E"),
        (SWITCH_DEFAULT, "loc_1F7A"),
    )


    label("loc_1F4A")

    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1F87")

    label("loc_1F56")

    NewScene("ED6_DT21/T4138   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1F87")

    label("loc_1F62")

    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1F87")

    label("loc_1F6E")

    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1F87")

    label("loc_1F7A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F87")

    label("loc_1F87")

    Jump("loc_1E9A")

    label("loc_1F8A")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_1E90 end

    def Function_19_1F9A(): pass

    label("Function_19_1F9A")


    AnonymousTalk(    #17
        "\x06どこ？\x02",
    )


    label("loc_1FA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2009")

    Menu(
        4,
        -1,
        -1,
        1,
        "R4103  キルシェ通り王都前（夜）\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1FEA"),
        (SWITCH_DEFAULT, "loc_1FF9"),
    )


    label("loc_1FEA")

    OP_A2(0x2504)
    NewScene("ED6_DT21/R4103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2006")

    label("loc_1FF9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2006")

    label("loc_2006")

    Jump("loc_1FA4")

    label("loc_2009")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_19_1F9A end

    def Function_20_2019(): pass

    label("Function_20_2019")


    AnonymousTalk(    #18
        "\x06どこ？\x02",
    )


    label("loc_2023")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2083")

    Menu(
        4,
        -1,
        -1,
        1,
        "T4210  グランセル城内部(広間)\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2067"),
        (SWITCH_DEFAULT, "loc_2073"),
    )


    label("loc_2067")

    NewScene("ED6_DT21/T4210   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2080")

    label("loc_2073")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2080")

    label("loc_2080")

    Jump("loc_2023")

    label("loc_2083")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #19
        "\x06どこ？\x02",
    )

    Return()

    # Function_20_2019 end

    def Function_21_209D(): pass

    label("Function_21_209D")


    AnonymousTalk(    #20
        "\x06どこ？\x02",
    )


    label("loc_20A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2188")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T0100  ロレント外部\x01",                          # 0
            "T0101  (夜)ロレント外部\x01",                      # 1
            "T0121  商店１F・２F、遊撃士協会１F・２F\x01",      # 2
            "T0135  (夜)酒場、厨房、２F\x01",                   # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2148"),
        (1, "loc_2154"),
        (2, "loc_2160"),
        (3, "loc_216C"),
        (SWITCH_DEFAULT, "loc_2178"),
    )


    label("loc_2148")

    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2185")

    label("loc_2154")

    NewScene("ED6_DT21/T0101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2185")

    label("loc_2160")

    NewScene("ED6_DT21/T0121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2185")

    label("loc_216C")

    NewScene("ED6_DT21/T0135   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2185")

    label("loc_2178")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2185")

    label("loc_2185")

    Jump("loc_20A7")

    label("loc_2188")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_209D end

    def Function_22_2198(): pass

    label("Function_22_2198")


    AnonymousTalk(    #21
        "\x06どこ？\x02",
    )


    label("loc_21A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2274")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T3200  エルモ外部\x01",                # 0
            "T3201  エルモ外部（夜）\x01",          # 1
            "T3221  エルモ内部（宿屋）\x01",        # 2
            "T3223  エルモ内部（宿屋夜）\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2234"),
        (1, "loc_2240"),
        (2, "loc_224C"),
        (3, "loc_2258"),
        (SWITCH_DEFAULT, "loc_2264"),
    )


    label("loc_2234")

    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2271")

    label("loc_2240")

    NewScene("ED6_DT21/T3201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2271")

    label("loc_224C")

    NewScene("ED6_DT21/T3221   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2271")

    label("loc_2258")

    NewScene("ED6_DT21/T3223   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2271")

    label("loc_2264")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2271")

    label("loc_2271")

    Jump("loc_21A2")

    label("loc_2274")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_2198 end

    def Function_23_2284(): pass

    label("Function_23_2284")


    AnonymousTalk(    #22
        "\x06どこ？\x02",
    )


    label("loc_228E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_239D")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "E0810  スカイボックス（空壁あり）＜前半＞\x01",      # 0
            "E0102 （新規）飛行船（空賊用）外側昼\x01",           # 1
            "E0110  飛行船（空賊用夜）内部\x01",                  # 2
            "E0810  スカイボックス（空壁あり）＜後半＞\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2357"),
        (1, "loc_2366"),
        (2, "loc_2372"),
        (3, "loc_237E"),
        (SWITCH_DEFAULT, "loc_238D"),
    )


    label("loc_2357")

    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_239A")

    label("loc_2366")

    NewScene("ED6_DT21/E0102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_239A")

    label("loc_2372")

    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_239A")

    label("loc_237E")

    OP_A2(0x2505)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_239A")

    label("loc_238D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239A")

    label("loc_239A")

    Jump("loc_228E")

    label("loc_239D")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_23_2284 end

    def Function_24_23AD(): pass

    label("Function_24_23AD")


    AnonymousTalk(    #23
        "\x06どこ？\x02",
    )


    label("loc_23B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_241B")

    Menu(
        4,
        -1,
        -1,
        1,
        "T4142  酒場　リベール通信社（夜）\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23FF"),
        (SWITCH_DEFAULT, "loc_240B"),
    )


    label("loc_23FF")

    NewScene("ED6_DT21/T4142   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2418")

    label("loc_240B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2418")

    label("loc_2418")

    Jump("loc_23B7")

    label("loc_241B")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_24_23AD end

    def Function_25_242B(): pass

    label("Function_25_242B")


    AnonymousTalk(    #24
        "\x06どこ？\x02",
    )


    label("loc_2435")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24A6")

    Menu(
        4,
        -1,
        -1,
        1,
        "T4206 （新規）グランセル城外部(空中庭園)（夜）\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_248A"),
        (SWITCH_DEFAULT, "loc_2496"),
    )


    label("loc_248A")

    NewScene("ED6_DT21/T4206   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_24A3")

    label("loc_2496")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24A3")

    label("loc_24A3")

    Jump("loc_2435")

    label("loc_24A6")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_25_242B end

    def Function_26_24B6(): pass

    label("Function_26_24B6")


    AnonymousTalk(    #25
        "\x06どこ？\x02",
    )


    label("loc_24C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2591")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "C5408  グロリアス外装（甲板）\x01",                 # 0
            "C5401  グロリアス内部（ワイスマンの間）\x01",       # 1
            "C5416 （新規）グロリアス内部（星辰の間）\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_255D"),
        (1, "loc_2569"),
        (2, "loc_2575"),
        (SWITCH_DEFAULT, "loc_2581"),
    )


    label("loc_255D")

    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_258E")

    label("loc_2569")

    NewScene("ED6_DT21/C5401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_258E")

    label("loc_2575")

    NewScene("ED6_DT21/C5416   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_258E")

    label("loc_2581")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_258E")

    label("loc_258E")

    Jump("loc_24C0")

    label("loc_2591")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_26_24B6 end

    def Function_27_25A1(): pass

    label("Function_27_25A1")


    AnonymousTalk(    #26
        (
            "\x06！注意！\x01",
            "※保留項目のためジャンプできません。あしからず。\x02",
        )
    )


    label("loc_25DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2633")

    Menu(
        4,
        -1,
        -1,
        1,
        "R2201  メーヴェ海道（中央）\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2620"),
        (SWITCH_DEFAULT, "loc_2623"),
    )


    label("loc_2620")

    Jump("loc_2630")

    label("loc_2623")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2630")

    label("loc_2630")

    Jump("loc_25DE")

    label("loc_2633")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_27_25A1 end

    def Function_28_2643(): pass

    label("Function_28_2643")


    AnonymousTalk(    #27
        "\x06どこ？\x02",
    )


    label("loc_264D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27B5")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "C3101  レイストン水上要塞外観(中庭)）\x01",        # 0
            "C3110  レイストン水上要塞内部（司令塔）\x01",      # 1
            "C3102  レイストン水上要塞外観(格納庫)\x01",        # 2
            "E0610  紅い高速飛行艇内部\x01",                    # 3
            "E0810  スカイボックス（空壁あり）\x01",            # 4
            "T4202  グランセル城外部(女王のテラス)\x01",        # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_275D"),
        (1, "loc_2769"),
        (2, "loc_2775"),
        (3, "loc_2781"),
        (4, "loc_278D"),
        (5, "loc_2799"),
        (SWITCH_DEFAULT, "loc_27A5"),
    )


    label("loc_275D")

    NewScene("ED6_DT21/C3101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_27B2")

    label("loc_2769")

    NewScene("ED6_DT21/C3110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_27B2")

    label("loc_2775")

    NewScene("ED6_DT21/C3102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_27B2")

    label("loc_2781")

    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_27B2")

    label("loc_278D")

    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_27B2")

    label("loc_2799")

    NewScene("ED6_DT21/T4202   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_27B2")

    label("loc_27A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27B2")

    label("loc_27B2")

    Jump("loc_264D")

    label("loc_27B5")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_28_2643 end

    def Function_29_27C5(): pass

    label("Function_29_27C5")


    AnonymousTalk(    #28
        "\x06どこ？\x02",
    )


    label("loc_27CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2899")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T4220  グランセル城内部(謁見の間)\x01",          # 0
            "T4230  グランセル城内部(女王宮)\x01",            # 1
            "T4202  グランセル城外部(女王のテラス)\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2865"),
        (1, "loc_2871"),
        (2, "loc_287D"),
        (SWITCH_DEFAULT, "loc_2889"),
    )


    label("loc_2865")

    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2896")

    label("loc_2871")

    NewScene("ED6_DT21/T4230   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2896")

    label("loc_287D")

    NewScene("ED6_DT21/T4202   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2896")

    label("loc_2889")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2896")

    label("loc_2896")

    Jump("loc_27CF")

    label("loc_2899")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_29_27C5 end

    def Function_30_28A9(): pass

    label("Function_30_28A9")


    AnonymousTalk(    #29
        "\x06どこ？\x02",
    )


    label("loc_28B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28FE")

    Menu(
        4,
        -1,
        -1,
        1,
        "？？？？\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_28E2"),
        (SWITCH_DEFAULT, "loc_28EE"),
    )


    label("loc_28E2")

    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_28FB")

    label("loc_28EE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28FB")

    label("loc_28FB")

    Jump("loc_28B3")

    label("loc_28FE")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_30_28A9 end

    def Function_31_290E(): pass

    label("Function_31_290E")


    AnonymousTalk(    #30
        "\x06どこ？\x02",
    )


    label("loc_2918")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A31")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T4400  王都グランセル外部（波止場１）\x01",                       # 0
            "T4401  王都グランセル外部（波止場２）\x01",                       # 1
            "T4106  グランセル飛行場(アルセイユ無し)/(緑)セシリア号\x01",      # 2
            "T4100  王都グランセル外部（南街区）\x01",                         # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29F1"),
        (1, "loc_29FD"),
        (2, "loc_2A09"),
        (3, "loc_2A15"),
        (SWITCH_DEFAULT, "loc_2A21"),
    )


    label("loc_29F1")

    NewScene("ED6_DT21/T4400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2A2E")

    label("loc_29FD")

    NewScene("ED6_DT21/T4401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2A2E")

    label("loc_2A09")

    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2A2E")

    label("loc_2A15")

    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2A2E")

    label("loc_2A21")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A2E")

    label("loc_2A2E")

    Jump("loc_2918")

    label("loc_2A31")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_31_290E end

    def Function_32_2A41(): pass

    label("Function_32_2A41")


    AnonymousTalk(    #31
        "\x06どこ？\x02",
    )


    label("loc_2A4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AE4")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T2402  マーシア孤児院外部（再建後）\x01",      # 0
            "T2412  マーシア孤児院内部（再建後)\x01",       # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2ABC"),
        (1, "loc_2AC8"),
        (SWITCH_DEFAULT, "loc_2AD4"),
    )


    label("loc_2ABC")

    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AE1")

    label("loc_2AC8")

    NewScene("ED6_DT21/T2412   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AE1")

    label("loc_2AD4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AE1")

    label("loc_2AE1")

    Jump("loc_2A4B")

    label("loc_2AE4")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_32_2A41 end

    def Function_33_2AF4(): pass

    label("Function_33_2AF4")


    AnonymousTalk(    #32
        "\x06どこ？\x02",
    )


    label("loc_2AFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C22")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T2500  ジェニス王立学院外部\x01",                  # 0
            "T2510  ジェニス王立学院（本館）\x01",              # 1
            "T2511  ジェニス王立学院（クラブハウス）\x01",      # 2
            "T2512  ジェニス王立学院（寮）\x01",                # 3
            "T2513  ジェニス王立学院（講堂）\x01",              # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2BD6"),
        (1, "loc_2BE2"),
        (2, "loc_2BEE"),
        (3, "loc_2BFA"),
        (4, "loc_2C06"),
        (SWITCH_DEFAULT, "loc_2C12"),
    )


    label("loc_2BD6")

    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2C1F")

    label("loc_2BE2")

    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2C1F")

    label("loc_2BEE")

    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2C1F")

    label("loc_2BFA")

    NewScene("ED6_DT21/T2512   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2C1F")

    label("loc_2C06")

    NewScene("ED6_DT21/T2513   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2C1F")

    label("loc_2C12")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C1F")

    label("loc_2C1F")

    Jump("loc_2AFE")

    label("loc_2C22")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_33_2AF4 end

    def Function_34_2C32(): pass

    label("Function_34_2C32")


    AnonymousTalk(    #33
        "\x06どこ？\x02",
    )


    label("loc_2C3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D0E")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T1101  ボース外部　北\x01",            # 0
            "T1100  ボース外部　南\x01",            # 1
            "T1122  ボースマーケット内部\x01",      # 2
            "T1111  ボース市長邸内部\x01",          # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2CCE"),
        (1, "loc_2CDA"),
        (2, "loc_2CE6"),
        (3, "loc_2CF2"),
        (SWITCH_DEFAULT, "loc_2CFE"),
    )


    label("loc_2CCE")

    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D0B")

    label("loc_2CDA")

    NewScene("ED6_DT21/T1100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D0B")

    label("loc_2CE6")

    NewScene("ED6_DT21/T1122   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D0B")

    label("loc_2CF2")

    NewScene("ED6_DT21/T1111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D0B")

    label("loc_2CFE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D0B")

    label("loc_2D0B")

    Jump("loc_2C3C")

    label("loc_2D0E")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_34_2C32 end

    def Function_35_2D1E(): pass

    label("Function_35_2D1E")


    AnonymousTalk(    #34
        "\x06どこ？\x02",
    )


    label("loc_2D28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E6D")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T4200  グランセル城外部(町と接続)\x01",                           # 0
            "T4106  グランセル飛行場(アルセイユ無し)/(白)アルセイユ\x01",      # 1
            "T4213  グランセル城内部(親衛隊詰所)\x01",                         # 2
            "T4214  グランセル城内部(メイド部屋)\x01",                         # 3
            "T4201  グランセル城外部(空中庭園)\x01",                           # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E21"),
        (1, "loc_2E2D"),
        (2, "loc_2E39"),
        (3, "loc_2E45"),
        (4, "loc_2E51"),
        (SWITCH_DEFAULT, "loc_2E5D"),
    )


    label("loc_2E21")

    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E6A")

    label("loc_2E2D")

    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E6A")

    label("loc_2E39")

    NewScene("ED6_DT21/T4213   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E6A")

    label("loc_2E45")

    NewScene("ED6_DT21/T4214   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E6A")

    label("loc_2E51")

    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E6A")

    label("loc_2E5D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E6A")

    label("loc_2E6A")

    Jump("loc_2D28")

    label("loc_2E6D")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_2D1E end

    def Function_36_2E7D(): pass

    label("Function_36_2E7D")


    AnonymousTalk(    #35
        "\x06どこ？\x02",
    )


    label("loc_2E87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EF1")

    Menu(
        4,
        -1,
        -1,
        1,
        "C3110  レイストン水上要塞内部（司令塔）\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2ED5"),
        (SWITCH_DEFAULT, "loc_2EE1"),
    )


    label("loc_2ED5")

    NewScene("ED6_DT21/C3110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2EEE")

    label("loc_2EE1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EEE")

    label("loc_2EEE")

    Jump("loc_2E87")

    label("loc_2EF1")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_36_2E7D end

    def Function_37_2F01(): pass

    label("Function_37_2F01")


    AnonymousTalk(    #36
        "\x06どこ？\x02",
    )


    label("loc_2F0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3092")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "R0100  エリーズ街道(ロレント側、ブライト家)\x01",      # 0
            "T0100  ロレント外部\x01",                              # 1
            "T0120  武器屋１F・２F、工房\x01",                      # 2
            "T0121  商店１F・２F、遊撃士協会１F・２F\x01",          # 3
            "T0131  酒場、厨房、２F\x01",                           # 4
            "T0700  ロレント飛行場(セシリア号停泊中)\x01",          # 5
            "E0810  スカイボックス（空壁あり）\x01",                # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_302E"),
        (1, "loc_303A"),
        (2, "loc_3046"),
        (3, "loc_3052"),
        (4, "loc_305E"),
        (5, "loc_306A"),
        (6, "loc_3076"),
        (SWITCH_DEFAULT, "loc_3082"),
    )


    label("loc_302E")

    NewScene("ED6_DT21/R0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_308F")

    label("loc_303A")

    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_308F")

    label("loc_3046")

    NewScene("ED6_DT21/T0120   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_308F")

    label("loc_3052")

    NewScene("ED6_DT21/T0121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_308F")

    label("loc_305E")

    NewScene("ED6_DT21/T0131   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_308F")

    label("loc_306A")

    NewScene("ED6_DT21/T0700   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_308F")

    label("loc_3076")

    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_308F")

    label("loc_3082")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_308F")

    label("loc_308F")

    Jump("loc_2F0B")

    label("loc_3092")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_37_2F01 end

    def Function_38_30A2(): pass

    label("Function_38_30A2")


    AnonymousTalk(    #37
        "\x06どこ？\x02",
    )


    label("loc_30AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30F7")

    Menu(
        4,
        -1,
        -1,
        1,
        "？？？？\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30DB"),
        (SWITCH_DEFAULT, "loc_30E7"),
    )


    label("loc_30DB")

    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_30F4")

    label("loc_30E7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30F4")

    label("loc_30F4")

    Jump("loc_30AC")

    label("loc_30F7")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_38_30A2 end

    def Function_39_3107(): pass

    label("Function_39_3107")


    AnonymousTalk(    #38
        "\x06どこ？\x02",
    )


    label("loc_3111")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_315C")

    Menu(
        4,
        -1,
        -1,
        1,
        "？？？？\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3140"),
        (SWITCH_DEFAULT, "loc_314C"),
    )


    label("loc_3140")

    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3159")

    label("loc_314C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3159")

    label("loc_3159")

    Jump("loc_3111")

    label("loc_315C")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_39_3107 end

    def Function_40_316C(): pass

    label("Function_40_316C")


    AnonymousTalk(    #39
        "\x06どこ？\x02",
    )


    label("loc_3176")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31C1")

    Menu(
        4,
        -1,
        -1,
        1,
        "？？？？\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31A5"),
        (SWITCH_DEFAULT, "loc_31B1"),
    )


    label("loc_31A5")

    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_31BE")

    label("loc_31B1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31BE")

    label("loc_31BE")

    Jump("loc_3176")

    label("loc_31C1")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_40_316C end

    def Function_41_31D1(): pass

    label("Function_41_31D1")


    AnonymousTalk(    #40
        "\x06どこ？\x02",
    )


    label("loc_31DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3226")

    Menu(
        4,
        -1,
        -1,
        1,
        "？？？？\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_320A"),
        (SWITCH_DEFAULT, "loc_3216"),
    )


    label("loc_320A")

    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3223")

    label("loc_3216")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3223")

    label("loc_3223")

    Jump("loc_31DB")

    label("loc_3226")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_41_31D1 end

    def Function_42_3236(): pass

    label("Function_42_3236")


    AnonymousTalk(    #41
        "\x06どこ？\x02",
    )


    label("loc_3240")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_328B")

    Menu(
        4,
        -1,
        -1,
        1,
        "？？？？\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_326F"),
        (SWITCH_DEFAULT, "loc_327B"),
    )


    label("loc_326F")

    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3288")

    label("loc_327B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3288")

    label("loc_3288")

    Jump("loc_3240")

    label("loc_328B")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_42_3236 end

    def Function_43_329B(): pass

    label("Function_43_329B")

    OP_28(0x1, 0x4, 0x4)
    OP_28(0x1, 0x4, 0x2)
    OP_28(0x1, 0x4, 0x8)
    OP_28(0x1, 0x4, 0x10)
    OP_28(0x1, 0x4, 0x20)
    OP_28(0x1, 0x1, 0x1)
    OP_28(0x1, 0x1, 0x2)
    OP_28(0x1, 0x1, 0x4)
    OP_28(0x1, 0x1, 0x8)
    OP_28(0x1, 0x1, 0x10)
    OP_28(0x1, 0x1, 0x20)
    OP_28(0x1, 0x1, 0x40)
    OP_28(0x1, 0x1, 0x80)
    OP_28(0x1, 0x1, 0x100)
    OP_28(0x1, 0x1, 0x200)
    OP_28(0x1, 0x1, 0x400)
    OP_28(0x1, 0x1, 0x800)
    OP_28(0x1, 0x1, 0x1000)
    OP_28(0x1, 0x1, 0x2000)
    OP_28(0x1, 0x1, 0x4000)
    OP_28(0x1, 0x1, 0x8000)
    OP_28(0x2, 0x4, 0x4)
    OP_28(0x2, 0x4, 0x2)
    OP_28(0x2, 0x4, 0x8)
    OP_28(0x2, 0x4, 0x10)
    OP_28(0x2, 0x4, 0x20)
    OP_28(0x2, 0x1, 0x1)
    OP_28(0x2, 0x1, 0x2)
    OP_28(0x2, 0x1, 0x4)
    OP_28(0x2, 0x1, 0x8)
    OP_28(0x2, 0x1, 0x10)
    OP_28(0x2, 0x1, 0x20)
    OP_28(0x2, 0x1, 0x40)
    OP_28(0x2, 0x1, 0x80)
    OP_28(0x2, 0x1, 0x100)
    OP_28(0x2, 0x1, 0x200)
    OP_28(0x2, 0x1, 0x400)
    OP_28(0x2, 0x1, 0x800)
    OP_28(0x2, 0x1, 0x1000)
    OP_28(0x2, 0x1, 0x2000)
    OP_28(0x2, 0x1, 0x4000)
    OP_28(0x2, 0x1, 0x8000)
    OP_28(0x3, 0x4, 0x4)
    OP_28(0x3, 0x4, 0x2)
    OP_28(0x3, 0x4, 0x8)
    OP_28(0x3, 0x4, 0x10)
    OP_28(0x3, 0x4, 0x20)
    OP_28(0x3, 0x1, 0x1)
    OP_28(0x3, 0x1, 0x2)
    OP_28(0x3, 0x1, 0x4)
    OP_28(0x3, 0x1, 0x8)
    OP_28(0x3, 0x1, 0x10)
    OP_28(0x3, 0x1, 0x20)
    OP_28(0x3, 0x1, 0x40)
    OP_28(0x3, 0x1, 0x80)
    OP_28(0x3, 0x1, 0x100)
    OP_28(0x3, 0x1, 0x200)
    OP_28(0x3, 0x1, 0x400)
    OP_28(0x3, 0x1, 0x800)
    OP_28(0x3, 0x1, 0x1000)
    OP_28(0x3, 0x1, 0x2000)
    OP_28(0x3, 0x1, 0x4000)
    OP_28(0x3, 0x1, 0x8000)
    OP_28(0x4, 0x4, 0x4)
    OP_28(0x4, 0x4, 0x2)
    OP_28(0x4, 0x4, 0x8)
    OP_28(0x4, 0x4, 0x10)
    OP_28(0x4, 0x4, 0x20)
    OP_28(0x4, 0x1, 0x1)
    OP_28(0x4, 0x1, 0x2)
    OP_28(0x4, 0x1, 0x4)
    OP_28(0x4, 0x1, 0x8)
    OP_28(0x4, 0x1, 0x10)
    OP_28(0x4, 0x1, 0x20)
    OP_28(0x4, 0x1, 0x40)
    OP_28(0x4, 0x1, 0x80)
    OP_28(0x4, 0x1, 0x100)
    OP_28(0x4, 0x1, 0x200)
    OP_28(0x4, 0x1, 0x400)
    OP_28(0x4, 0x1, 0x800)
    OP_28(0x4, 0x1, 0x1000)
    OP_28(0x4, 0x1, 0x2000)
    OP_28(0x4, 0x1, 0x4000)
    OP_28(0x4, 0x1, 0x8000)
    OP_28(0x5, 0x4, 0x4)
    OP_28(0x5, 0x4, 0x2)
    OP_28(0x5, 0x4, 0x8)
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x5, 0x4, 0x20)
    OP_28(0x5, 0x1, 0x1)
    OP_28(0x5, 0x1, 0x2)
    OP_28(0x5, 0x1, 0x4)
    OP_28(0x5, 0x1, 0x8)
    OP_28(0x5, 0x1, 0x10)
    OP_28(0x5, 0x1, 0x20)
    OP_28(0x5, 0x1, 0x40)
    OP_28(0x5, 0x1, 0x80)
    OP_28(0x5, 0x1, 0x100)
    OP_28(0x5, 0x1, 0x200)
    OP_28(0x5, 0x1, 0x400)
    OP_28(0x5, 0x1, 0x800)
    OP_28(0x5, 0x1, 0x1000)
    OP_28(0x5, 0x1, 0x2000)
    OP_28(0x5, 0x1, 0x4000)
    OP_28(0x5, 0x1, 0x8000)
    OP_28(0x6, 0x4, 0x4)
    OP_28(0x6, 0x4, 0x2)
    OP_28(0x6, 0x4, 0x8)
    OP_28(0x6, 0x4, 0x10)
    OP_28(0x6, 0x4, 0x20)
    OP_28(0x6, 0x1, 0x1)
    OP_28(0x6, 0x1, 0x2)
    OP_28(0x6, 0x1, 0x4)
    OP_28(0x6, 0x1, 0x8)
    OP_28(0x6, 0x1, 0x10)
    OP_28(0x6, 0x1, 0x20)
    OP_28(0x6, 0x1, 0x40)
    OP_28(0x6, 0x1, 0x80)
    OP_28(0x6, 0x1, 0x100)
    OP_28(0x6, 0x1, 0x200)
    OP_28(0x6, 0x1, 0x400)
    OP_28(0x6, 0x1, 0x800)
    OP_28(0x6, 0x1, 0x1000)
    OP_28(0x6, 0x1, 0x2000)
    OP_28(0x6, 0x1, 0x4000)
    OP_28(0x6, 0x1, 0x8000)
    OP_28(0x7, 0x4, 0x4)
    OP_28(0x7, 0x4, 0x2)
    OP_28(0x7, 0x4, 0x8)
    OP_28(0x7, 0x4, 0x10)
    OP_28(0x7, 0x4, 0x20)
    OP_28(0x7, 0x1, 0x1)
    OP_28(0x7, 0x1, 0x2)
    OP_28(0x7, 0x1, 0x4)
    OP_28(0x7, 0x1, 0x8)
    OP_28(0x7, 0x1, 0x10)
    OP_28(0x7, 0x1, 0x20)
    OP_28(0x7, 0x1, 0x40)
    OP_28(0x7, 0x1, 0x80)
    OP_28(0x7, 0x1, 0x100)
    OP_28(0x7, 0x1, 0x200)
    OP_28(0x7, 0x1, 0x400)
    OP_28(0x7, 0x1, 0x800)
    OP_28(0x7, 0x1, 0x1000)
    OP_28(0x7, 0x1, 0x2000)
    OP_28(0x7, 0x1, 0x4000)
    OP_28(0x7, 0x1, 0x8000)
    OP_28(0x8, 0x4, 0x4)
    OP_28(0x8, 0x4, 0x2)
    OP_28(0x8, 0x4, 0x8)
    OP_28(0x8, 0x4, 0x10)
    OP_28(0x8, 0x4, 0x20)
    OP_28(0x8, 0x1, 0x1)
    OP_28(0x8, 0x1, 0x2)
    OP_28(0x8, 0x1, 0x4)
    OP_28(0x8, 0x1, 0x8)
    OP_28(0x8, 0x1, 0x10)
    OP_28(0x8, 0x1, 0x20)
    OP_28(0x8, 0x1, 0x40)
    OP_28(0x8, 0x1, 0x80)
    OP_28(0x8, 0x1, 0x100)
    OP_28(0x8, 0x1, 0x200)
    OP_28(0x8, 0x1, 0x400)
    OP_28(0x8, 0x1, 0x800)
    OP_28(0x8, 0x1, 0x1000)
    OP_28(0x8, 0x1, 0x2000)
    OP_28(0x8, 0x1, 0x4000)
    OP_28(0x8, 0x1, 0x8000)
    OP_28(0x9, 0x4, 0x4)
    OP_28(0x9, 0x4, 0x2)
    OP_28(0x9, 0x4, 0x8)
    OP_28(0x9, 0x4, 0x10)
    OP_28(0x9, 0x4, 0x20)
    OP_28(0x9, 0x1, 0x1)
    OP_28(0x9, 0x1, 0x2)
    OP_28(0x9, 0x1, 0x4)
    OP_28(0x9, 0x1, 0x8)
    OP_28(0x9, 0x1, 0x10)
    OP_28(0x9, 0x1, 0x20)
    OP_28(0x9, 0x1, 0x40)
    OP_28(0x9, 0x1, 0x80)
    OP_28(0x9, 0x1, 0x100)
    OP_28(0x9, 0x1, 0x200)
    OP_28(0x9, 0x1, 0x400)
    OP_28(0x9, 0x1, 0x800)
    OP_28(0x9, 0x1, 0x1000)
    OP_28(0x9, 0x1, 0x2000)
    OP_28(0x9, 0x1, 0x4000)
    OP_28(0x9, 0x1, 0x8000)
    OP_28(0xA, 0x4, 0x4)
    OP_28(0xA, 0x4, 0x2)
    OP_28(0xA, 0x4, 0x8)
    OP_28(0xA, 0x4, 0x10)
    OP_28(0xA, 0x4, 0x20)
    OP_28(0xA, 0x1, 0x1)
    OP_28(0xA, 0x1, 0x2)
    OP_28(0xA, 0x1, 0x4)
    OP_28(0xA, 0x1, 0x8)
    OP_28(0xA, 0x1, 0x10)
    OP_28(0xA, 0x1, 0x20)
    OP_28(0xA, 0x1, 0x40)
    OP_28(0xA, 0x1, 0x80)
    OP_28(0xA, 0x1, 0x100)
    OP_28(0xA, 0x1, 0x200)
    OP_28(0xA, 0x1, 0x400)
    OP_28(0xA, 0x1, 0x800)
    OP_28(0xA, 0x1, 0x1000)
    OP_28(0xA, 0x1, 0x2000)
    OP_28(0xA, 0x1, 0x4000)
    OP_28(0xA, 0x1, 0x8000)
    OP_28(0xB, 0x4, 0x4)
    OP_28(0xB, 0x4, 0x2)
    OP_28(0xB, 0x4, 0x8)
    OP_28(0xB, 0x4, 0x10)
    OP_28(0xB, 0x4, 0x20)
    OP_28(0xB, 0x1, 0x1)
    OP_28(0xB, 0x1, 0x2)
    OP_28(0xB, 0x1, 0x4)
    OP_28(0xB, 0x1, 0x8)
    OP_28(0xB, 0x1, 0x10)
    OP_28(0xB, 0x1, 0x20)
    OP_28(0xB, 0x1, 0x40)
    OP_28(0xB, 0x1, 0x80)
    OP_28(0xB, 0x1, 0x100)
    OP_28(0xB, 0x1, 0x200)
    OP_28(0xB, 0x1, 0x400)
    OP_28(0xB, 0x1, 0x800)
    OP_28(0xB, 0x1, 0x1000)
    OP_28(0xB, 0x1, 0x2000)
    OP_28(0xB, 0x1, 0x4000)
    OP_28(0xB, 0x1, 0x8000)
    OP_28(0xC, 0x4, 0x4)
    OP_28(0xC, 0x4, 0x2)
    OP_28(0xC, 0x4, 0x8)
    OP_28(0xC, 0x4, 0x10)
    OP_28(0xC, 0x4, 0x20)
    OP_28(0xC, 0x1, 0x1)
    OP_28(0xC, 0x1, 0x2)
    OP_28(0xC, 0x1, 0x4)
    OP_28(0xC, 0x1, 0x8)
    OP_28(0xC, 0x1, 0x10)
    OP_28(0xC, 0x1, 0x20)
    OP_28(0xC, 0x1, 0x40)
    OP_28(0xC, 0x1, 0x80)
    OP_28(0xC, 0x1, 0x100)
    OP_28(0xC, 0x1, 0x200)
    OP_28(0xC, 0x1, 0x400)
    OP_28(0xC, 0x1, 0x800)
    OP_28(0xC, 0x1, 0x1000)
    OP_28(0xC, 0x1, 0x2000)
    OP_28(0xC, 0x1, 0x4000)
    OP_28(0xC, 0x1, 0x8000)
    OP_28(0xD, 0x4, 0x4)
    OP_28(0xD, 0x4, 0x2)
    OP_28(0xD, 0x4, 0x8)
    OP_28(0xD, 0x4, 0x10)
    OP_28(0xD, 0x4, 0x20)
    OP_28(0xD, 0x1, 0x1)
    OP_28(0xD, 0x1, 0x2)
    OP_28(0xD, 0x1, 0x4)
    OP_28(0xD, 0x1, 0x8)
    OP_28(0xD, 0x1, 0x10)
    OP_28(0xD, 0x1, 0x20)
    OP_28(0xD, 0x1, 0x40)
    OP_28(0xD, 0x1, 0x80)
    OP_28(0xD, 0x1, 0x100)
    OP_28(0xD, 0x1, 0x200)
    OP_28(0xD, 0x1, 0x400)
    OP_28(0xD, 0x1, 0x800)
    OP_28(0xD, 0x1, 0x1000)
    OP_28(0xD, 0x1, 0x2000)
    OP_28(0xD, 0x1, 0x4000)
    OP_28(0xD, 0x1, 0x8000)
    OP_28(0xE, 0x4, 0x4)
    OP_28(0xE, 0x4, 0x2)
    OP_28(0xE, 0x4, 0x8)
    OP_28(0xE, 0x4, 0x10)
    OP_28(0xE, 0x4, 0x20)
    OP_28(0xE, 0x1, 0x1)
    OP_28(0xE, 0x1, 0x2)
    OP_28(0xE, 0x1, 0x4)
    OP_28(0xE, 0x1, 0x8)
    OP_28(0xE, 0x1, 0x10)
    OP_28(0xE, 0x1, 0x20)
    OP_28(0xE, 0x1, 0x40)
    OP_28(0xE, 0x1, 0x80)
    OP_28(0xE, 0x1, 0x100)
    OP_28(0xE, 0x1, 0x200)
    OP_28(0xE, 0x1, 0x400)
    OP_28(0xE, 0x1, 0x800)
    OP_28(0xE, 0x1, 0x1000)
    OP_28(0xE, 0x1, 0x2000)
    OP_28(0xE, 0x1, 0x4000)
    OP_28(0xE, 0x1, 0x8000)
    OP_28(0xF, 0x4, 0x4)
    OP_28(0xF, 0x4, 0x2)
    OP_28(0xF, 0x4, 0x8)
    OP_28(0xF, 0x4, 0x10)
    OP_28(0xF, 0x4, 0x20)
    OP_28(0xF, 0x1, 0x1)
    OP_28(0xF, 0x1, 0x2)
    OP_28(0xF, 0x1, 0x4)
    OP_28(0xF, 0x1, 0x8)
    OP_28(0xF, 0x1, 0x10)
    OP_28(0xF, 0x1, 0x20)
    OP_28(0xF, 0x1, 0x40)
    OP_28(0xF, 0x1, 0x80)
    OP_28(0xF, 0x1, 0x100)
    OP_28(0xF, 0x1, 0x200)
    OP_28(0xF, 0x1, 0x400)
    OP_28(0xF, 0x1, 0x800)
    OP_28(0xF, 0x1, 0x1000)
    OP_28(0xF, 0x1, 0x2000)
    OP_28(0xF, 0x1, 0x4000)
    OP_28(0xF, 0x1, 0x8000)
    OP_28(0x12, 0x4, 0x4)
    OP_28(0x12, 0x4, 0x2)
    OP_28(0x12, 0x4, 0x8)
    OP_28(0x12, 0x4, 0x10)
    OP_28(0x12, 0x4, 0x20)
    OP_28(0x12, 0x1, 0x1)
    OP_28(0x12, 0x1, 0x2)
    OP_28(0x12, 0x1, 0x4)
    OP_28(0x12, 0x1, 0x8)
    OP_28(0x12, 0x1, 0x10)
    OP_28(0x12, 0x1, 0x20)
    OP_28(0x12, 0x1, 0x40)
    OP_28(0x12, 0x1, 0x80)
    OP_28(0x12, 0x1, 0x100)
    OP_28(0x12, 0x1, 0x200)
    OP_28(0x12, 0x1, 0x400)
    OP_28(0x12, 0x1, 0x800)
    OP_28(0x12, 0x1, 0x1000)
    OP_28(0x12, 0x1, 0x2000)
    OP_28(0x12, 0x1, 0x4000)
    OP_28(0x12, 0x1, 0x8000)
    OP_28(0x13, 0x4, 0x4)
    OP_28(0x13, 0x4, 0x2)
    OP_28(0x13, 0x4, 0x8)
    OP_28(0x13, 0x4, 0x10)
    OP_28(0x13, 0x4, 0x20)
    OP_28(0x13, 0x1, 0x1)
    OP_28(0x13, 0x1, 0x2)
    OP_28(0x13, 0x1, 0x4)
    OP_28(0x13, 0x1, 0x8)
    OP_28(0x13, 0x1, 0x10)
    OP_28(0x13, 0x1, 0x20)
    OP_28(0x13, 0x1, 0x40)
    OP_28(0x13, 0x1, 0x80)
    OP_28(0x13, 0x1, 0x100)
    OP_28(0x13, 0x1, 0x200)
    OP_28(0x13, 0x1, 0x400)
    OP_28(0x13, 0x1, 0x800)
    OP_28(0x13, 0x1, 0x1000)
    OP_28(0x13, 0x1, 0x2000)
    OP_28(0x13, 0x1, 0x4000)
    OP_28(0x13, 0x1, 0x8000)
    OP_28(0x14, 0x4, 0x4)
    OP_28(0x14, 0x4, 0x2)
    OP_28(0x14, 0x4, 0x8)
    OP_28(0x14, 0x4, 0x10)
    OP_28(0x14, 0x4, 0x20)
    OP_28(0x14, 0x1, 0x1)
    OP_28(0x14, 0x1, 0x2)
    OP_28(0x14, 0x1, 0x4)
    OP_28(0x14, 0x1, 0x8)
    OP_28(0x14, 0x1, 0x10)
    OP_28(0x14, 0x1, 0x20)
    OP_28(0x14, 0x1, 0x40)
    OP_28(0x14, 0x1, 0x80)
    OP_28(0x14, 0x1, 0x100)
    OP_28(0x14, 0x1, 0x200)
    OP_28(0x14, 0x1, 0x400)
    OP_28(0x14, 0x1, 0x800)
    OP_28(0x14, 0x1, 0x1000)
    OP_28(0x14, 0x1, 0x2000)
    OP_28(0x14, 0x1, 0x4000)
    OP_28(0x14, 0x1, 0x8000)
    OP_28(0x15, 0x4, 0x4)
    OP_28(0x15, 0x4, 0x2)
    OP_28(0x15, 0x4, 0x8)
    OP_28(0x15, 0x4, 0x10)
    OP_28(0x15, 0x4, 0x20)
    OP_28(0x15, 0x1, 0x1)
    OP_28(0x15, 0x1, 0x2)
    OP_28(0x15, 0x1, 0x4)
    OP_28(0x15, 0x1, 0x8)
    OP_28(0x15, 0x1, 0x10)
    OP_28(0x15, 0x1, 0x20)
    OP_28(0x15, 0x1, 0x40)
    OP_28(0x15, 0x1, 0x80)
    OP_28(0x15, 0x1, 0x100)
    OP_28(0x15, 0x1, 0x200)
    OP_28(0x15, 0x1, 0x400)
    OP_28(0x15, 0x1, 0x800)
    OP_28(0x15, 0x1, 0x1000)
    OP_28(0x15, 0x1, 0x2000)
    OP_28(0x15, 0x1, 0x4000)
    OP_28(0x15, 0x1, 0x8000)
    OP_28(0x16, 0x4, 0x4)
    OP_28(0x16, 0x4, 0x2)
    OP_28(0x16, 0x4, 0x8)
    OP_28(0x16, 0x4, 0x10)
    OP_28(0x16, 0x4, 0x20)
    OP_28(0x16, 0x1, 0x1)
    OP_28(0x16, 0x1, 0x2)
    OP_28(0x16, 0x1, 0x4)
    OP_28(0x16, 0x1, 0x8)
    OP_28(0x16, 0x1, 0x10)
    OP_28(0x16, 0x1, 0x20)
    OP_28(0x16, 0x1, 0x40)
    OP_28(0x16, 0x1, 0x80)
    OP_28(0x16, 0x1, 0x100)
    OP_28(0x16, 0x1, 0x200)
    OP_28(0x16, 0x1, 0x400)
    OP_28(0x16, 0x1, 0x800)
    OP_28(0x16, 0x1, 0x1000)
    OP_28(0x16, 0x1, 0x2000)
    OP_28(0x16, 0x1, 0x4000)
    OP_28(0x16, 0x1, 0x8000)
    OP_28(0x17, 0x4, 0x4)
    OP_28(0x17, 0x4, 0x2)
    OP_28(0x17, 0x4, 0x8)
    OP_28(0x17, 0x4, 0x10)
    OP_28(0x17, 0x4, 0x20)
    OP_28(0x17, 0x1, 0x1)
    OP_28(0x17, 0x1, 0x2)
    OP_28(0x17, 0x1, 0x4)
    OP_28(0x17, 0x1, 0x8)
    OP_28(0x17, 0x1, 0x10)
    OP_28(0x17, 0x1, 0x20)
    OP_28(0x17, 0x1, 0x40)
    OP_28(0x17, 0x1, 0x80)
    OP_28(0x17, 0x1, 0x100)
    OP_28(0x17, 0x1, 0x200)
    OP_28(0x17, 0x1, 0x400)
    OP_28(0x17, 0x1, 0x800)
    OP_28(0x17, 0x1, 0x1000)
    OP_28(0x17, 0x1, 0x2000)
    OP_28(0x17, 0x1, 0x4000)
    OP_28(0x17, 0x1, 0x8000)
    OP_28(0x19, 0x4, 0x4)
    OP_28(0x19, 0x4, 0x2)
    OP_28(0x19, 0x4, 0x8)
    OP_28(0x19, 0x4, 0x10)
    OP_28(0x19, 0x4, 0x20)
    OP_28(0x19, 0x1, 0x1)
    OP_28(0x19, 0x1, 0x2)
    OP_28(0x19, 0x1, 0x4)
    OP_28(0x19, 0x1, 0x8)
    OP_28(0x19, 0x1, 0x10)
    OP_28(0x19, 0x1, 0x20)
    OP_28(0x19, 0x1, 0x40)
    OP_28(0x19, 0x1, 0x80)
    OP_28(0x19, 0x1, 0x100)
    OP_28(0x19, 0x1, 0x200)
    OP_28(0x19, 0x1, 0x400)
    OP_28(0x19, 0x1, 0x800)
    OP_28(0x19, 0x1, 0x1000)
    OP_28(0x19, 0x1, 0x2000)
    OP_28(0x19, 0x1, 0x4000)
    OP_28(0x19, 0x1, 0x8000)
    OP_28(0x1A, 0x4, 0x4)
    OP_28(0x1A, 0x4, 0x2)
    OP_28(0x1A, 0x4, 0x8)
    OP_28(0x1A, 0x4, 0x10)
    OP_28(0x1A, 0x4, 0x20)
    OP_28(0x1A, 0x1, 0x1)
    OP_28(0x1A, 0x1, 0x2)
    OP_28(0x1A, 0x1, 0x4)
    OP_28(0x1A, 0x1, 0x8)
    OP_28(0x1A, 0x1, 0x10)
    OP_28(0x1A, 0x1, 0x20)
    OP_28(0x1A, 0x1, 0x40)
    OP_28(0x1A, 0x1, 0x80)
    OP_28(0x1A, 0x1, 0x100)
    OP_28(0x1A, 0x1, 0x200)
    OP_28(0x1A, 0x1, 0x400)
    OP_28(0x1A, 0x1, 0x800)
    OP_28(0x1A, 0x1, 0x1000)
    OP_28(0x1A, 0x1, 0x2000)
    OP_28(0x1A, 0x1, 0x4000)
    OP_28(0x1A, 0x1, 0x8000)
    OP_28(0x1B, 0x4, 0x4)
    OP_28(0x1B, 0x4, 0x2)
    OP_28(0x1B, 0x4, 0x8)
    OP_28(0x1B, 0x4, 0x10)
    OP_28(0x1B, 0x4, 0x20)
    OP_28(0x1B, 0x1, 0x1)
    OP_28(0x1B, 0x1, 0x2)
    OP_28(0x1B, 0x1, 0x4)
    OP_28(0x1B, 0x1, 0x8)
    OP_28(0x1B, 0x1, 0x10)
    OP_28(0x1B, 0x1, 0x20)
    OP_28(0x1B, 0x1, 0x40)
    OP_28(0x1B, 0x1, 0x80)
    OP_28(0x1B, 0x1, 0x100)
    OP_28(0x1B, 0x1, 0x200)
    OP_28(0x1B, 0x1, 0x400)
    OP_28(0x1B, 0x1, 0x800)
    OP_28(0x1B, 0x1, 0x1000)
    OP_28(0x1B, 0x1, 0x2000)
    OP_28(0x1B, 0x1, 0x4000)
    OP_28(0x1B, 0x1, 0x8000)
    OP_28(0x1C, 0x4, 0x4)
    OP_28(0x1C, 0x4, 0x2)
    OP_28(0x1C, 0x4, 0x8)
    OP_28(0x1C, 0x4, 0x10)
    OP_28(0x1C, 0x4, 0x20)
    OP_28(0x1C, 0x1, 0x1)
    OP_28(0x1C, 0x1, 0x2)
    OP_28(0x1C, 0x1, 0x4)
    OP_28(0x1C, 0x1, 0x8)
    OP_28(0x1C, 0x1, 0x10)
    OP_28(0x1C, 0x1, 0x20)
    OP_28(0x1C, 0x1, 0x40)
    OP_28(0x1C, 0x1, 0x80)
    OP_28(0x1C, 0x1, 0x100)
    OP_28(0x1C, 0x1, 0x200)
    OP_28(0x1C, 0x1, 0x400)
    OP_28(0x1C, 0x1, 0x800)
    OP_28(0x1C, 0x1, 0x1000)
    OP_28(0x1C, 0x1, 0x2000)
    OP_28(0x1C, 0x1, 0x4000)
    OP_28(0x1C, 0x1, 0x8000)
    OP_28(0x1D, 0x4, 0x4)
    OP_28(0x1D, 0x4, 0x2)
    OP_28(0x1D, 0x4, 0x8)
    OP_28(0x1D, 0x4, 0x10)
    OP_28(0x1D, 0x4, 0x20)
    OP_28(0x1D, 0x1, 0x1)
    OP_28(0x1D, 0x1, 0x2)
    OP_28(0x1D, 0x1, 0x4)
    OP_28(0x1D, 0x1, 0x8)
    OP_28(0x1D, 0x1, 0x10)
    OP_28(0x1D, 0x1, 0x20)
    OP_28(0x1D, 0x1, 0x40)
    OP_28(0x1D, 0x1, 0x80)
    OP_28(0x1D, 0x1, 0x100)
    OP_28(0x1D, 0x1, 0x200)
    OP_28(0x1D, 0x1, 0x400)
    OP_28(0x1D, 0x1, 0x800)
    OP_28(0x1D, 0x1, 0x1000)
    OP_28(0x1D, 0x1, 0x2000)
    OP_28(0x1D, 0x1, 0x4000)
    OP_28(0x1D, 0x1, 0x8000)
    OP_28(0x1E, 0x4, 0x4)
    OP_28(0x1E, 0x4, 0x2)
    OP_28(0x1E, 0x4, 0x8)
    OP_28(0x1E, 0x4, 0x10)
    OP_28(0x1E, 0x4, 0x20)
    OP_28(0x1E, 0x1, 0x1)
    OP_28(0x1E, 0x1, 0x2)
    OP_28(0x1E, 0x1, 0x4)
    OP_28(0x1E, 0x1, 0x8)
    OP_28(0x1E, 0x1, 0x10)
    OP_28(0x1E, 0x1, 0x20)
    OP_28(0x1E, 0x1, 0x40)
    OP_28(0x1E, 0x1, 0x80)
    OP_28(0x1E, 0x1, 0x100)
    OP_28(0x1E, 0x1, 0x200)
    OP_28(0x1E, 0x1, 0x400)
    OP_28(0x1E, 0x1, 0x800)
    OP_28(0x1E, 0x1, 0x1000)
    OP_28(0x1E, 0x1, 0x2000)
    OP_28(0x1E, 0x1, 0x4000)
    OP_28(0x1E, 0x1, 0x8000)
    OP_28(0x1F, 0x4, 0x4)
    OP_28(0x1F, 0x4, 0x2)
    OP_28(0x1F, 0x4, 0x8)
    OP_28(0x1F, 0x4, 0x10)
    OP_28(0x1F, 0x4, 0x20)
    OP_28(0x1F, 0x1, 0x1)
    OP_28(0x1F, 0x1, 0x2)
    OP_28(0x1F, 0x1, 0x4)
    OP_28(0x1F, 0x1, 0x8)
    OP_28(0x1F, 0x1, 0x10)
    OP_28(0x1F, 0x1, 0x20)
    OP_28(0x1F, 0x1, 0x40)
    OP_28(0x1F, 0x1, 0x80)
    OP_28(0x1F, 0x1, 0x100)
    OP_28(0x1F, 0x1, 0x200)
    OP_28(0x1F, 0x1, 0x400)
    OP_28(0x1F, 0x1, 0x800)
    OP_28(0x1F, 0x1, 0x1000)
    OP_28(0x1F, 0x1, 0x2000)
    OP_28(0x1F, 0x1, 0x4000)
    OP_28(0x1F, 0x1, 0x8000)
    OP_28(0x20, 0x4, 0x4)
    OP_28(0x20, 0x4, 0x2)
    OP_28(0x20, 0x4, 0x8)
    OP_28(0x20, 0x4, 0x10)
    OP_28(0x20, 0x4, 0x20)
    OP_28(0x20, 0x1, 0x1)
    OP_28(0x20, 0x1, 0x2)
    OP_28(0x20, 0x1, 0x4)
    OP_28(0x20, 0x1, 0x8)
    OP_28(0x20, 0x1, 0x10)
    OP_28(0x20, 0x1, 0x20)
    OP_28(0x20, 0x1, 0x40)
    OP_28(0x20, 0x1, 0x80)
    OP_28(0x20, 0x1, 0x100)
    OP_28(0x20, 0x1, 0x200)
    OP_28(0x20, 0x1, 0x400)
    OP_28(0x20, 0x1, 0x800)
    OP_28(0x20, 0x1, 0x1000)
    OP_28(0x20, 0x1, 0x2000)
    OP_28(0x20, 0x1, 0x4000)
    OP_28(0x20, 0x1, 0x8000)
    OP_28(0x21, 0x4, 0x4)
    OP_28(0x21, 0x4, 0x2)
    OP_28(0x21, 0x4, 0x8)
    OP_28(0x21, 0x4, 0x10)
    OP_28(0x21, 0x4, 0x20)
    OP_28(0x21, 0x1, 0x1)
    OP_28(0x21, 0x1, 0x2)
    OP_28(0x21, 0x1, 0x4)
    OP_28(0x21, 0x1, 0x8)
    OP_28(0x21, 0x1, 0x10)
    OP_28(0x21, 0x1, 0x20)
    OP_28(0x21, 0x1, 0x40)
    OP_28(0x21, 0x1, 0x80)
    OP_28(0x21, 0x1, 0x100)
    OP_28(0x21, 0x1, 0x200)
    OP_28(0x21, 0x1, 0x400)
    OP_28(0x21, 0x1, 0x800)
    OP_28(0x21, 0x1, 0x1000)
    OP_28(0x21, 0x1, 0x2000)
    OP_28(0x21, 0x1, 0x4000)
    OP_28(0x21, 0x1, 0x8000)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x4, 0x2)
    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x10)
    OP_28(0x22, 0x4, 0x20)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)
    OP_28(0x22, 0x1, 0x4)
    OP_28(0x22, 0x1, 0x8)
    OP_28(0x22, 0x1, 0x10)
    OP_28(0x22, 0x1, 0x20)
    OP_28(0x22, 0x1, 0x40)
    OP_28(0x22, 0x1, 0x80)
    OP_28(0x22, 0x1, 0x100)
    OP_28(0x22, 0x1, 0x200)
    OP_28(0x22, 0x1, 0x400)
    OP_28(0x22, 0x1, 0x800)
    OP_28(0x22, 0x1, 0x1000)
    OP_28(0x22, 0x1, 0x2000)
    OP_28(0x22, 0x1, 0x4000)
    OP_28(0x22, 0x1, 0x8000)
    OP_28(0x23, 0x4, 0x4)
    OP_28(0x23, 0x4, 0x2)
    OP_28(0x23, 0x4, 0x8)
    OP_28(0x23, 0x4, 0x10)
    OP_28(0x23, 0x4, 0x20)
    OP_28(0x23, 0x1, 0x1)
    OP_28(0x23, 0x1, 0x2)
    OP_28(0x23, 0x1, 0x4)
    OP_28(0x23, 0x1, 0x8)
    OP_28(0x23, 0x1, 0x10)
    OP_28(0x23, 0x1, 0x20)
    OP_28(0x23, 0x1, 0x40)
    OP_28(0x23, 0x1, 0x80)
    OP_28(0x23, 0x1, 0x100)
    OP_28(0x23, 0x1, 0x200)
    OP_28(0x23, 0x1, 0x400)
    OP_28(0x23, 0x1, 0x800)
    OP_28(0x23, 0x1, 0x1000)
    OP_28(0x23, 0x1, 0x2000)
    OP_28(0x23, 0x1, 0x4000)
    OP_28(0x23, 0x1, 0x8000)
    OP_28(0x24, 0x4, 0x4)
    OP_28(0x24, 0x4, 0x2)
    OP_28(0x24, 0x4, 0x8)
    OP_28(0x24, 0x4, 0x10)
    OP_28(0x24, 0x4, 0x20)
    OP_28(0x24, 0x1, 0x1)
    OP_28(0x24, 0x1, 0x2)
    OP_28(0x24, 0x1, 0x4)
    OP_28(0x24, 0x1, 0x8)
    OP_28(0x24, 0x1, 0x10)
    OP_28(0x24, 0x1, 0x20)
    OP_28(0x24, 0x1, 0x40)
    OP_28(0x24, 0x1, 0x80)
    OP_28(0x24, 0x1, 0x100)
    OP_28(0x24, 0x1, 0x200)
    OP_28(0x24, 0x1, 0x400)
    OP_28(0x24, 0x1, 0x800)
    OP_28(0x24, 0x1, 0x1000)
    OP_28(0x24, 0x1, 0x2000)
    OP_28(0x24, 0x1, 0x4000)
    OP_28(0x24, 0x1, 0x8000)
    OP_28(0x28, 0x4, 0x4)
    OP_28(0x28, 0x4, 0x2)
    OP_28(0x28, 0x4, 0x8)
    OP_28(0x28, 0x4, 0x10)
    OP_28(0x28, 0x4, 0x20)
    OP_28(0x28, 0x1, 0x1)
    OP_28(0x28, 0x1, 0x2)
    OP_28(0x28, 0x1, 0x4)
    OP_28(0x28, 0x1, 0x8)
    OP_28(0x28, 0x1, 0x10)
    OP_28(0x28, 0x1, 0x20)
    OP_28(0x28, 0x1, 0x40)
    OP_28(0x28, 0x1, 0x80)
    OP_28(0x28, 0x1, 0x100)
    OP_28(0x28, 0x1, 0x200)
    OP_28(0x28, 0x1, 0x400)
    OP_28(0x28, 0x1, 0x800)
    OP_28(0x28, 0x1, 0x1000)
    OP_28(0x28, 0x1, 0x2000)
    OP_28(0x28, 0x1, 0x4000)
    OP_28(0x28, 0x1, 0x8000)
    OP_28(0x29, 0x4, 0x4)
    OP_28(0x29, 0x4, 0x2)
    OP_28(0x29, 0x4, 0x8)
    OP_28(0x29, 0x4, 0x10)
    OP_28(0x29, 0x4, 0x20)
    OP_28(0x29, 0x1, 0x1)
    OP_28(0x29, 0x1, 0x2)
    OP_28(0x29, 0x1, 0x4)
    OP_28(0x29, 0x1, 0x8)
    OP_28(0x29, 0x1, 0x10)
    OP_28(0x29, 0x1, 0x20)
    OP_28(0x29, 0x1, 0x40)
    OP_28(0x29, 0x1, 0x80)
    OP_28(0x29, 0x1, 0x100)
    OP_28(0x29, 0x1, 0x200)
    OP_28(0x29, 0x1, 0x400)
    OP_28(0x29, 0x1, 0x800)
    OP_28(0x29, 0x1, 0x1000)
    OP_28(0x29, 0x1, 0x2000)
    OP_28(0x29, 0x1, 0x4000)
    OP_28(0x29, 0x1, 0x8000)
    OP_28(0x2A, 0x4, 0x4)
    OP_28(0x2A, 0x4, 0x2)
    OP_28(0x2A, 0x4, 0x8)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x4, 0x20)
    OP_28(0x2A, 0x1, 0x1)
    OP_28(0x2A, 0x1, 0x2)
    OP_28(0x2A, 0x1, 0x4)
    OP_28(0x2A, 0x1, 0x8)
    OP_28(0x2A, 0x1, 0x10)
    OP_28(0x2A, 0x1, 0x20)
    OP_28(0x2A, 0x1, 0x40)
    OP_28(0x2A, 0x1, 0x80)
    OP_28(0x2A, 0x1, 0x100)
    OP_28(0x2A, 0x1, 0x200)
    OP_28(0x2A, 0x1, 0x400)
    OP_28(0x2A, 0x1, 0x800)
    OP_28(0x2A, 0x1, 0x1000)
    OP_28(0x2A, 0x1, 0x2000)
    OP_28(0x2A, 0x1, 0x4000)
    OP_28(0x2A, 0x1, 0x8000)
    OP_28(0x2B, 0x4, 0x4)
    OP_28(0x2B, 0x4, 0x2)
    OP_28(0x2B, 0x4, 0x8)
    OP_28(0x2B, 0x4, 0x10)
    OP_28(0x2B, 0x4, 0x20)
    OP_28(0x2B, 0x1, 0x1)
    OP_28(0x2B, 0x1, 0x2)
    OP_28(0x2B, 0x1, 0x4)
    OP_28(0x2B, 0x1, 0x8)
    OP_28(0x2B, 0x1, 0x10)
    OP_28(0x2B, 0x1, 0x20)
    OP_28(0x2B, 0x1, 0x40)
    OP_28(0x2B, 0x1, 0x80)
    OP_28(0x2B, 0x1, 0x100)
    OP_28(0x2B, 0x1, 0x200)
    OP_28(0x2B, 0x1, 0x400)
    OP_28(0x2B, 0x1, 0x800)
    OP_28(0x2B, 0x1, 0x1000)
    OP_28(0x2B, 0x1, 0x2000)
    OP_28(0x2B, 0x1, 0x4000)
    OP_28(0x2B, 0x1, 0x8000)
    OP_28(0x2C, 0x4, 0x4)
    OP_28(0x2C, 0x4, 0x2)
    OP_28(0x2C, 0x4, 0x8)
    OP_28(0x2C, 0x4, 0x10)
    OP_28(0x2C, 0x4, 0x20)
    OP_28(0x2C, 0x1, 0x1)
    OP_28(0x2C, 0x1, 0x2)
    OP_28(0x2C, 0x1, 0x4)
    OP_28(0x2C, 0x1, 0x8)
    OP_28(0x2C, 0x1, 0x10)
    OP_28(0x2C, 0x1, 0x20)
    OP_28(0x2C, 0x1, 0x40)
    OP_28(0x2C, 0x1, 0x80)
    OP_28(0x2C, 0x1, 0x100)
    OP_28(0x2C, 0x1, 0x200)
    OP_28(0x2C, 0x1, 0x400)
    OP_28(0x2C, 0x1, 0x800)
    OP_28(0x2C, 0x1, 0x1000)
    OP_28(0x2C, 0x1, 0x2000)
    OP_28(0x2C, 0x1, 0x4000)
    OP_28(0x2C, 0x1, 0x8000)
    OP_28(0x2D, 0x4, 0x4)
    OP_28(0x2D, 0x4, 0x2)
    OP_28(0x2D, 0x4, 0x8)
    OP_28(0x2D, 0x4, 0x10)
    OP_28(0x2D, 0x4, 0x20)
    OP_28(0x2D, 0x1, 0x1)
    OP_28(0x2D, 0x1, 0x2)
    OP_28(0x2D, 0x1, 0x4)
    OP_28(0x2D, 0x1, 0x8)
    OP_28(0x2D, 0x1, 0x10)
    OP_28(0x2D, 0x1, 0x20)
    OP_28(0x2D, 0x1, 0x40)
    OP_28(0x2D, 0x1, 0x80)
    OP_28(0x2D, 0x1, 0x100)
    OP_28(0x2D, 0x1, 0x200)
    OP_28(0x2D, 0x1, 0x400)
    OP_28(0x2D, 0x1, 0x800)
    OP_28(0x2D, 0x1, 0x1000)
    OP_28(0x2D, 0x1, 0x2000)
    OP_28(0x2D, 0x1, 0x4000)
    OP_28(0x2D, 0x1, 0x8000)
    OP_28(0x2E, 0x4, 0x4)
    OP_28(0x2E, 0x4, 0x2)
    OP_28(0x2E, 0x4, 0x8)
    OP_28(0x2E, 0x4, 0x10)
    OP_28(0x2E, 0x4, 0x20)
    OP_28(0x2E, 0x1, 0x1)
    OP_28(0x2E, 0x1, 0x2)
    OP_28(0x2E, 0x1, 0x4)
    OP_28(0x2E, 0x1, 0x8)
    OP_28(0x2E, 0x1, 0x10)
    OP_28(0x2E, 0x1, 0x20)
    OP_28(0x2E, 0x1, 0x40)
    OP_28(0x2E, 0x1, 0x80)
    OP_28(0x2E, 0x1, 0x100)
    OP_28(0x2E, 0x1, 0x200)
    OP_28(0x2E, 0x1, 0x400)
    OP_28(0x2E, 0x1, 0x800)
    OP_28(0x2E, 0x1, 0x1000)
    OP_28(0x2E, 0x1, 0x2000)
    OP_28(0x2E, 0x1, 0x4000)
    OP_28(0x2E, 0x1, 0x8000)
    OP_28(0x2F, 0x4, 0x4)
    OP_28(0x2F, 0x4, 0x2)
    OP_28(0x2F, 0x4, 0x8)
    OP_28(0x2F, 0x4, 0x10)
    OP_28(0x2F, 0x4, 0x20)
    OP_28(0x2F, 0x1, 0x1)
    OP_28(0x2F, 0x1, 0x2)
    OP_28(0x2F, 0x1, 0x4)
    OP_28(0x2F, 0x1, 0x8)
    OP_28(0x2F, 0x1, 0x10)
    OP_28(0x2F, 0x1, 0x20)
    OP_28(0x2F, 0x1, 0x40)
    OP_28(0x2F, 0x1, 0x80)
    OP_28(0x2F, 0x1, 0x100)
    OP_28(0x2F, 0x1, 0x200)
    OP_28(0x2F, 0x1, 0x400)
    OP_28(0x2F, 0x1, 0x800)
    OP_28(0x2F, 0x1, 0x1000)
    OP_28(0x2F, 0x1, 0x2000)
    OP_28(0x2F, 0x1, 0x4000)
    OP_28(0x2F, 0x1, 0x8000)
    OP_28(0x30, 0x4, 0x4)
    OP_28(0x30, 0x4, 0x2)
    OP_28(0x30, 0x4, 0x8)
    OP_28(0x30, 0x4, 0x10)
    OP_28(0x30, 0x4, 0x20)
    OP_28(0x30, 0x1, 0x1)
    OP_28(0x30, 0x1, 0x2)
    OP_28(0x30, 0x1, 0x4)
    OP_28(0x30, 0x1, 0x8)
    OP_28(0x30, 0x1, 0x10)
    OP_28(0x30, 0x1, 0x20)
    OP_28(0x30, 0x1, 0x40)
    OP_28(0x30, 0x1, 0x80)
    OP_28(0x30, 0x1, 0x100)
    OP_28(0x30, 0x1, 0x200)
    OP_28(0x30, 0x1, 0x400)
    OP_28(0x30, 0x1, 0x800)
    OP_28(0x30, 0x1, 0x1000)
    OP_28(0x30, 0x1, 0x2000)
    OP_28(0x30, 0x1, 0x4000)
    OP_28(0x30, 0x1, 0x8000)
    OP_28(0x31, 0x4, 0x4)
    OP_28(0x31, 0x4, 0x2)
    OP_28(0x31, 0x4, 0x8)
    OP_28(0x31, 0x4, 0x10)
    OP_28(0x31, 0x4, 0x20)
    OP_28(0x31, 0x1, 0x1)
    OP_28(0x31, 0x1, 0x2)
    OP_28(0x31, 0x1, 0x4)
    OP_28(0x31, 0x1, 0x8)
    OP_28(0x31, 0x1, 0x10)
    OP_28(0x31, 0x1, 0x20)
    OP_28(0x31, 0x1, 0x40)
    OP_28(0x31, 0x1, 0x80)
    OP_28(0x31, 0x1, 0x100)
    OP_28(0x31, 0x1, 0x200)
    OP_28(0x31, 0x1, 0x400)
    OP_28(0x31, 0x1, 0x800)
    OP_28(0x31, 0x1, 0x1000)
    OP_28(0x31, 0x1, 0x2000)
    OP_28(0x31, 0x1, 0x4000)
    OP_28(0x31, 0x1, 0x8000)
    OP_28(0x32, 0x4, 0x4)
    OP_28(0x32, 0x4, 0x2)
    OP_28(0x32, 0x4, 0x8)
    OP_28(0x32, 0x4, 0x10)
    OP_28(0x32, 0x4, 0x20)
    OP_28(0x32, 0x1, 0x1)
    OP_28(0x32, 0x1, 0x2)
    OP_28(0x32, 0x1, 0x4)
    OP_28(0x32, 0x1, 0x8)
    OP_28(0x32, 0x1, 0x10)
    OP_28(0x32, 0x1, 0x20)
    OP_28(0x32, 0x1, 0x40)
    OP_28(0x32, 0x1, 0x80)
    OP_28(0x32, 0x1, 0x100)
    OP_28(0x32, 0x1, 0x200)
    OP_28(0x32, 0x1, 0x400)
    OP_28(0x32, 0x1, 0x800)
    OP_28(0x32, 0x1, 0x1000)
    OP_28(0x32, 0x1, 0x2000)
    OP_28(0x32, 0x1, 0x4000)
    OP_28(0x32, 0x1, 0x8000)
    OP_28(0x33, 0x4, 0x4)
    OP_28(0x33, 0x4, 0x2)
    OP_28(0x33, 0x4, 0x8)
    OP_28(0x33, 0x4, 0x10)
    OP_28(0x33, 0x4, 0x20)
    OP_28(0x33, 0x1, 0x1)
    OP_28(0x33, 0x1, 0x2)
    OP_28(0x33, 0x1, 0x4)
    OP_28(0x33, 0x1, 0x8)
    OP_28(0x33, 0x1, 0x10)
    OP_28(0x33, 0x1, 0x20)
    OP_28(0x33, 0x1, 0x40)
    OP_28(0x33, 0x1, 0x80)
    OP_28(0x33, 0x1, 0x100)
    OP_28(0x33, 0x1, 0x200)
    OP_28(0x33, 0x1, 0x400)
    OP_28(0x33, 0x1, 0x800)
    OP_28(0x33, 0x1, 0x1000)
    OP_28(0x33, 0x1, 0x2000)
    OP_28(0x33, 0x1, 0x4000)
    OP_28(0x33, 0x1, 0x8000)
    OP_28(0x34, 0x4, 0x4)
    OP_28(0x34, 0x4, 0x2)
    OP_28(0x34, 0x4, 0x8)
    OP_28(0x34, 0x4, 0x10)
    OP_28(0x34, 0x4, 0x20)
    OP_28(0x34, 0x1, 0x1)
    OP_28(0x34, 0x1, 0x2)
    OP_28(0x34, 0x1, 0x4)
    OP_28(0x34, 0x1, 0x8)
    OP_28(0x34, 0x1, 0x10)
    OP_28(0x34, 0x1, 0x20)
    OP_28(0x34, 0x1, 0x40)
    OP_28(0x34, 0x1, 0x80)
    OP_28(0x34, 0x1, 0x100)
    OP_28(0x34, 0x1, 0x200)
    OP_28(0x34, 0x1, 0x400)
    OP_28(0x34, 0x1, 0x800)
    OP_28(0x34, 0x1, 0x1000)
    OP_28(0x34, 0x1, 0x2000)
    OP_28(0x34, 0x1, 0x4000)
    OP_28(0x34, 0x1, 0x8000)
    OP_28(0x35, 0x4, 0x4)
    OP_28(0x35, 0x4, 0x2)
    OP_28(0x35, 0x4, 0x8)
    OP_28(0x35, 0x4, 0x10)
    OP_28(0x35, 0x4, 0x20)
    OP_28(0x35, 0x1, 0x1)
    OP_28(0x35, 0x1, 0x2)
    OP_28(0x35, 0x1, 0x4)
    OP_28(0x35, 0x1, 0x8)
    OP_28(0x35, 0x1, 0x10)
    OP_28(0x35, 0x1, 0x20)
    OP_28(0x35, 0x1, 0x40)
    OP_28(0x35, 0x1, 0x80)
    OP_28(0x35, 0x1, 0x100)
    OP_28(0x35, 0x1, 0x200)
    OP_28(0x35, 0x1, 0x400)
    OP_28(0x35, 0x1, 0x800)
    OP_28(0x35, 0x1, 0x1000)
    OP_28(0x35, 0x1, 0x2000)
    OP_28(0x35, 0x1, 0x4000)
    OP_28(0x35, 0x1, 0x8000)
    OP_28(0x36, 0x4, 0x4)
    OP_28(0x36, 0x4, 0x2)
    OP_28(0x36, 0x4, 0x8)
    OP_28(0x36, 0x4, 0x10)
    OP_28(0x36, 0x4, 0x20)
    OP_28(0x36, 0x1, 0x1)
    OP_28(0x36, 0x1, 0x2)
    OP_28(0x36, 0x1, 0x4)
    OP_28(0x36, 0x1, 0x8)
    OP_28(0x36, 0x1, 0x10)
    OP_28(0x36, 0x1, 0x20)
    OP_28(0x36, 0x1, 0x40)
    OP_28(0x36, 0x1, 0x80)
    OP_28(0x36, 0x1, 0x100)
    OP_28(0x36, 0x1, 0x200)
    OP_28(0x36, 0x1, 0x400)
    OP_28(0x36, 0x1, 0x800)
    OP_28(0x36, 0x1, 0x1000)
    OP_28(0x36, 0x1, 0x2000)
    OP_28(0x36, 0x1, 0x4000)
    OP_28(0x36, 0x1, 0x8000)
    OP_28(0x37, 0x4, 0x4)
    OP_28(0x37, 0x4, 0x2)
    OP_28(0x37, 0x4, 0x8)
    OP_28(0x37, 0x4, 0x10)
    OP_28(0x37, 0x4, 0x20)
    OP_28(0x37, 0x1, 0x1)
    OP_28(0x37, 0x1, 0x2)
    OP_28(0x37, 0x1, 0x4)
    OP_28(0x37, 0x1, 0x8)
    OP_28(0x37, 0x1, 0x10)
    OP_28(0x37, 0x1, 0x20)
    OP_28(0x37, 0x1, 0x40)
    OP_28(0x37, 0x1, 0x80)
    OP_28(0x37, 0x1, 0x100)
    OP_28(0x37, 0x1, 0x200)
    OP_28(0x37, 0x1, 0x400)
    OP_28(0x37, 0x1, 0x800)
    OP_28(0x37, 0x1, 0x1000)
    OP_28(0x37, 0x1, 0x2000)
    OP_28(0x37, 0x1, 0x4000)
    OP_28(0x37, 0x1, 0x8000)
    OP_28(0x38, 0x4, 0x4)
    OP_28(0x38, 0x4, 0x2)
    OP_28(0x38, 0x4, 0x8)
    OP_28(0x38, 0x4, 0x10)
    OP_28(0x38, 0x4, 0x20)
    OP_28(0x38, 0x1, 0x1)
    OP_28(0x38, 0x1, 0x2)
    OP_28(0x38, 0x1, 0x4)
    OP_28(0x38, 0x1, 0x8)
    OP_28(0x38, 0x1, 0x10)
    OP_28(0x38, 0x1, 0x20)
    OP_28(0x38, 0x1, 0x40)
    OP_28(0x38, 0x1, 0x80)
    OP_28(0x38, 0x1, 0x100)
    OP_28(0x38, 0x1, 0x200)
    OP_28(0x38, 0x1, 0x400)
    OP_28(0x38, 0x1, 0x800)
    OP_28(0x38, 0x1, 0x1000)
    OP_28(0x38, 0x1, 0x2000)
    OP_28(0x38, 0x1, 0x4000)
    OP_28(0x38, 0x1, 0x8000)
    OP_28(0x39, 0x4, 0x4)
    OP_28(0x39, 0x4, 0x2)
    OP_28(0x39, 0x4, 0x8)
    OP_28(0x39, 0x4, 0x10)
    OP_28(0x39, 0x4, 0x20)
    OP_28(0x39, 0x1, 0x1)
    OP_28(0x39, 0x1, 0x2)
    OP_28(0x39, 0x1, 0x4)
    OP_28(0x39, 0x1, 0x8)
    OP_28(0x39, 0x1, 0x10)
    OP_28(0x39, 0x1, 0x20)
    OP_28(0x39, 0x1, 0x40)
    OP_28(0x39, 0x1, 0x80)
    OP_28(0x39, 0x1, 0x100)
    OP_28(0x39, 0x1, 0x200)
    OP_28(0x39, 0x1, 0x400)
    OP_28(0x39, 0x1, 0x800)
    OP_28(0x39, 0x1, 0x1000)
    OP_28(0x39, 0x1, 0x2000)
    OP_28(0x39, 0x1, 0x4000)
    OP_28(0x39, 0x1, 0x8000)
    OP_28(0x3A, 0x4, 0x4)
    OP_28(0x3A, 0x4, 0x2)
    OP_28(0x3A, 0x4, 0x8)
    OP_28(0x3A, 0x4, 0x10)
    OP_28(0x3A, 0x4, 0x20)
    OP_28(0x3A, 0x1, 0x1)
    OP_28(0x3A, 0x1, 0x2)
    OP_28(0x3A, 0x1, 0x4)
    OP_28(0x3A, 0x1, 0x8)
    OP_28(0x3A, 0x1, 0x10)
    OP_28(0x3A, 0x1, 0x20)
    OP_28(0x3A, 0x1, 0x40)
    OP_28(0x3A, 0x1, 0x80)
    OP_28(0x3A, 0x1, 0x100)
    OP_28(0x3A, 0x1, 0x200)
    OP_28(0x3A, 0x1, 0x400)
    OP_28(0x3A, 0x1, 0x800)
    OP_28(0x3A, 0x1, 0x1000)
    OP_28(0x3A, 0x1, 0x2000)
    OP_28(0x3A, 0x1, 0x4000)
    OP_28(0x3A, 0x1, 0x8000)
    OP_28(0x3B, 0x4, 0x4)
    OP_28(0x3B, 0x4, 0x2)
    OP_28(0x3B, 0x4, 0x8)
    OP_28(0x3B, 0x4, 0x10)
    OP_28(0x3B, 0x4, 0x20)
    OP_28(0x3B, 0x1, 0x1)
    OP_28(0x3B, 0x1, 0x2)
    OP_28(0x3B, 0x1, 0x4)
    OP_28(0x3B, 0x1, 0x8)
    OP_28(0x3B, 0x1, 0x10)
    OP_28(0x3B, 0x1, 0x20)
    OP_28(0x3B, 0x1, 0x40)
    OP_28(0x3B, 0x1, 0x80)
    OP_28(0x3B, 0x1, 0x100)
    OP_28(0x3B, 0x1, 0x200)
    OP_28(0x3B, 0x1, 0x400)
    OP_28(0x3B, 0x1, 0x800)
    OP_28(0x3B, 0x1, 0x1000)
    OP_28(0x3B, 0x1, 0x2000)
    OP_28(0x3B, 0x1, 0x4000)
    OP_28(0x3B, 0x1, 0x8000)
    OP_28(0x3C, 0x4, 0x2)
    OP_28(0x3C, 0x4, 0x8)
    OP_28(0x3C, 0x4, 0x10)
    OP_28(0x3C, 0x4, 0x20)
    OP_28(0x3C, 0x1, 0x1)
    OP_28(0x3C, 0x1, 0x2)
    OP_28(0x3C, 0x1, 0x4)
    OP_28(0x3C, 0x1, 0x8)
    OP_28(0x3C, 0x1, 0x10)
    OP_28(0x3C, 0x1, 0x20)
    OP_28(0x3C, 0x1, 0x40)
    OP_28(0x3C, 0x1, 0x80)
    OP_28(0x3C, 0x1, 0x100)
    OP_28(0x3C, 0x1, 0x200)
    OP_28(0x3C, 0x1, 0x400)
    OP_28(0x3C, 0x1, 0x800)
    OP_28(0x3C, 0x1, 0x1000)
    OP_28(0x3C, 0x1, 0x2000)
    OP_28(0x3C, 0x1, 0x4000)
    OP_28(0x3C, 0x1, 0x8000)
    OP_28(0x3D, 0x4, 0x4)
    OP_28(0x3D, 0x4, 0x2)
    OP_28(0x3D, 0x4, 0x8)
    OP_28(0x3D, 0x4, 0x10)
    OP_28(0x3D, 0x4, 0x20)
    OP_28(0x3D, 0x1, 0x1)
    OP_28(0x3D, 0x1, 0x2)
    OP_28(0x3D, 0x1, 0x4)
    OP_28(0x3D, 0x1, 0x8)
    OP_28(0x3D, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x20)
    OP_28(0x3D, 0x1, 0x40)
    OP_28(0x3D, 0x1, 0x80)
    OP_28(0x3D, 0x1, 0x100)
    OP_28(0x3D, 0x1, 0x200)
    OP_28(0x3D, 0x1, 0x400)
    OP_28(0x3D, 0x1, 0x800)
    OP_28(0x3D, 0x1, 0x1000)
    OP_28(0x3D, 0x1, 0x2000)
    OP_28(0x3D, 0x1, 0x4000)
    OP_28(0x3D, 0x1, 0x8000)
    OP_28(0x3E, 0x4, 0x4)
    OP_28(0x3E, 0x4, 0x2)
    OP_28(0x3E, 0x4, 0x8)
    OP_28(0x3E, 0x4, 0x10)
    OP_28(0x3E, 0x4, 0x20)
    OP_28(0x3E, 0x1, 0x1)
    OP_28(0x3E, 0x1, 0x2)
    OP_28(0x3E, 0x1, 0x4)
    OP_28(0x3E, 0x1, 0x8)
    OP_28(0x3E, 0x1, 0x10)
    OP_28(0x3E, 0x1, 0x20)
    OP_28(0x3E, 0x1, 0x40)
    OP_28(0x3E, 0x1, 0x80)
    OP_28(0x3E, 0x1, 0x100)
    OP_28(0x3E, 0x1, 0x200)
    OP_28(0x3E, 0x1, 0x400)
    OP_28(0x3E, 0x1, 0x800)
    OP_28(0x3E, 0x1, 0x1000)
    OP_28(0x3E, 0x1, 0x2000)
    OP_28(0x3E, 0x1, 0x4000)
    OP_28(0x3E, 0x1, 0x8000)
    OP_28(0x3F, 0x4, 0x4)
    OP_28(0x3F, 0x4, 0x2)
    OP_28(0x3F, 0x4, 0x8)
    OP_28(0x3F, 0x4, 0x10)
    OP_28(0x3F, 0x4, 0x20)
    OP_28(0x3F, 0x1, 0x1)
    OP_28(0x3F, 0x1, 0x2)
    OP_28(0x3F, 0x1, 0x4)
    OP_28(0x3F, 0x1, 0x8)
    OP_28(0x3F, 0x1, 0x10)
    OP_28(0x3F, 0x1, 0x20)
    OP_28(0x3F, 0x1, 0x40)
    OP_28(0x3F, 0x1, 0x80)
    OP_28(0x3F, 0x1, 0x100)
    OP_28(0x3F, 0x1, 0x200)
    OP_28(0x3F, 0x1, 0x400)
    OP_28(0x3F, 0x1, 0x800)
    OP_28(0x3F, 0x1, 0x1000)
    OP_28(0x3F, 0x1, 0x2000)
    OP_28(0x3F, 0x1, 0x4000)
    OP_28(0x3F, 0x1, 0x8000)
    OP_28(0x40, 0x4, 0x4)
    OP_28(0x40, 0x4, 0x2)
    OP_28(0x40, 0x4, 0x8)
    OP_28(0x40, 0x4, 0x10)
    OP_28(0x40, 0x4, 0x20)
    OP_28(0x40, 0x1, 0x1)
    OP_28(0x40, 0x1, 0x2)
    OP_28(0x40, 0x1, 0x4)
    OP_28(0x40, 0x1, 0x8)
    OP_28(0x40, 0x1, 0x10)
    OP_28(0x40, 0x1, 0x20)
    OP_28(0x40, 0x1, 0x40)
    OP_28(0x40, 0x1, 0x80)
    OP_28(0x40, 0x1, 0x100)
    OP_28(0x40, 0x1, 0x200)
    OP_28(0x40, 0x1, 0x400)
    OP_28(0x40, 0x1, 0x800)
    OP_28(0x40, 0x1, 0x1000)
    OP_28(0x40, 0x1, 0x2000)
    OP_28(0x40, 0x1, 0x4000)
    OP_28(0x40, 0x1, 0x8000)
    Return()

    # Function_43_329B end

    def Function_44_4E01(): pass

    label("Function_44_4E01")

    OP_AC(0x1)
    OP_AC(0x2)
    OP_AC(0x3)
    OP_AC(0x4)
    OP_AC(0x5)
    OP_AC(0x6)
    OP_AC(0x7)
    OP_AC(0x8)
    OP_AC(0x9)
    OP_AC(0xA)
    OP_AC(0xB)
    OP_AC(0xC)
    OP_AC(0x14)
    OP_AC(0x15)
    OP_AC(0x16)
    OP_AC(0x17)
    OP_AC(0x18)
    OP_AC(0x19)
    OP_AC(0x1A)
    OP_AC(0x1B)
    OP_AC(0x1C)
    OP_AC(0x1D)
    OP_AC(0x1E)
    OP_AC(0x1F)
    OP_AC(0x20)
    OP_AC(0x21)
    OP_AC(0x22)
    OP_AC(0x23)
    OP_AC(0x24)
    OP_AC(0x25)
    OP_AC(0x26)
    OP_AC(0x27)
    OP_AC(0x28)
    OP_AC(0x29)
    OP_AC(0x2A)
    OP_AC(0x2B)
    OP_AC(0x2C)
    OP_AC(0x2D)
    OP_AC(0x2E)
    OP_AC(0x2F)
    OP_AC(0x30)
    OP_AC(0x31)
    OP_AC(0x32)
    OP_AC(0x33)
    OP_AC(0x34)
    OP_AC(0x35)
    OP_AC(0x36)
    OP_AC(0x37)
    OP_AC(0x38)
    OP_AC(0x39)
    OP_AC(0x3A)
    OP_AC(0x3B)
    OP_AC(0x3C)
    OP_AC(0x3D)
    OP_AC(0x3E)
    OP_AC(0x3F)
    OP_AC(0x40)
    OP_AC(0x41)
    OP_AC(0x42)
    OP_AC(0x43)
    OP_AC(0x44)
    OP_AC(0x45)
    OP_AC(0x46)
    OP_AC(0x47)
    OP_AC(0x48)
    OP_AC(0x49)
    OP_AC(0x4A)
    OP_AC(0x4B)
    OP_AC(0x4C)
    Return()

    # Function_44_4E01 end

    SaveToFile()

Try(main)
